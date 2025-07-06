#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_CYAN, WIN_HEIGHT, WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW
from code.Score import load_high_score


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "CYBER", (0, 255, 255), (WIN_WIDTH // 2, 80), glow=True)
            self.menu_text(60, "FLY", (255, 0, 255), (WIN_WIDTH // 2, 140), glow=True)

            for i, opt in enumerate(MENU_OPTION):
                y_pos = 200 + 35 * i
                if i == menu_option:
                    self.menu_text(24, f"> {opt}", C_YELLOW, (WIN_WIDTH // 2, y_pos), glow=True)
                else:
                    self.menu_text(20, opt, C_WHITE, (WIN_WIDTH // 2, y_pos))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        selected_option = MENU_OPTION[menu_option]
                        if selected_option == "SCORE":
                            self.show_score()
                        elif selected_option == "EXIT":
                            pygame.quit()
                            quit()   # encerra o jogo imediatamente
                        else:
                            return selected_option



    def show_score(self):
        font = pygame.font.Font('./asset/fonts/Orbitron-Bold.ttf', 30)
        clock = pygame.time.Clock()
        running = True

        high_score = load_high_score()

        while running:
            self.window.fill((0, 0, 0))

            title = font.render("HIGHEST SCORE", True, (0, 255, 255))
            title_rect = title.get_rect(center=(WIN_WIDTH // 2, 100))
            self.window.blit(title, title_rect)

            score_text = font.render(str(high_score), True, (255, 255, 0))
            score_rect = score_text.get_rect(center=(WIN_WIDTH // 2, 180))
            self.window.blit(score_text, score_rect)

            info = font.render("Press ENTER or ESC to return", True, (255, 255, 255))
            info_rect = info.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 50))
            self.window.blit(info, info_rect)

            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_RETURN, pygame.K_ESCAPE]:
                        running = False

    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, glow=False):

        text_font: Font = pygame.font.Font('./asset/fonts/Orbitron-Bold.ttf', text_size)

        if glow:
            glow_surf = text_font.render(text, True, (100, 255, 255))
            glow_surf.set_alpha(80)
            glow_rect = glow_surf.get_rect(center=text_center_pos)
            self.window.blit(glow_surf, glow_rect)

        # Camada principal
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

# Developed by: Saulo Ruan Nascimento Oliveira