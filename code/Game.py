import pygame
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))
        
    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                current_level = 'Level1'
                score = 0  # inicia o score

                while current_level:
                    level = Level(self.window, current_level, menu_return, score)
                    result = level.run()

                    if result is None:
                        break  # voltou ao menu ou saiu do jogo
                    elif isinstance(result, dict):
                        current_level = result.get("next_level")
                        score = result.get("score", 0)
                    else:
                        current_level = result 
                        
# Developed by: Saulo Ruan Nascimento Oliveira