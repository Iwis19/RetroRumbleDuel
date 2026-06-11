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
SCREEN CONSTANTS
"""

WIDTH, HEIGHT = 1200, 600
MAP_DISPLAY_SIZE = (200, 100)

ORIGIN = (0,0)




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
BAR =      (250,250,250)
CDBLUE =   ( 25,134,252)
YELLOW =   (255,195, 11)
HOVER =    (222,182, 71)




"""
FONTS
"""

menuTextFont = pygame.font.SysFont("calibri", 26, WHITE)
mapSelectionTextFont = pygame.font.SysFont("calibri", 28, WHITE)
continueTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 21)
mapTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 21)
selectMapFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
selectedMapFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 23)
countdownFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 39)
guiFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
guiInformationFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 15)
playerNameFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
controlFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
controlKeysFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 17)
selectCharacterFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 28)
playerCharacterNameTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
takenCharacterTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 25)
nameTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 20)
gameOverTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 60)
gameCloseTextFont = pygame.font.Font(asset_path("font", "PixelDigivolve.ttf"), 18)




"""
AUDIOS
"""

menuBackgroundMusic = pygame.mixer.Sound(asset_path("backgroundmusic", "main_menu_music.mp3"))
menuBackgroundMusic.set_volume(0.04)

selectionSound = pygame.mixer.Sound(asset_path("backgroundmusic", "selectionSound.mp3"))
selectionSound.set_volume(1)

buttonClick = pygame.mixer.Sound(asset_path("backgroundmusic", "buttonClick.mp3"))
buttonClick.set_volume(1)

countdownSound = pygame.mixer.Sound(asset_path("backgroundmusic", "countdownSound.mp3"))
countdownSound.set_volume(0.7)



"""
TIMERS
"""

# clock = pygame.time.Clock()
# menuBackgroundReferenceTime = pygame.time.get_ticks()
# selectedCharacterReferenceTime = pygame.time.get_ticks()
# animationTimeP1 = pygame.time.get_ticks()
# animationTimeP2 = pygame.time.get_ticks()
# gameBackgroundTime = pygame.time.get_ticks()
# gameCloseTime = pygame.time.get_ticks()
# animationTimeP1 = pygame.time.get_ticks()
# animationTimeP2 = pygame.time.get_ticks()
# gameBackgroundTime = pygame.time.get_ticks()
# countdownStartTime = pygame.time.get_ticks()


