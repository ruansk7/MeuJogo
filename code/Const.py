# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Lv1bg0': 0,
    'Lv1bg1': 1,
    'Lv1bg2': 2,
    'Lv1bg3': 3,
    'Lv1bg4': 4,
    'Lv1bg5': 5,
    'Lv1bg6': 6,
    'Lv1bg7': 7,
    'Lv1bg8': 8,
    'Lv1bg9': 9,
    'Lv1bg10': 10,
    'Lv2bg0': 0,
    'Lv2bg1': 1,
    'Lv2bg2': 2,
    'Lv2bg3': 3,
    'Lv2bg4': 4,
    'Lv2bg5': 5,
    'Lv2bg6': 6,
    'Lv2bg7': 7,
    'Lv2bg8': 8,
    'Lv3bg0': 0,
    'Lv3bg1': 1,
    'Lv3bg2': 2,
    'Lv3bg3': 3,
    'Lv3bg4': 4,
    'Lv3bg5': 5,
    'Lv3bg6': 6,
    'Lv3bg7': 7,
    'Lv4bg0': 0,
    'Lv4bg1': 1,
    'Lv4bg2': 2,
    'Lv4bg3': 3,
    'Lv4bg4': 4,
    'Lv4bg5': 5,
    'Lv4bg6': 6,
    'Lv4bg7': 7,
    'Lv4bg8': 8,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 3,
    'Enemy2': 3,
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

# Developed by: Saulo Ruan Nascimento Oliveira
