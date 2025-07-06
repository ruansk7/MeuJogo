import random
import sys
import time
from tkinter.font import Font
import pygame
from code.Background import Background
from code.Const import C_WHITE, EVENT_ENEMY, SPAWN_TIME, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Explosion import Explosion
from code.Score import save_high_score, load_high_score



class Level:
    def __init__(self, window, name, game_mode, score=0):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        level_number = int(name.replace("Level", ""))
        self.entity_list.extend(EntityFactory.get_entity(f'Lv{level_number}bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        self.score = score
        self.start_ticks = pygame.time.get_ticks()
        self.start_time = time.time()
        
        base_spawn = SPAWN_TIME
        # Spawn mais rápido conforme nível aumenta. Nunca menor que 300 ms.
        spawn_time = max(300, base_spawn - (level_number - 1) * 200)
            
        pygame.time.set_timer(EVENT_ENEMY, spawn_time)

    
    def level_text_decorated(self, text_size, text, base_color, glow_color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        
        # Texto sombra (glow)
        glow_surf = font.render(text, True, glow_color)
        glow_rect = glow_surf.get_rect(center=(pos[0]+2, pos[1]+2))
        self.window.blit(glow_surf, glow_rect)
        
        # Texto principal
        main_surf = font.render(text, True, base_color)
        main_rect = main_surf.get_rect(center=pos)
        self.window.blit(main_surf, main_rect)

    
    def fade_transition_to_next_level(self, next_level_name):
        level_number = next_level_name.replace("Level", "")
        next_bg_name = f"Lv{level_number}bg"
        next_bg_entities = EntityFactory.get_entity(next_bg_name)

        if not next_bg_entities:
            return  # evita crash se o fundo não existir

        for alpha in range(0, 256, 10):  # fade in
            self.window.fill((0, 0, 0))

            # fundo atual
            for ent in self.entity_list:
                if hasattr(ent, 'surf') and hasattr(ent, 'rect'):
                    if isinstance(ent, Background):
                        self.window.blit(ent.surf, ent.rect)

            # novo fundo com transparência crescente
            for new_bg in next_bg_entities:
                if hasattr(new_bg, 'surf') and hasattr(new_bg, 'rect'):
                    faded_surf = new_bg.surf.copy()
                    faded_surf.set_alpha(alpha)
                    self.window.blit(faded_surf, new_bg.rect)

            pygame.display.flip()
            pygame.time.delay(30)

    
    def game_over(self):
        player = next((e for e in self.entity_list if e.name == 'Player1'), None)

        # Explosão
        if player:
            from code.Explosion import Explosion
            explosion = Explosion(
                image_path='./asset/explosion.png',
                frame_size=(32, 32),
                num_frames=6,
                position=player.rect.center
            )

            while not explosion.done:
                self.window.fill((0, 0, 0))
                for ent in self.entity_list:
                    if hasattr(ent, 'surf') and hasattr(ent, 'rect'):
                        self.window.blit(ent.surf, ent.rect)
                explosion.update()
                explosion.draw(self.window)
                pygame.display.flip()
                pygame.time.delay(30)

            high_score = load_high_score()
            if self.score > high_score:
                save_high_score(self.score)

        # Tela de Game Over com opções
        font = pygame.font.SysFont("Lucida Sans Typewriter", 36)
        options = ["Reiniciar", "Menu"]
        selected = 0

        while True:
            self.window.fill((0, 0, 0))
            title = font.render("GAME OVER", True, (255, 0, 0))
            title_rect = title.get_rect(center=(WIN_WIDTH // 2, 80))
            self.window.blit(title, title_rect)

            for i, opt in enumerate(options):
                color = (255, 255, 0) if i == selected else (255, 255, 255)
                txt = font.render(opt, True, color)
                rect = txt.get_rect(center=(WIN_WIDTH // 2, 180 + i * 50))
                self.window.blit(txt, rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if options[selected] == "Reiniciar":
                            from code.EntityFactory import EntityFactory
                            # Recomeça o mesmo level do zero
                            new_level = Level(self.window, self.name, self.game_mode)
                            return new_level.run()
                        elif options[selected] == "Menu":
                            return "menu"


    def get_next_level_name(self):
        if self.name.startswith("Level"):
            level_num = int(self.name.replace("Level", ""))
            if level_num >= 4:
                # Após Lv4, retorna aleatório entre Lv1 e Lv4
                level_num = random.randint(1, 4)
            else:
                level_num += 1
            return f"Level{level_num}"
        return None

      
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            current_time = time.time()
            time_this_level = current_time - self.start_time  # tempo em segundos no nível atual

            score_rate = 5  # pontos por segundo (pode ajustar)
            total_score = self.score + int(time_this_level * score_rate)

            elapsed_time = time_this_level * 1000  # milissegundos

            if elapsed_time >= self.timeout:
                next_level_name = self.get_next_level_name()
                self.fade_transition_to_next_level(next_level_name)

                # Atualiza o score acumulado para passar ao próximo nível
                self.score = total_score

                return {"next_level": next_level_name, "score": self.score}

            player = next((e for e in self.entity_list if e.name == 'Player1'), None)
            enemies = [e for e in self.entity_list if e.name in ['Enemy1', 'Enemy2']]

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            if player:
                for enemy in enemies:
                    if player.rect.colliderect(enemy.rect):
                        result = self.game_over()
                        if result == "menu":
                            return None  # volta ao menu
                        elif result == "restart":
                            return self.run()  # reinicia o mesmo nível

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice)) 

            # Mostra o score dinâmico acumulado em tempo real
            self.level_text_decorated(
                24,
                f'Score: {total_score}',
                (255, 255, 0),
                (255, 150, 0),
                (WIN_WIDTH // 2, 50)
            )
            pygame.display.flip()


            
            
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)