import os
import pygame

"""
FILE PATHS
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

if not os.path.isdir(os.path.join(ASSETS_DIR, "font")):
    ASSETS_DIR = BASE_DIR

def asset_path(*path_parts):
    return os.path.join(ASSETS_DIR, *path_parts)


"""
GENERAL CONSTANTS
"""

FPS = 30
UPDATE_INTERVAL = 150
TICK_SPEED = 1000

WIDTH, HEIGHT = 1200, 600

LEFT = 0
RIGHT = WIDTH
TOP = 0
BOTTOM = HEIGHT

ORIGIN = (0,0)

FORWARD_BUTTON_X = 1115
BACK_BUTTON_X = 85
MOVE_BUTTON_Y = 500
MOVE_BUTTON_H = 36
MOVE_BOTTON_W = 22

FORWARD_BUTTON_RECT = pygame.Rect(FORWARD_BUTTON_X, MOVE_BUTTON_Y, MOVE_BOTTON_W, MOVE_BUTTON_H)
BACK_BUTTON_RECT = pygame.Rect(BACK_BUTTON_X - MOVE_BOTTON_W, MOVE_BUTTON_Y, MOVE_BOTTON_W, MOVE_BUTTON_H)

PFP_WIDTH = 72
PFP_HEIGHT = 72
PFP_DIMENSION = (PFP_WIDTH, PFP_HEIGHT)

PORTRAIT_HEIGHT = 130
PORTRAIT_WIDTH = 130
PORTRAIT_DIMENSION = (PORTRAIT_WIDTH, PORTRAIT_HEIGHT)

IMAGE_WIDTH = 900
IMAGE_HEIGHT = 400
CHARACTER_DIMENSION = (IMAGE_WIDTH, IMAGE_HEIGHT)


"""
MAPS PROPERTY
"""

MAP_NUMBER = [0, 1, 2, 3, 4, 5]
MAP_DISPLAY_SIZE = (200, 100)
MAP_GROUND_LEVEL = [0, 500, 550, 565, 575, 553]


"""
CHARACTERS PROPERTY
"""

JUMP_SPEED = -25
GRAVITY = 2
RUNNING_SPEED = 12
MAX_HEALTH = 100

CHARACTER_NAMES = ['None Selected', 'Fire Knight', 'Wind Hashashin', 'Water Priestess', 'Metal Bladekeeper']
CHARACTER_FILE_NAMES = [None, 'fire_knight', 'wind_hashashin', 'water_priestess', 'metal_bladekeeper']

HITBOX_WIDTH = [0, 100, 90, 80, 100]
HITBOX_HEIGHT = [0, 150, 125, 125, 138]

# atk hitboxes
ATK1_Y_SHIFT = [0, -100, 25, 40, 30]
ATK1_WIDTH = [0, 160, 75, 145, 120]
ATK1_HEIGHT = [0, 250, 45, 15, 70]

ATK2_Y_SHIFT = [0, -10, -25, 40, -30]
ATK2_WIDTH = [0, 410, 120, 240, 580]
ATK2_HEIGHT = [0, 170, 130, 15, 180]

# frames of atk hitbox
ATK1_HIT_FRAME = [0, 5, 1, 3, 2]
ATK2_HIT_FRAME = [0, 13, 9, 15, 4]

# atk cooldown
ATK1_COOLDOWN = [0, 750, 1000, 850, 1000]
ATK2_COOLDOWN = [0, 5000, 4400, 4000, 7400]

# atk damage
ATK1_DAMAGE = [0, 24, 16, 14, 16]
ATK2_DAMAGE = [0, 34, 32, 29, 37]

INITIAL_X = [0, -200, 500]
INITIAL_Y = 150


"""
PLAYER HUD 
"""

REFERENCE_BAR_X = [0, 130, 1070]


"""
COLORS
"""

BLACK =    (  0,  0,  0)
WHITE =    (255,255,255)
RED =      (255,  0,  0)
GREEN =    (  0,255,  0)
BLUE =     (  0,  0,255)
GRAY =     (128,128,128)
DARKRED =  (169, 29, 58)
BROWN =    (207,132, 62)
BAR_COLOR =      (250,250,250)
CD_BLUE =   ( 25,134,252)
YELLOW =   (255,195, 11)
HOVER =    (222,182, 71)




"""
FONTS
"""

continue_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 21)
map_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 21)
select_map_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
selected_map_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 23)
countdown_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 39)
gui_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
gui_information_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 15)
control_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
control_keys_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 17)
select_character_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 28)
player_character_name_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
taken_character_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
name_text_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
game_over_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 60)
game_close_font = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 18)




"""
AUDIOS
"""

menuBackgroundMusic = pygame.mixer.Sound(asset_path("backgroundmusic", "main_menu_music.mp3"))
menuBackgroundMusic.set_volume(0.04)

selection_sound = pygame.mixer.Sound(asset_path("backgroundmusic", "selectionSound.mp3"))
selection_sound.set_volume(1)

button_click_sound = pygame.mixer.Sound(asset_path("backgroundmusic", "buttonClick.mp3"))
button_click_sound.set_volume(1)

countdownSound = pygame.mixer.Sound(asset_path("backgroundmusic", "countdownSound.mp3"))
countdownSound.set_volume(0.7)



"""
TIMERS
"""

clock = pygame.time.Clock()
# menuBackgroundReferenceTime = pygame.time.get_ticks()
# selectedCharacterReferenceTime = pygame.time.get_ticks()
# animationTimeP1 = pygame.time.get_ticks()
# animationTimeP2 = pygame.time.get_ticks()
# gameBackgroundTime = pygame.time.get_ticks()
# gameCloseTime = pygame.time.get_ticks()
# animationTimeP1 = pygame.time.get_ticks()
# animationTimeP2 = pygame.time.get_ticks()
# gameBackgroundTime = pygame.time.get_ticks()
#countdown_start_time = pygame.time.get_ticks()


