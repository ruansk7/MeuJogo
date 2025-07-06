import os
import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case bg_name if bg_name.startswith("Lv") and bg_name.endswith("bg"):
                list_bg = []
                asset_dir = "./asset"
                
                i = 0
                while True:
                    file_name = f"{bg_name}{i}.png"
                    file_path = os.path.join(asset_dir, file_name)
                    
                    if not os.path.isfile(file_path):
                        break

                    list_bg.append(Background(f'{bg_name}{i}', (0,0)))
                    list_bg.append(Background(f'{bg_name}{i}', (WIN_WIDTH, 0)))
                    i += 1

                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
   
# Developed by: Saulo Ruan Nascimento Oliveira 