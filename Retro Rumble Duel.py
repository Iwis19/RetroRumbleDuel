import pygame
import sys
import os

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 0)
WIDTH = 1200    
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Rumble Duel")


#colors
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


#fonts
menuTextFont = pygame.font.SysFont("calibri", 26, WHITE)
mapSelectionTextFont = pygame.font.SysFont("calibri", 28, WHITE)
continueTextFont = pygame.font.Font("font/PixelDigivolve.ttf", 21)
mapTextFont = pygame.font.Font("font/PixelDigivolve.ttf", 21)
selectMapFont = pygame.font.Font('font/PixelDigivolve.ttf', 25)
selectedMapFont = pygame.font.Font('font/PixelDigivolve.ttf', 23)
countdownFont = pygame.font.Font('font/PixelDigivolve.ttf', 39)
guiFont = pygame.font.Font('font/PixelDigivolve.ttf', 20)
guiInformationFont = pygame.font.Font('font/PixelDigivolve.ttf', 15)
playerNameFont = pygame.font.Font("font/PixelDigivolve.ttf", 20)
controlFont = pygame.font.Font("font/PixelDigivolve.ttf", 20)
controlKeysFont = pygame.font.Font("font/PixelDigivolve.ttf", 17)
selectCharacterFont = pygame.font.Font('font/PixelDigivolve.ttf', 28)
playerCharacterNameTextFont = pygame.font.Font('font/PixelDigivolve.ttf', 25)
takenCharacterTextFont = pygame.font.Font('font/PixelDigivolve.ttf', 25)
nameTextFont = pygame.font.Font("font/PixelDigivolve.ttf", 20)
gameOverTextFont = pygame.font.Font('font/PixelDigivolve.ttf', 60)
gameCloseTextFont = pygame.font.Font('font/PixelDigivolve.ttf', 18)


#audio files
menuBackgroundMusic = pygame.mixer.Sound('backgroundmusic/main_menu_music.mp3')
menuBackgroundMusic.set_volume(0.04)

selectionSound = pygame.mixer.Sound('backgroundmusic/selectionSound.mp3')
selectionSound.set_volume(1)

buttonClick = pygame.mixer.Sound('backgroundmusic/buttonClick.mp3')
buttonClick.set_volume(1)

countdownSound = pygame.mixer.Sound('backgroundmusic/countdownSound.mp3')
countdownSound.set_volume(0.7)


#CONSTANTS
ORIGIN = (0,0)

FPS = 30

LEFT = 0
RIGHT = WIDTH
TOP = 0
BOTTOM = HEIGHT

MAP_DISPLAY_SIZE = (200, 100)

IMAGE_WIDTH = 900
IMAGE_HEIGHT = 400
CHARACTER_DIMENSION = (IMAGE_WIDTH, IMAGE_HEIGHT)

PFP_WIDTH = 72
PFP_HEIGHT = 72
PFP_DIMENSION = (PFP_WIDTH, PFP_HEIGHT)

PORTRAIT_HEIGHT = 130
PORTRAIT_WIDTH = 130
PORTRAIT_DIMENSION = (PORTRAIT_WIDTH, PORTRAIT_HEIGHT)

CHARACTER_DIMENSION = (IMAGE_WIDTH, IMAGE_HEIGHT)
PFP_DIMENSION = (PFP_WIDTH, PFP_HEIGHT)

MAP1_GROUND_LEVEL = 500
MAP2_GROUND_LEVEL = 550
MAP3_GROUND_LEVEL = 565
MAP4_GROUND_LEVEL = 575
MAP5_GROUND_LEVEL = 553

JUMP_SPEED = -25
GRAVITY = 2
RUNNING_SPEED = 12
MAX_HEALTH = 100

#-----------------------------------LOADING BACKGROUNDS-------------------------------------#
#solid black background
solidBlack = pygame.transform.scale(pygame.image.load('COUNTDOWNBACKGROUND/solid_black.png'), (WIDTH, 400)).convert()
solidBlack.set_alpha(210)

#menu background 
menuBackground = []

for tiles in range (len(os.listdir(f'MENUBACKGROUND')) - 1):
    menuImage = pygame.transform.scale(pygame.image.load("MENUBACKGROUND/tile00"+ str(tiles) + ".png"), (WIDTH,HEIGHT)).convert_alpha()
    menuBackground.append(menuImage)

#map 1
selectionBackground1Display = pygame.transform.scale(pygame.image.load("MAP1/tile000.png"), MAP_DISPLAY_SIZE).convert_alpha()
background1 = []
for tiles in range(len(os.listdir(f"MAP1"))):
    background1Tile = pygame.transform.scale(pygame.image.load(f"MAP1/tile00{tiles}.png"), (WIDTH, HEIGHT)).convert_alpha()
    background1.append(background1Tile)


#map 2
selectionBackground2Display = pygame.transform.scale(pygame.image.load("MAP2/tile000.png"), MAP_DISPLAY_SIZE).convert_alpha()
background2 = []
for tiles in range (0, 10):     #only 1 frame in file, 10 as a place holder as in animation
    background2Tile = pygame.transform.scale(pygame.image.load(f"MAP2/tile000.png"), (WIDTH, HEIGHT)).convert_alpha()
    background2.append(background2Tile)


#map 3
selectionBackground3Display = pygame.transform.scale(pygame.image.load("MAP3/tile000.png"), MAP_DISPLAY_SIZE).convert_alpha()
background3 = []
for tiles in range(len(os.listdir(f"MAP3"))):
    background3Tile = pygame.transform.scale(pygame.image.load(f"MAP3/tile00{tiles}.png"), (WIDTH, HEIGHT)).convert_alpha()
    background3.append(background3Tile)


#map 4
selectionBackground4Display = pygame.transform.scale(pygame.image.load("MAP4/tile000.png"), MAP_DISPLAY_SIZE).convert_alpha()
background4 = []
for tiles in range(len(os.listdir(f"MAP4"))):
    background4Tile = pygame.transform.scale(pygame.image.load(f"MAP4/tile00{tiles}.png"), (WIDTH, HEIGHT)).convert_alpha()
    background4.append(background4Tile)


#map 5
selectionBackground5Display = pygame.transform.scale(pygame.image.load("MAP5/tile000.png"), MAP_DISPLAY_SIZE).convert_alpha()
background5 = []
for tiles in range(len(os.listdir(f"MAP5"))):
    background5Tile = pygame.transform.scale(pygame.image.load(f"MAP5/tile00{tiles}.png"), (WIDTH, HEIGHT)).convert_alpha()
    background5.append(background5Tile)
#-------------------------------------------------------------------------------------------#


#----------------------------------LOADING CHARACTERS---------------------------------------#
characterNames = ['None Selected', 'Fire Knight', 'Wind Hashashin', 'Water Priestess', 'Metal Bladekeeper']

#character 1
character1_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character1_ANIMATIONLIST_RIGHT = []
character1_ANIMATIONLIST_LEFT = []
character1ProfilePicture = pygame.transform.scale(pygame.image.load('character1/fire_knight.png'), PFP_DIMENSION).convert_alpha()
character1SelectionPicture = pygame.transform.scale(pygame.image.load("character1/fire_knight.png"), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character1_ACTIONS)):
    temp_list1_right = []
    temp_list1_left = []
    frames1 = len(os.listdir(f"character1/png/0{animation + 1}_{character1_ACTIONS[animation]}"))
    for items in range (frames1):
        tile1right = pygame.transform.scale(pygame.image.load(f"character1/png/0{animation + 1}_{character1_ACTIONS[animation]}/{character1_ACTIONS[animation]}_{items + 1}.png"), CHARACTER_DIMENSION).convert_alpha()
        tile1left = pygame.transform.flip(tile1right, True, False).convert_alpha()
        temp_list1_right.append(tile1right)
        temp_list1_left.append(tile1left)
    character1_ANIMATIONLIST_RIGHT.append(temp_list1_right)
    character1_ANIMATIONLIST_LEFT.append(temp_list1_left)


#character 2
character2_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character2_ANIMATIONLIST_RIGHT = []
character2_ANIMATIONLIST_LEFT = []
character2ProfilePicture = pygame.transform.scale(pygame.image.load('character2/wind_hashashin.png'), PFP_DIMENSION).convert_alpha()
character2SelectionPicture = pygame.transform.scale(pygame.image.load("character2/wind_hashashin.png"), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character2_ACTIONS)):
    temp_list2_right = []
    temp_list2_left = []
    frames2 = len(os.listdir(f"character2/png/0{animation + 1}_{character1_ACTIONS[animation]}"))
    for items in range (frames2):
        tile2right = pygame.transform.scale(pygame.image.load(f"character2/png/0{animation + 1}_{character1_ACTIONS[animation]}/{character1_ACTIONS[animation]}_{items + 1}.png"), CHARACTER_DIMENSION).convert_alpha()
        tile2left = pygame.transform.flip(tile2right, True, False).convert_alpha()
        temp_list2_right.append(tile2right)
        temp_list2_left.append(tile2left)
    character2_ANIMATIONLIST_RIGHT.append(temp_list2_right)
    character2_ANIMATIONLIST_LEFT.append(temp_list2_left)


#character 3
character3_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character3_ANIMATIONLIST_RIGHT = []
character3_ANIMATIONLIST_LEFT = []
character3ProfilePicture = pygame.transform.scale(pygame.image.load('character3/water_priestess.png'), PFP_DIMENSION).convert_alpha()
character3SelectionPicture = pygame.transform.scale(pygame.image.load("character3/water_priestess.png"), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character3_ACTIONS)):
    temp_list3_right = []
    temp_list3_left = []
    frames3 = len(os.listdir(f"character3/png/0{animation + 1}_{character1_ACTIONS[animation]}"))
    for items in range (frames3):
        tile3right = pygame.transform.scale(pygame.image.load(f"character3/png/0{animation + 1}_{character3_ACTIONS[animation]}/{character3_ACTIONS[animation]}_{items + 1}.png"), CHARACTER_DIMENSION).convert_alpha()
        tile3left = pygame.transform.flip(tile3right, True, False).convert_alpha()
        temp_list3_right.append(tile3right)
        temp_list3_left.append(tile3left)
    character3_ANIMATIONLIST_RIGHT.append(temp_list3_right)
    character3_ANIMATIONLIST_LEFT.append(temp_list3_left)


#character 4
character4_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character4_ANIMATIONLIST_RIGHT = []
character4_ANIMATIONLIST_LEFT = []
character4ProfilePicture = pygame.transform.scale(pygame.image.load('character4/metal_bladekeeper.png'), PFP_DIMENSION).convert_alpha()
character4SelectionPicture = pygame.transform.scale(pygame.image.load("character4/metal_bladekeeper.png"), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character4_ACTIONS)):
    temp_list4_right = []
    temp_list4_left = []
    frames4 = len(os.listdir(f"character4/png/0{animation + 1}_{character1_ACTIONS[animation]}"))
    for items in range (frames4):
        tile4right = pygame.transform.scale(pygame.image.load(f"character4/png/0{animation + 1}_{character4_ACTIONS[animation]}/{character4_ACTIONS[animation]}_{items + 1}.png"), CHARACTER_DIMENSION).convert_alpha()
        tile4left = pygame.transform.flip(tile4right, True, False).convert_alpha()
        temp_list4_right.append(tile4right)
        temp_list4_left.append(tile4left)
    character4_ANIMATIONLIST_RIGHT.append(temp_list4_right)
    character4_ANIMATIONLIST_LEFT.append(temp_list4_left)

#all animation list:
displayCharacterList = [character1_ANIMATIONLIST_RIGHT, character2_ANIMATIONLIST_RIGHT, character3_ANIMATIONLIST_RIGHT, character4_ANIMATIONLIST_RIGHT]
#-------------------------------------------------------------------------------------------#


#-------------------------------------------VARIABLES---------------------------------------#
#user inputs
selectedMap = 0
player1Character = 0
player2Character = 0

#menu variables
menuFrame = 0

#map display vars
map1DisplayX = 60
map2DisplayX = 280
map3DisplayX = 500
map4DisplayX = 720
map5DisplayX = 940
mapDisplayY = 288
mapDisplayWidth = 200

mapSelectionArrowX = [-1000, map1DisplayX + mapDisplayWidth//2, map2DisplayX + mapDisplayWidth//2, map3DisplayX + mapDisplayWidth//2, map4DisplayX + mapDisplayWidth//2, map5DisplayX + mapDisplayWidth//2]
mapselectionArrowY = mapDisplayY + 125


#back & forward buttons
backButtonX = 85
forwardButtonX = 1115
buttonH = 36    #for back & forward button heights
buttonY = 500
buttonW = 22


#character selection
character1SelectionPictureX = 205
character3SelectionPictureX = 205
character2SelectionPictureX = 385
character4SelectionPictureX = 385

character1SelectionPictureY = 160
character3SelectionPictureY = 350
character2SelectionPictureY = 160
character4SelectionPictureY = 350

characterSelectionP1ArrowX = [-1000, character1SelectionPictureX + PORTRAIT_WIDTH//2, character2SelectionPictureX + PORTRAIT_WIDTH//2, character3SelectionPictureX + PORTRAIT_WIDTH//2, character4SelectionPictureX + PORTRAIT_WIDTH//2]
characterSelectionP2ArrowX = [-1000, character1SelectionPictureX + PORTRAIT_WIDTH//2, character2SelectionPictureX + PORTRAIT_WIDTH//2, character3SelectionPictureX + PORTRAIT_WIDTH//2, character4SelectionPictureX + PORTRAIT_WIDTH//2]
characterSelectionP1ArrowY = 0
characterSelectionP2ArrowY = 0

frame = 0

characterDisplayXList = [character1SelectionPictureX, character2SelectionPictureX, character3SelectionPictureX, character4SelectionPictureX]
characterDisplayYList = [character1SelectionPictureY, character2SelectionPictureY, character3SelectionPictureY, character4SelectionPictureY]


#countdown 
second = 6


#timers for frames
clock = pygame.time.Clock()
menuBackgroundReferenceTime = pygame.time.get_ticks()
selectedCharacterReferenceTime = pygame.time.get_ticks()
animationTimeP1 = pygame.time.get_ticks()
animationTimeP2 = pygame.time.get_ticks()
gameBackgroundTime = pygame.time.get_ticks()
gameCloseTime = pygame.time.get_ticks()
animationTimeP1 = pygame.time.get_ticks()
animationTimeP2 = pygame.time.get_ticks()
gameBackgroundTime = pygame.time.get_ticks()
countdownStartTime = pygame.time.get_ticks()


#fight 
mapFrame = 0

player1Health = 100
player2Health = 100

dx1 = 0
dy1 = 0

dx2 = 0
dy2 = 0

player1Direction = 'right'
player2Direction = 'left'

playerW = 900
playerH = 400
player1_y = 150
player1_x = -200
player2_y = 150
player2_x = 500

referenceBarX_LEFT = 130
referenceBarX_RIGHT = 1070

pfpBoxY = 55
pfpBoxWidth = 83
pfpBoxHeight = 80
pfpBox1X = referenceBarX_LEFT - pfpBoxWidth + 3
pfpBox2X = referenceBarX_RIGHT - 3

nameBarY = 55
nameBarWidth = 120
NameBarHeight = 30
nameBar1X = referenceBarX_LEFT
nameBar2X = referenceBarX_RIGHT - nameBarWidth

healthBarWidth = 210
healthWidth = 200
healthBarHeight = 30
healthBarY = 80
health1BarX = referenceBarX_LEFT
health2BarX = referenceBarX_RIGHT - healthBarWidth

cdBar1Y = 105
cdBar1Height = 30
cdBar1Width = 150
fullcdBar1Width = cdBar1Width - 5*2
cdBar1P1 = fullcdBar1Width
cdBar1P2 = fullcdBar1Width
cdBar1P1X = referenceBarX_LEFT
cdBar1P2X = referenceBarX_RIGHT - cdBar1Width

cdBar2Y = 130
cdBar2Height = 30
cdBar2Width = 250
fullcdBar2Width = cdBar2Width - 5*2
cdBar2P1 = 0
cdBar2P2 = 0
cdBar2P1X = referenceBarX_LEFT - pfpBoxWidth + 3
cdBar2P2X = referenceBarX_RIGHT - cdBar2Width + pfpBoxWidth - 3

actionP1 = 0
actionP2 = 0

frameP1 = 0
frameP2 = 0

character1_hitbox_width = 100
character1_hitbox_height = 150

character2_hitbox_width = 90
character2_hitbox_height = 125

character3_hitbox_width = 80
character3_hitbox_height = 125

character4_hitbox_width = 100
character4_hitbox_height = 138


#atk hitboxes
character1_atk1_y_shift = -100   #atk1
character1_atk1_width = 160
character1_atk1_height = 250

character2_atk1_y_shift = 25
character2_atk1_width = 75
character2_atk1_height = 45

character3_atk1_y_shift = 40
character3_atk1_width = 145
character3_atk1_height = 15

character4_atk1_y_shift = 30
character4_atk1_width = 120
character4_atk1_height = 70

character1_atk2_y_shift = -10  #atk2
character1_atk2_width = 410
character1_atk2_height = 170

character2_atk2_y_shift = -25
character2_atk2_width = 120
character2_atk2_height = 130

character3_atk2_y_shift = 40
character3_atk2_width = 240
character3_atk2_height = 15

character4_atk2_y_shift = -30
character4_atk2_width = 580
character4_atk2_height = 180


#frames of atk hitbox
character1_atk1_hitframe = 5
character2_atk1_hitframe = 1
character3_atk1_hitframe = 3
character4_atk1_hitframe = 2

character1_atk2_hitframe = 13
character2_atk2_hitframe = 9
character3_atk2_hitframe = 15
character4_atk2_hitframe = 4


#atk cooldown           #1 second = 1000
character1_atk1_cooldown = 750    #atk1
character2_atk1_cooldown = 1000
character3_atk1_cooldown = 850
character4_atk1_cooldown = 1000

character1_atk2_cooldown = 5000   #atk 2
character2_atk2_cooldown = 4400
character3_atk2_cooldown = 4000
character4_atk2_cooldown = 7400


#atk damage
character1_atk1_damage = 24   #atk1
character2_atk1_damage = 16
character3_atk1_damage = 14    
character4_atk1_damage = 16

character1_atk2_damage = 34   #atk2
character2_atk2_damage = 32
character3_atk2_damage = 29
character4_atk2_damage = 37

player1_attacked_atk1 = False
player2_attacked_atk1 = False

player1_attacked_atk2 = False
player2_attacked_atk2 = False

player1_hitbox_x = 0
player1_hitbox_y = 0

player2_hitbox_x = 0
player2_hitbox_y = 0


#list of all character attributes to integrate characters
pfp = [0, character1ProfilePicture, character2ProfilePicture, character3ProfilePicture, character4ProfilePicture]
animationlist_left = [0, character1_ANIMATIONLIST_LEFT, character2_ANIMATIONLIST_LEFT, character3_ANIMATIONLIST_LEFT, character4_ANIMATIONLIST_LEFT]
animationlist_right = [0, character1_ANIMATIONLIST_RIGHT, character2_ANIMATIONLIST_RIGHT, character3_ANIMATIONLIST_RIGHT, character4_ANIMATIONLIST_RIGHT]

hitbox_width = [0, character1_hitbox_width, character2_hitbox_width, character3_hitbox_width, character4_hitbox_width]
hitbox_height = [0, character1_hitbox_height, character2_hitbox_height, character3_hitbox_height, character4_hitbox_height]

atk1_width = [0, character1_atk1_width, character2_atk1_width, character3_atk1_width, character4_atk1_width]
atk1_height = [0, character1_atk1_height, character2_atk1_height, character3_atk1_height, character4_atk1_height]
atk1_hitframe = [0, character1_atk1_hitframe, character2_atk1_hitframe, character3_atk1_hitframe, character4_atk1_hitframe]
atk1_y_shift = [0, character1_atk1_y_shift, character2_atk1_y_shift, character3_atk1_y_shift, character4_atk1_y_shift]
atk1_damage = [0, character1_atk1_damage, character2_atk1_damage, character3_atk1_damage, character4_atk1_damage]
atk1_cooldown = [0, character1_atk1_cooldown, character2_atk1_cooldown, character3_atk1_cooldown, character4_atk1_cooldown]

atk2_width = [0, character1_atk2_width, character2_atk2_width, character3_atk2_width, character4_atk2_width]
atk2_height = [0, character1_atk2_height, character2_atk2_height, character3_atk2_height, character4_atk2_height]
atk2_hitframe = [0, character1_atk2_hitframe, character2_atk2_hitframe, character3_atk2_hitframe, character4_atk2_hitframe]
atk2_y_shift = [0, character1_atk2_y_shift, character2_atk2_y_shift, character3_atk2_y_shift, character4_atk2_y_shift]
atk2_damage = [0, character1_atk2_damage, character2_atk2_damage, character3_atk2_damage, character4_atk2_damage]
atk2_cooldown = [0, character1_atk2_cooldown, character2_atk2_cooldown, character3_atk2_cooldown, character4_atk2_cooldown]


#map attributes
mapGroundLevel = [0, MAP1_GROUND_LEVEL, MAP2_GROUND_LEVEL, MAP3_GROUND_LEVEL, MAP4_GROUND_LEVEL, MAP5_GROUND_LEVEL]
mapPool = [0, background1, background2, background3, background4, background5]


#boolean for animation and conditions
player1_atk1_animation = False
player1_atk2_animation = False

player2_atk1_animation = False
player2_atk2_animation = False

player1_takehit_animation = False
player2_takehit_animation = False

player1_death_animation = False
player2_death_animation = False

stopAnimationP1 = False
stopAnimationP2 = False

player1_alive = True
player2_alive = True

deathAnimationOver = False

lastAtk1TimeP1 = 0
lastAtk1TimeP2 = 0
lastAtk2TimeP1 = 0
lastATk2TimeP2 = 0

timeP1 = 0
timeP2 = 0

closeCountdownLength = 20

#-----------------------------------------FUNCTIONS ----------------------------------------#
def closeGame():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:       #if escape is pressed, escape game
        pygame.quit()
        sys.exit()



def displayMenuBackground():

    global menuBackgroundReferenceTime
    global menuFrame

    #centre game name title image
    titleText = pygame.transform.scale(pygame.image.load("MENUBACKGROUND/RetroRumbleDuel.png"), (WIDTH,HEIGHT)).convert_alpha()
    continueText = continueTextFont.render("Hold SPACEBAR to Continue", True, WHITE)
    continueTextLocation = continueText.get_rect(center = (WIDTH//2, 370))
    
    updateSpeed = 150

    timeBG = pygame.time.get_ticks()

    #when updateSpeed is reached, update frame and reset timer
    if timeBG - menuBackgroundReferenceTime > updateSpeed:
        menuBackgroundReferenceTime = timeBG
        menuFrame += 1

    #prevents going past frame limit
    if menuFrame >= len(menuBackground):
        menuFrame = 0

    gameWindow.blit(menuBackground[menuFrame], (ORIGIN))
    gameWindow.blit(continueText, continueTextLocation)
    gameWindow.blit(titleText, (0, -30))
    


def displayMapSelectionMenu():

    gameWindow.blit(menuBackground[0], ORIGIN)

    #render text
    chooseMap = selectMapFont.render("Select the Duel Stage:", True, WHITE)
    chooseMapLocation = chooseMap.get_rect(center = (WIDTH//2, 170))
    map1Text = mapTextFont.render("Map 1", True, WHITE)
    map1Location = map1Text.get_rect(center = (map1DisplayX + mapDisplayWidth//2, mapDisplayY - 20))
    map2Text = mapTextFont.render("Map 2", True, WHITE)
    map2Location = map2Text.get_rect(center = (map2DisplayX + mapDisplayWidth//2, mapDisplayY - 20))
    map3Text = mapTextFont.render("Map 3", True, WHITE)
    map3Location = map3Text.get_rect(center = (map3DisplayX + mapDisplayWidth//2, mapDisplayY - 20))
    map4Text = mapTextFont.render("Map 4", True, WHITE)
    map4Location = map4Text.get_rect(center = (map4DisplayX + mapDisplayWidth//2, mapDisplayY - 20))
    map5Text = mapTextFont.render("Map 5", True, WHITE)
    map5Location = map5Text.get_rect(center = (map5DisplayX + mapDisplayWidth//2, mapDisplayY - 20))

    #draw boxes & display maps
    pygame.draw.rect(gameWindow, BLACK, (20, 20, 1160, 560), False, 3)            #black box background
    pygame.draw.rect(gameWindow, DARKRED, (20, 20 , 1160, 560), 4, 3)           #red outline of the black box
    gameWindow.blit(chooseMap, chooseMapLocation)

    gameWindow.blit(selectionBackground1Display, (map1DisplayX, mapDisplayY))
    pygame.draw.rect(gameWindow, DARKRED, (map1DisplayX, mapDisplayY, mapDisplayWidth, 100), 3)
    gameWindow.blit(map1Text, map1Location) 

    gameWindow.blit(selectionBackground2Display, (map2DisplayX, mapDisplayY))
    pygame.draw.rect(gameWindow, DARKRED, (map2DisplayX, mapDisplayY, mapDisplayWidth, 100), 3)
    gameWindow.blit(map2Text, map2Location)

    gameWindow.blit(selectionBackground3Display, (map3DisplayX, mapDisplayY))
    pygame.draw.rect(gameWindow, DARKRED, (map3DisplayX, mapDisplayY, mapDisplayWidth, 100), 3)
    gameWindow.blit(map3Text, map3Location)

    gameWindow.blit(selectionBackground4Display, (map4DisplayX, mapDisplayY))
    pygame.draw.rect(gameWindow, DARKRED, (map4DisplayX, mapDisplayY, mapDisplayWidth, 100), 3)
    gameWindow.blit(map4Text, map4Location)

    gameWindow.blit(selectionBackground5Display, (map5DisplayX, mapDisplayY))
    pygame.draw.rect(gameWindow, DARKRED, (map5DisplayX, mapDisplayY, mapDisplayWidth, 100), 3)
    gameWindow.blit(map5Text, map5Location)

    #map selection arrow
    pygame.draw.polygon(gameWindow, WHITE, ((mapSelectionArrowX[selectedMap] - 20, mapselectionArrowY), (mapSelectionArrowX[selectedMap] + 20, mapselectionArrowY), (mapSelectionArrowX[selectedMap], mapselectionArrowY - 15)) )

    #display chosen map text
    chosenMap = selectedMapFont.render(f"Selected: Map {selectedMap}", True, WHITE)
    noChosenMap = selectedMapFont.render(f"Selected: None", True, WHITE)
    chosenMapLocation = chosenMap.get_rect(center = (WIDTH//2, 465))

    if selectedMap > 0:
        gameWindow.blit(chosenMap, chosenMapLocation)
    else: 
        gameWindow.blit(noChosenMap, chosenMapLocation)



def displayCharacterSelectionMenu(player):

    global characterSelectionP1ArrowX
    global characterSelectionP2ArrowX
    global characterSelectionP1ArrowY
    global characterSelectionP2ArrowY
    global player1Character
    global player2Character
    global takenCharacterDisplayX
    global takenCharacterDisplayY

    gameWindow.blit(menuBackground[0], ORIGIN)

    pygame.draw.rect(gameWindow, BLACK, (20, 20, 700, 560), False, 6)            
    pygame.draw.rect(gameWindow, DARKRED, (20, 20 , 700, 560), 4, 6) 

    pygame.draw.rect(gameWindow, BLACK, (740, 20, 440, 560), False, 6)            
    pygame.draw.rect(gameWindow, DARKRED, (740, 20, 440, 560), 4, 6) 

    #if its first player's turn
    if player == 1:
        player1SelectText =  selectCharacterFont.render('Choose your character: (P1)', True, WHITE)
        gameWindow.blit(player1SelectText, (140, 75))
        
        #showing controls for player
        P1ControlText = controlFont.render('Player 1 Controls:', True, WHITE)
        P1ControlTextLocation = P1ControlText.get_rect(center = (960, 437))
        gameWindow.blit(P1ControlText, P1ControlTextLocation)

        P1KeysJump = controlKeysFont.render('Jump: W', True, WHITE)
        gameWindow.blit(P1KeysJump, (835, 478))

        P1KeysRun = controlKeysFont.render('Run: A, D', True, WHITE)
        gameWindow.blit(P1KeysRun, (835, 500))

        P1KeysAtk1 = controlKeysFont.render('Attack 1: E', True, WHITE)
        gameWindow.blit(P1KeysAtk1, (975, 478))

        P1KeysAtk2 = controlKeysFont.render('Attack 2: R', True, WHITE)
        gameWindow.blit(P1KeysAtk2, (975, 500))

        player1CharacterNameText = playerCharacterNameTextFont.render(f'{characterNames[player1Character]}', True, WHITE)
        player1CharacterNameLocation = player1CharacterNameText.get_rect(center = (960, 95))
        gameWindow.blit(player1CharacterNameText, player1CharacterNameLocation)

        #if player chosen these characters, selection arrow y will be adjusted
        if player1Character == 1 or player1Character == 2:
            characterSelectionP1ArrowY = character1SelectionPictureY + PORTRAIT_HEIGHT + 25
    
        elif player1Character == 3 or player1Character == 4:
            characterSelectionP1ArrowY = character3SelectionPictureY + PORTRAIT_HEIGHT + 25

        else:
            characterSelectionP1ArrowY = 0

        pygame.draw.polygon(gameWindow, WHITE, ((characterSelectionP1ArrowX[player1Character] - 20, characterSelectionP1ArrowY), (characterSelectionP1ArrowX[player1Character] + 20, characterSelectionP1ArrowY), (characterSelectionP1ArrowX[player1Character], characterSelectionP1ArrowY - 15)))

    #if it's second player's turn
    elif player == 2:
        player2SelectText =  selectCharacterFont.render('Choose your character: (P2)', True, WHITE)
        gameWindow.blit(player2SelectText, (140, 75))

        #display controls
        P2ControlText = controlFont.render('Player 2 Controls:', True, WHITE)
        P2ControlTextLocation = P2ControlText.get_rect(center = (960, 437))
        gameWindow.blit(P2ControlText, P2ControlTextLocation)

        P2KeysJump = controlKeysFont.render('Jump: I', True, WHITE)
        gameWindow.blit(P2KeysJump, (835, 478))

        P2KeysRun = controlKeysFont.render('Run: J, L', True, WHITE)
        gameWindow.blit(P2KeysRun, (835, 500))

        P2KeysAtk1 = controlKeysFont.render('Attack 1: O', True, WHITE)
        gameWindow.blit(P2KeysAtk1, (975, 478))

        P2KeysAtk2 = controlKeysFont.render('Attack 2: P', True, WHITE)
        gameWindow.blit(P2KeysAtk2, (975, 500))

        player2CharacterNameText = playerCharacterNameTextFont.render(f'{characterNames[player2Character]}', True, WHITE)
        player2CharacterNameLocation = player2CharacterNameText.get_rect(center = (960, 95))
        gameWindow.blit(player2CharacterNameText, player2CharacterNameLocation)

        #adjust selection arrow Y coordinates
        if player2Character == 1 or player2Character == 2:
            characterSelectionP2ArrowY = character1SelectionPictureY + PORTRAIT_HEIGHT + 25
    
        elif player2Character == 3 or player2Character == 4:
            characterSelectionP2ArrowY = character3SelectionPictureY + PORTRAIT_HEIGHT + 25

        else:
            characterSelectionP2ArrowY = 0

        pygame.draw.polygon(gameWindow, WHITE, ((characterSelectionP2ArrowX[player2Character] - 20, characterSelectionP2ArrowY), (characterSelectionP2ArrowX[player2Character] + 20, characterSelectionP2ArrowY), (characterSelectionP2ArrowX[player2Character], characterSelectionP2ArrowY - 15)))
    
    #show characters and draw a box around their pfp
    gameWindow.blit(character1SelectionPicture, (character1SelectionPictureX, character1SelectionPictureY))
    pygame.draw.rect(gameWindow, DARKRED, (character1SelectionPictureX, character1SelectionPictureY, PORTRAIT_WIDTH, PORTRAIT_HEIGHT), 4)

    gameWindow.blit(character2SelectionPicture, (character2SelectionPictureX, character2SelectionPictureY))
    pygame.draw.rect(gameWindow, DARKRED, (character2SelectionPictureX, character2SelectionPictureY, PORTRAIT_WIDTH, PORTRAIT_HEIGHT), 4)

    gameWindow.blit(character3SelectionPicture, (character3SelectionPictureX, character3SelectionPictureY))
    pygame.draw.rect(gameWindow, DARKRED, (character3SelectionPictureX, character3SelectionPictureY, PORTRAIT_WIDTH, PORTRAIT_HEIGHT), 4)    

    gameWindow.blit(character4SelectionPicture, (character4SelectionPictureX, character4SelectionPictureY))
    pygame.draw.rect(gameWindow, DARKRED, (character4SelectionPictureX, character4SelectionPictureY, PORTRAIT_WIDTH, PORTRAIT_HEIGHT), 4)

    #if player is 2, they have a restriction from choosing p1's character
    if player == 2:
        takenCharacterDisplayX = characterDisplayXList[player1Character - 1]
        takenCharacterDisplayY = characterDisplayYList[player1Character - 1]
        pygame.draw.rect(gameWindow, DARKRED, (takenCharacterDisplayX, takenCharacterDisplayY, PORTRAIT_WIDTH, PORTRAIT_HEIGHT))
        takenCharacterText1 = takenCharacterTextFont.render('Taken', True, WHITE)
        takenCharacterText2 = takenCharacterTextFont.render('By P1', True, WHITE)
        takenCharacterTextLocation1 = takenCharacterText1.get_rect(center = (takenCharacterDisplayX + PORTRAIT_WIDTH//2, takenCharacterDisplayY + PORTRAIT_HEIGHT//2 - 15))
        takenCharacterTextLocation2 = takenCharacterText2.get_rect(center = (takenCharacterDisplayX + PORTRAIT_WIDTH//2, takenCharacterDisplayY + PORTRAIT_HEIGHT//2 + 15))
        gameWindow.blit(takenCharacterText1, takenCharacterTextLocation1)
        gameWindow.blit(takenCharacterText2, takenCharacterTextLocation2)



#showcases their selected character on the side
def displaySelectedCharacter(player):

    global selectedCharacterReferenceTime
    global frame

    #chooses their selected character from the list
    if player == 1:
        temp_list = displayCharacterList[player1Character - 1]
    if player == 2:
        temp_list = displayCharacterList[player2Character - 1]

    #same animation process as menu background function
    updateSpeed = 150
    timeCharacter = pygame.time.get_ticks()

    if timeCharacter - selectedCharacterReferenceTime > updateSpeed:
        selectedCharacterReferenceTime = timeCharacter
        frame += 1

    if frame >= len(temp_list[0]) - 1:
        frame = 0

    gameWindow.blit(temp_list[0][frame], (513, -60))



#back and forward button in the gui
def back_forward_button():

    pygame.draw.polygon(gameWindow, WHITE, ((backButtonX, buttonY), (backButtonX, buttonY + buttonH), (backButtonX - buttonW, buttonY + buttonH//2)))     #back
    pygame.draw.polygon(gameWindow, WHITE, ((forwardButtonX, buttonY), (forwardButtonX, buttonY + buttonH), (forwardButtonX + buttonW, buttonY + buttonH//2)))      #forward



#display map background in fighting windows
def displayBackground():

    global map
    global selectedMap
    global gameBackgroundTime
    global mapFrame

    updateSpeed = 150

    timeBG = pygame.time.get_ticks()
    if timeBG - gameBackgroundTime > updateSpeed:
        gameBackgroundTime = timeBG
        mapFrame += 1

    if mapFrame >= len(background1):
        mapFrame = 0
        
    gameWindow.blit(map[mapFrame], (0,0))



#load in map info, such as selected map and ground level
def loadMap():

    global GROUND_LEVEL
    global map

    GROUND_LEVEL = mapGroundLevel[selectedMap]
    map = mapPool[selectedMap]



#load in every attribute of player 1's character
def loadPlayer1():

    global player1_PFP
    global player1_ANIMATIONLIST_LEFT
    global player1_ANIMATIONLIST_RIGHT
    global player1_hitbox_width
    global player1_hitbox_height
    global player1_atk1_width
    global player1_atk1_height
    global player1_atk1_hitframe
    global player1_atk1_y_shift
    global player1_atk1_damage
    global player1_atk1_cooldown
    global player1_atk1_cooldown
    global player1_atk2_width
    global player1_atk2_height
    global player1_atk2_hitframe
    global player1_atk2_y_shift
    global player1_atk2_damage
    global player1_atk2_cooldown
    global player1_atk2_cooldown

    player1_PFP = pfp[player1Character]
    player1_ANIMATIONLIST_LEFT = animationlist_left[player1Character]
    player1_ANIMATIONLIST_RIGHT = animationlist_right[player1Character]
    player1_hitbox_width = hitbox_width[player1Character]
    player1_hitbox_height = hitbox_height[player1Character]
    player1_atk1_width = atk1_width[player1Character]
    player1_atk1_height = atk1_height[player1Character]
    player1_atk1_hitframe = atk1_hitframe[player1Character]
    player1_atk1_y_shift = atk1_y_shift[player1Character]
    player1_atk1_damage = atk1_damage[player1Character]
    player1_atk1_cooldown = atk1_cooldown[player1Character]
    player1_atk2_width = atk2_width[player1Character]
    player1_atk2_height = atk2_height[player1Character]
    player1_atk2_hitframe = atk2_hitframe[player1Character]
    player1_atk2_y_shift = atk2_y_shift[player1Character]
    player1_atk2_damage = atk2_damage[player1Character]
    player1_atk2_cooldown = atk2_cooldown[player1Character]



#loads every attribute of player 2's character to avoid loading in actual fighting loop
def loadPlayer2():

    global player2_PFP
    global player2_ANIMATIONLIST_LEFT
    global player2_ANIMATIONLIST_RIGHT
    global player2_hitbox_width
    global player2_hitbox_height
    global player2_atk1_width
    global player2_atk1_height
    global player2_atk1_hitframe
    global player2_atk1_y_shift
    global player2_atk1_damage
    global player2_atk1_cooldown
    global player2_atk1_cooldown
    global player2_atk2_width
    global player2_atk2_height
    global player2_atk2_hitframe
    global player2_atk2_y_shift
    global player2_atk2_damage
    global player2_atk2_cooldown
    global player2_atk2_cooldown

    player2_PFP = pfp[player2Character]
    player2_ANIMATIONLIST_LEFT = animationlist_left[player2Character]
    player2_ANIMATIONLIST_RIGHT = animationlist_right[player2Character]
    player2_hitbox_width = hitbox_width[player2Character]
    player2_hitbox_height = hitbox_height[player2Character]
    player2_atk1_width = atk1_width[player2Character]
    player2_atk1_height = atk1_height[player2Character]
    player2_atk1_hitframe = atk1_hitframe[player2Character]
    player2_atk1_y_shift = atk1_y_shift[player2Character]
    player2_atk1_damage = atk1_damage[player2Character]
    player2_atk1_cooldown = atk1_cooldown[player2Character]
    player2_atk2_width = atk2_width[player2Character]
    player2_atk2_height = atk2_height[player2Character]
    player2_atk2_hitframe = atk2_hitframe[player2Character]
    player2_atk2_y_shift = atk2_y_shift[player2Character]
    player2_atk2_damage = atk2_damage[player2Character]
    player2_atk2_cooldown = atk2_cooldown[player2Character]



def p1Animation():

    global frameP1
    global actionP1
    global animationTimeP1
    global player1_atk1_animation
    global player1_atk2_animation
    global player1_takehit_animation
    global player1_death_animation
    global stopAnimationP1
    global deathAnimationOver

    cooldown = 80
    timeP1 = pygame.time.get_ticks()

    #player 1 death animation
    if player1_death_animation:
        update_statusP1(7)
        if frameP1 >= len(player1_ANIMATIONLIST_LEFT[actionP1]) - 1:
            frameP1 = len(player1_ANIMATIONLIST_LEFT[actionP1]) - 1
            stopAnimationP1 = True
            deathAnimationOver = True
        

    #player 1 take hit animation
    if player1_takehit_animation and player1_alive:
        update_statusP1(6)
        if frameP1 >= len(player1_ANIMATIONLIST_LEFT[actionP1]) - 1:
            actionP1 = 0
            frameP1 = 0
            player1_takehit_animation = False
    else: 
        player1_takehit_animation = False

    #idle
    if dx1 == 0 and not player1_atk1_animation and not player1_atk2_animation and not player1_takehit_animation and not player1_death_animation:
        update_statusP1(0)

    #jump up
    if dy1 < 0:
        cooldown = 150
        update_statusP1(2)

    #jump down
    if dy1 > 0:
        cooldown = 100
        update_statusP1(3)


    #slow down animation
    if timeP1 - animationTimeP1 > cooldown and not stopAnimationP1:
        animationTimeP1 = timeP1
        frameP1 += 1

    #checks the length of the animation and returns to it
    if frameP1 >= len(player1_ANIMATIONLIST_LEFT[actionP1]) and actionP1 != 7:
        frameP1 = 0
        

    #player1 atk animation
    if player1_atk1_animation and dx1 == 0:
        update_statusP1(4)
        if frameP1 >= len(player1_ANIMATIONLIST_LEFT[actionP1]) - 1:
            actionP1 = 0
            frameP1 = 0
            player1_atk1_animation = False
    else: 
        player1_atk1_animation = False   #keeps var false


    if player1_atk2_animation and dx1 == 0:
        update_statusP1(5)
        if frameP1 >= len(player1_ANIMATIONLIST_LEFT[actionP1]) - 1:
            actionP1 = 0
            frameP1 = 0
            player1_atk2_animation = False
    else:
        player1_atk2_animation = False



def update_statusP1(action):

    global frameP1
    global actionP1
    global timeP1

    #update action index it doesnt match with parameter
    if actionP1 != action:
        actionP1 = action
        frameP1 = 0
        timeP1 = pygame.time.get_ticks()   #reset frame timer



def p2Animation():

    global frameP2
    global actionP2
    global animationTimeP2
    global player2_atk1_animation
    global player2_atk2_animation
    global player2_takehit_animation
    global player2_death_animation
    global stopAnimationP2
    global deathAnimationOver

    cooldown = 80
    timeP2 = pygame.time.get_ticks()

    #player 2 death animation
    if player2_death_animation:
        update_statusP2(7)
        if frameP2 >= len(player2_ANIMATIONLIST_LEFT[actionP2]) - 1:
            frameP2 = len(player2_ANIMATIONLIST_LEFT[actionP2]) - 1
            stopAnimationP2 = True
            deathAnimationOver = True
    

    #player 2 take hit animation
    if player2_takehit_animation and player2_alive:
        update_statusP2(6)
        if frameP2 >= len(player2_ANIMATIONLIST_LEFT[actionP2]) - 1:
            actionP2 = 0
            frameP2 = 0
            player2_takehit_animation = False
    else: 
        player2_takehit_animation = False


    #idle 
    if dx2 == 0 and not player2_atk1_animation and not player2_atk2_animation and not player2_takehit_animation and not player2_death_animation:
        update_statusP2(0)

    #jumping up
    if dy2 < 0:
        cooldown = 150
        update_statusP2(2)

    #jumping down
    if dy2 > 0:
        cooldown = 100
        update_statusP2(3)


    #slow down animation
    if timeP2 - animationTimeP2 > cooldown and not stopAnimationP2:
        animationTimeP2 = timeP2
        frameP2 += 1

    #resets frames if it reaches last frame of the animation
    if frameP2 >= len(player2_ANIMATIONLIST_LEFT[actionP2]) and actionP2 != 7:
        frameP2 = 0

    #atk1 animation
    if player2_atk1_animation and dx2 == 0:
        update_statusP2(4)
        if frameP2 >= len(player2_ANIMATIONLIST_LEFT[actionP2]) - 1:   #ensures playing the full animation and stops
            actionP2 = 0
            frameP2 = 0 
            player2_atk1_animation = False
    else: 
        player2_atk1_animation = False        #maintain false so player doesnt keep attacking

    
    if player2_atk2_animation and dx2 == 0:
        update_statusP2(5)

        if frameP2 == len(player2_ANIMATIONLIST_LEFT[actionP2]) - 1:
            actionP2 = 0
            frameP2 = 0
            player2_atk2_animation = False
    else:
        player2_atk2_animation = False



def update_statusP2(action):

    global frameP2
    global actionP2
    global timeP2

    #update the actionP# if it does not match the parameter
    if actionP2 != action:
        actionP2 = action
        frameP2 = 0
        timeP2 = pygame.time.get_ticks()     #retimes the animation cooldown



def p1GUI():

    global player1_alive
    global cdBar1P1
    global cdBar2P1
    global player1_attacked_atk1
    global player1_attacked_atk2
    global lastAtk2TimeP1
    global player1_death_animation

    player1NameText = nameTextFont.render("Player 1", True, BLACK)

    player1HealthPercentage = player1Health / MAX_HEALTH
    player1HealthWidth = ''

    if player1Health >= 0:
        player1HealthWidth = healthWidth * player1HealthPercentage
    else: 
        player1HealthWidth = 0


    #COOLDOWN BAR 1
    if cdBar1P1 < fullcdBar1Width:
        cdBar1P1 = fullcdBar1Width * (atk1TimeCounter - lastAtk1TimeP1)/player1_atk1_cooldown

    #caps it from lagging and going outside of black box
    elif cdBar1P1 >= fullcdBar1Width:
        cdBar1P1 = fullcdBar1Width

    #reduce by 8 so that hitbox doesnt get skipped most of the time when holding down
    if cdBar1P1 >= fullcdBar1Width - 8:
        player1_attacked_atk1 = False


    #COOLDOWN BAR 2
    if cdBar2P1 < fullcdBar2Width:
        cdBar2P1 = fullcdBar2Width * (atk2TimeCounter - lastAtk2TimeP1)/player1_atk2_cooldown
    
    elif cdBar2P1 >= fullcdBar2Width:
        cdBar2P1 = fullcdBar2Width

    if cdBar2P1 >= fullcdBar2Width - 8:
        player1_attacked_atk2 = False

    #draw pfp, cdbox, hp box, etc
    pygame.draw.rect(gameWindow, BAR, (pfpBox1X, pfpBoxY, pfpBoxWidth, pfpBoxHeight), False)
    gameWindow.blit(player1_PFP, (pfpBox1X + 4, pfpBoxY + 4, pfpBoxWidth - 4*2, pfpBoxHeight - 4*2))
    pygame.draw.rect(gameWindow, BLACK, (pfpBox1X + 4, pfpBoxY + 4, pfpBoxWidth - 4*2, pfpBoxHeight - 4*2), 2)
    
    pygame.draw.rect(gameWindow, BAR, (nameBar1X, nameBarY, nameBarWidth, NameBarHeight), False, 5)
    gameWindow.blit(player1NameText, (nameBar1X + 10, nameBarY))

    pygame.draw.rect(gameWindow, BAR, (health1BarX, healthBarY, healthBarWidth, healthBarHeight), False, 5)
    pygame.draw.rect(gameWindow, RED, (health1BarX + 5, healthBarY + 5, player1HealthWidth, healthBarHeight - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (health1BarX + 5, healthBarY + 5, healthBarWidth - 5*2, healthBarHeight - 5*2), 2, 4)

    pygame.draw.rect(gameWindow, BAR, (cdBar1P1X, cdBar1Y, cdBar1Width, cdBar1Height), False, 5)
    pygame.draw.rect(gameWindow, CDBLUE, (cdBar1P1X + 5, cdBar1Y + 5, cdBar1P1, cdBar1Height - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (cdBar1P1X + 5, cdBar1Y + 5, cdBar1Width - 5*2, cdBar1Height - 5*2), 2, 4)

    pygame.draw.rect(gameWindow, BAR, (cdBar2P1X, cdBar2Y, cdBar2Width, cdBar2Height), False, 5)
    pygame.draw.rect(gameWindow, YELLOW, (cdBar2P1X + 5, cdBar2Y + 5, cdBar2P1, cdBar2Height - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (cdBar2P1X + 5, cdBar2Y + 5, cdBar2Width - 5*2, cdBar2Height - 5*2), 2, 4)



def p2GUI():

    global player2_alive
    global cdBar1P2
    global cdBar2P2
    global player2_attacked_atk1
    global player2_attacked_atk2
    global lastATk2TimeP2
    global player2_death_animation

    player2NameText = nameTextFont.render("Player 2", True, BLACK)

    player2HealthPercentage = player2Health / MAX_HEALTH
    player2HealthWidth = ''

    if player2Health >= 0:
        player2HealthWidth = healthWidth * player2HealthPercentage
    else: 
        player2HealthWidth = 0


    #COOLDOWN BAR 1
    if cdBar1P2 < fullcdBar1Width:
        cdBar1P2 = fullcdBar1Width * (atk1TimeCounter - lastAtk1TimeP2)/player2_atk1_cooldown

    #caps it from lagging and going outside of black box
    elif cdBar1P2 >= fullcdBar1Width:
        cdBar1P2 = fullcdBar1Width

    #reduce by 8 so that hitbox doesnt get skipped most of the time when holding down
    if cdBar1P2 >= fullcdBar1Width - 8:
        player2_attacked_atk1 = False

    
    #COOLDOWN BAR 2
    if cdBar2P2 < fullcdBar2Width:
        cdBar2P2 = fullcdBar2Width * (atk2TimeCounter - lastATk2TimeP2)/player2_atk2_cooldown
    
    elif cdBar2P2 >= fullcdBar2Width:
        cdBar2P2 = fullcdBar2Width

    if cdBar2P2 >= fullcdBar2Width - 8:
        player2_attacked_atk2 = False

    #draw everything, name bar, pfp, cdbar, etc
    pygame.draw.rect(gameWindow, BAR, (pfpBox2X, pfpBoxY, pfpBoxWidth, pfpBoxHeight), False)
    gameWindow.blit(player2_PFP, (pfpBox2X + 4, pfpBoxY + 4, pfpBoxWidth - 4*2, pfpBoxHeight - 4*2))
    pygame.draw.rect(gameWindow, BLACK, (pfpBox2X + 4, pfpBoxY + 4, pfpBoxWidth - 4*2, pfpBoxHeight - 4*2), 2)

    pygame.draw.rect(gameWindow, BAR, (nameBar2X, nameBarY, nameBarWidth, NameBarHeight), False, 5)
    gameWindow.blit(player2NameText, (nameBar2X + 10, nameBarY))

    pygame.draw.rect(gameWindow, BAR, (health2BarX, healthBarY, healthBarWidth, healthBarHeight), False, 5)
    pygame.draw.rect(gameWindow, RED, (health2BarX + 5, healthBarY + 5, player2HealthWidth, healthBarHeight - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (health2BarX + 5, healthBarY + 5, healthBarWidth - 5*2, healthBarHeight - 5*2), 2, 4)

    pygame.draw.rect(gameWindow, BAR, (cdBar1P2X, cdBar1Y, cdBar1Width, cdBar1Height), False, 5)
    pygame.draw.rect(gameWindow, CDBLUE, (cdBar1P2X + 5, cdBar1Y + 5, cdBar1P2, cdBar1Height - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (cdBar1P2X + 5, cdBar1Y + 5, cdBar1Width - 5*2, cdBar1Height - 5*2), 2, 4)

    pygame.draw.rect(gameWindow, BAR, (cdBar2P2X, cdBar2Y, cdBar2Width, cdBar2Height), False, 5)
    pygame.draw.rect(gameWindow, YELLOW, (cdBar2P2X + 5, cdBar2Y + 5, cdBar2P2, cdBar2Height - 5*2), False, 4)
    pygame.draw.rect(gameWindow, BLACK, (cdBar2P2X + 5, cdBar2Y + 5, cdBar2Width - 5*2, cdBar2Height - 5*2), 2, 4)



def playerHit():

    global player2Health
    global player1Health
    global player1_takehit_animation
    global player2_takehit_animation
    global player1_death_animation
    global player2_death_animation
    global player1_alive
    global player2_alive

    #takes away hp from player after being hit
    if player1Atk1.colliderect(player2Hitbox):
        player2Health -= player1_atk1_damage
        player2_takehit_animation = True
        if player2Health <= 0:            #checks if player has died to the hit
            player2_death_animation = True
            player2_alive = False

    if player2Atk1.colliderect(player1Hitbox):
        player1Health -= player2_atk1_damage
        player1_takehit_animation = True
        if player1Health <= 0:
            player1_death_animation = True
            player1_alive = False

    if player1Atk2.colliderect(player2Hitbox):
        player2Health -= player1_atk2_damage
        player2_takehit_animation = True
        if player2Health <= 0:
            player2_death_animation = True
            player2_alive = False

    if player2Atk2.colliderect(player1Hitbox):
        player1Health -= player2_atk2_damage
        player1_takehit_animation = True
        if player1Health <= 0:
            player1_death_animation = True
            player1_alive = False
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
#-----------------------------------------MAIN PROGRAM--------------------------------------#
#-------------------------------------------------------------------------------------------#

inPlay = True
menu = True
mapSelection = False
characterSelectionP1 = False
characterSelectionP2 = False
countdown = False
fight = False

print("Hold ESC to Exit Game Window.")

menuBackgroundMusic.play(-1)
while inPlay: 

    while menu:
        pygame.event.clear()
        closeGame()
        displayMenuBackground()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:         #if space is pressed, go to next menu
                    menu = False
                    mapSelection = True

        pygame.display.update()

        

    while mapSelection:
        closeGame()
        displayMapSelectionMenu()
        back_forward_button()
        
        #get the x,y coord of the mouse and lets player choose map 1-5
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:         #map selections
                if (map1DisplayX < mouseX < map1DisplayX + mapDisplayWidth) and (mapDisplayY < mouseY < mapDisplayY + 100):
                    pygame.mixer.Channel(1).play(selectionSound)
                    selectedMap = 1

                if (map2DisplayX < mouseX < map2DisplayX + mapDisplayWidth) and (mapDisplayY < mouseY < mapDisplayY + 100):
                    pygame.mixer.Channel(1).play(selectionSound)
                    selectedMap = 2

                if (map3DisplayX < mouseX < map3DisplayX + mapDisplayWidth) and (mapDisplayY < mouseY < mapDisplayY + 100):
                    pygame.mixer.Channel(1).play(selectionSound)
                    selectedMap = 3

                if (map4DisplayX < mouseX < map4DisplayX + mapDisplayWidth) and (mapDisplayY < mouseY < mapDisplayY + 100):
                    pygame.mixer.Channel(1).play(selectionSound)
                    selectedMap = 4

                if (map5DisplayX < mouseX < map5DisplayX + mapDisplayWidth) and (mapDisplayY < mouseY < mapDisplayY + 100):
                    pygame.mixer.Channel(1).play(selectionSound)
                    selectedMap = 5
                
                #back and forward button areas
                if (forwardButtonX  < mouseX < forwardButtonX + buttonW) and (buttonY < mouseY < buttonY + buttonH) and selectedMap != 0:
                    pygame.mixer.Channel(1). play(buttonClick)
                    mapSelection = False
                    characterSelectionP1 = True

                if (backButtonX - buttonW < mouseX < backButtonX) and (buttonY < mouseY < buttonY + buttonH):
                    pygame.mixer.Channel(1). play(buttonClick)
                    mapSelection = False
                    menu = True
            
            loadMap()

        pygame.display.update()



    while characterSelectionP1:

        pygame.event.clear()
        closeGame()

        #draw gui
        displayCharacterSelectionMenu(1)
        back_forward_button()

        #if something is selected, play the selected character idle animation
        if player1Character != 0:
            displaySelectedCharacter(1)

        #lets player choose their character
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (character1SelectionPictureX <= mouseX <= character1SelectionPictureX + PORTRAIT_WIDTH) and (character1SelectionPictureY <= mouseY <= character1SelectionPictureY + PORTRAIT_HEIGHT):
                    pygame.mixer.Channel(2).play(selectionSound)
                    player1Character = 1

                if (character2SelectionPictureX <= mouseX <= character2SelectionPictureX + PORTRAIT_WIDTH) and (character2SelectionPictureY <= mouseY <= character2SelectionPictureY + PORTRAIT_HEIGHT):
                    pygame.mixer.Channel(2).play(selectionSound)
                    player1Character = 2

                if (character3SelectionPictureX <= mouseX <= character3SelectionPictureX + PORTRAIT_WIDTH) and (character3SelectionPictureY <= mouseY <= character3SelectionPictureY + PORTRAIT_HEIGHT):
                    pygame.mixer.Channel(2).play(selectionSound)
                    player1Character = 3

                if (character4SelectionPictureX <= mouseX <= character4SelectionPictureX + PORTRAIT_WIDTH) and (character4SelectionPictureY <= mouseY <= character4SelectionPictureY + PORTRAIT_HEIGHT):
                    pygame.mixer.Channel(2).play(selectionSound)
                    player1Character = 4

                #back & forward button
                if (backButtonX - buttonW < mouseX < backButtonX) and (buttonY < mouseY < buttonY + buttonH):
                    pygame.mixer.Channel(2). play(buttonClick)
                    characterSelectionP1 = False
                    mapSelection = True

                if (forwardButtonX  < mouseX < forwardButtonX + buttonW) and (buttonY < mouseY < buttonY + buttonH) and player1Character != 0:
                    pygame.mixer.Channel(2). play(buttonClick)
                    characterSelectionP1 = False
                    characterSelectionP2 = True 
                        
        loadPlayer1()

        pygame.display.update()



    while characterSelectionP2:

        pygame.event.clear()
        closeGame()

        #display gui
        displayCharacterSelectionMenu(2)
        back_forward_button()
        
        #if something is selected, play the selected character idle animation
        if player2Character != 0:
            displaySelectedCharacter(2)

        #p1 selected character picture coords to prevent from selecting
        takenCharacterDisplayX = characterDisplayXList[player1Character - 1]
        takenCharacterDisplayY = characterDisplayYList[player1Character - 1]

        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (character1SelectionPictureX <= mouseX <= character1SelectionPictureX + PORTRAIT_WIDTH) and (character1SelectionPictureY <= mouseY <= character1SelectionPictureY +  PORTRAIT_HEIGHT):
                    #restriction for p2's character pool
                    if (character1SelectionPictureX != takenCharacterDisplayX) or (character1SelectionPictureY != takenCharacterDisplayY):
                        pygame.mixer.Channel(3).play(selectionSound)
                        player2Character = 1

                if (character2SelectionPictureX <= mouseX <= character2SelectionPictureX + PORTRAIT_WIDTH) and (character2SelectionPictureY <= mouseY <= character2SelectionPictureY +  PORTRAIT_HEIGHT):
                    if (character2SelectionPictureX != takenCharacterDisplayX) or (character2SelectionPictureY != takenCharacterDisplayY):
                        pygame.mixer.Channel(3).play(selectionSound)
                        player2Character = 2

                if (character3SelectionPictureX <= mouseX <= character3SelectionPictureX + PORTRAIT_WIDTH) and (character3SelectionPictureY <= mouseY <= character3SelectionPictureY +  PORTRAIT_HEIGHT):
                    if (character3SelectionPictureX != takenCharacterDisplayX) or (character3SelectionPictureY != takenCharacterDisplayY):
                        pygame.mixer.Channel(3).play(selectionSound)
                        player2Character = 3

                if (character4SelectionPictureX <= mouseX <= character4SelectionPictureX + PORTRAIT_WIDTH) and (character4SelectionPictureY <= mouseY <= character4SelectionPictureY +  PORTRAIT_HEIGHT):
                    if (character4SelectionPictureX != takenCharacterDisplayX) or (character4SelectionPictureY != takenCharacterDisplayY):
                        pygame.mixer.Channel(3).play(selectionSound)
                        player2Character = 4

                #back & forward buttons
                if (backButtonX - buttonW < mouseX < backButtonX) and (buttonY < mouseY < buttonY + buttonH):
                    pygame.mixer.Channel(3).play(buttonClick)
                    characterSelectionP1 = True
                    characterSelectionP2 = False
                    
                if (forwardButtonX  < mouseX < forwardButtonX + buttonW) and (buttonY < mouseY < buttonY + buttonH) and player2Character != 0 and player2Character != player1Character:
                    pygame.mixer.Channel(3).play(buttonClick)
                    countdown = True
                    characterSelectionP2 = False

        loadPlayer2()

        pygame.display.update()


    
    while countdown:

        closeGame()

        pygame.event.get()    #prevent from lagging out
        displayBackground()
        clock.tick(FPS)
        
        gameWindow.blit(solidBlack, (0, 100))

        tickSpeed = 1000
        timePassed = pygame.time.get_ticks()

        #if timer reaches 0, goes to fight window
        if second < 0:
            countdown = False
            fight = True

        #countdown system
        if timePassed - countdownStartTime >= tickSpeed:
            if second > 0:
                pygame.mixer.Channel(4).play(countdownSound)
            countdownStartTime = timePassed
            second -= 1
            timeText = second

            
        #changes last number in countdown to text 'fight'
        if second <= 0:
            timeText = 'FIGHT!'

        countdownText = countdownFont.render(f'{timeText}', True, WHITE)
        countdownTextLocation = countdownText.get_rect(center = (WIDTH//2, HEIGHT//2))

        player1Information = guiFont.render('Player 1 User Interface:', True, WHITE)
        player1Information1 = guiInformationFont.render(f'Healthbar: RED, HP: {player1Health}', True, WHITE)
        player1Information2 = guiInformationFont.render(f'Attack 1 Cooldown Bar: BLUE, COOLDOWN: {player1_atk1_cooldown//1000}s', True, WHITE)
        player1Information3 = guiInformationFont.render(f'Attack 2 Cooldown Bar: YELLOW, COOLDOWN: {player1_atk2_cooldown//1000}s', True, WHITE)

        player1InformationLocation = player1Information.get_rect(center = (WIDTH//4 - 40, 270))
        player1Information1Location = (90, 310)
        player1Information2Location = (90, 340)
        player1Information3Location = (90, 370)


        player2Information = guiFont.render('Player 2 User Interface:', True, WHITE)
        player2Information1 = guiInformationFont.render(f'Healthbar: RED, HP: {player2Health}', True, WHITE)
        player2Information2 = guiInformationFont.render(f'Attack 1 Cooldown Bar: BLUE, COOLDOWN: {player2_atk1_cooldown//1000}s', True, WHITE)
        player2Information3 = guiInformationFont.render(f'Attack 2 Cooldown Bar: YELLOW, COOLDOWN: {player2_atk2_cooldown//1000}s', True, WHITE)

        player2InformationLocation = player2Information.get_rect(center = (3*WIDTH//4 + 20, 270))
        player2Information1Location = (750, 310)
        player2Information2Location = (750, 340)
        player2Information3Location = (750, 370)

        gameWindow.blit(countdownText, countdownTextLocation)
        gameWindow.blit(player1Information, player1InformationLocation)
        gameWindow.blit(player1Information1, player1Information1Location)
        gameWindow.blit(player1Information2, player1Information2Location)
        gameWindow.blit(player1Information3, player1Information3Location)
        gameWindow.blit(player2Information, player2InformationLocation)
        gameWindow.blit(player2Information1, player2Information1Location)
        gameWindow.blit(player2Information2, player2Information2Location)
        gameWindow.blit(player2Information3, player2Information3Location)


        pygame.display.update()



    while fight:

        displayBackground()

        clock.tick(FPS)
        pygame.event.clear()

        #define hitbox for future use
        player1Atk1 = pygame.Rect(0, 0, 0, 0)
        player2Atk1 = pygame.Rect(0, 0, 0, 0)
        player1Atk2 = pygame.Rect(0, 0, 0, 0)
        player2Atk2 = pygame.Rect(0, 0, 0, 0)

        #time since last attack
        atk1TimeCounter = pygame.time.get_ticks()
        atk2TimeCounter = pygame.time.get_ticks()
        
        #------------------------------------PLAYER CONTROLS-----------------------------------#

        #PLAYER 1

        #decide to use flipped list or not based on direction
        if player1Direction == 'right':
            player1Image = player1_ANIMATIONLIST_RIGHT[actionP1][frameP1]
        if player1Direction == 'left':
            player1Image = player1_ANIMATIONLIST_LEFT[actionP1][frameP1]

        gameWindow.blit(player1Image, (player1_x, player1_y))

        p1Animation()    #animate character

        #p1 hitbox variables
        player1_hitbox_x = player1_x + (playerW - player1_hitbox_width)//2
        player1_hitbox_y = player1_y + (playerH - player1_hitbox_height)

        #p1 atk1 variables
        player1_atk1_y = player1_hitbox_y + player1_atk1_y_shift
        player1_atk1_x_RIGHT = player1_hitbox_x + player1_hitbox_width
        player1_atk1_x_LEFT = player1_hitbox_x - player1_atk1_width

        #p1 atk2 variables
        player1_atk2_y = player1_hitbox_y + player1_atk2_y_shift

        #adjust hitbox location based on character attack areas
        if player1Character == 1:
            player1_atk2_x_RIGHT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2
            player1_atk2_x_LEFT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2
        elif player1Character == 4:
            player1_atk2_x_RIGHT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2 - 20
            player1_atk2_x_LEFT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2 + 20
        else:
            player1_atk2_x_LEFT = player1_hitbox_x - player1_atk2_width
            player1_atk2_x_RIGHT = player1_hitbox_x + player1_hitbox_width
        
        #define hitbox
        player1Hitbox = pygame.Rect(player1_hitbox_x, player1_hitbox_y, player1_hitbox_width, player1_hitbox_height)
        #player1HitboxVisual = pygame.draw.rect(gameWindow, RED, (player1_hitbox_x, player1_hitbox_y, player1_hitbox_width, player1_hitbox_height), 1)



        #PLAYER 2

        #decide to use flipped list or not based on direction
        if player2Direction == 'left':
            player2Image = player2_ANIMATIONLIST_LEFT[actionP2][frameP2]
        elif player2Direction == 'right':
            player2Image = player2_ANIMATIONLIST_RIGHT[actionP2][frameP2]

        gameWindow.blit(player2Image, (player2_x, player2_y))

        p2Animation()    #animate character
        
        #p2 hitbox variables
        player2_hitbox_x = player2_x + (playerW - player2_hitbox_width)//2
        player2_hitbox_y = player2_y + (playerH - player2_hitbox_height)

        #p2 atk1 variables
        player2_atk1_y = player2_hitbox_y + player2_atk1_y_shift
        player2_atk1_x_LEFT = player2_hitbox_x - player2_atk1_width
        player2_atk1_x_RIGHT = player2_hitbox_x + player2_hitbox_width

        #p2 atk2 variables
        player2_atk2_y = player2_hitbox_y + player2_atk2_y_shift

        #adjust hitbox location based on character attack areas
        if player2Character == 1:
            player2_atk2_x_LEFT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2
            player2_atk2_x_RIGHT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2
        elif player2Character == 4:
            player2_atk2_x_LEFT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2 - 20
            player2_atk2_x_RIGHT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2 + 20
        else:
            player2_atk2_x_LEFT = player2_hitbox_x - player2_atk2_width
            player2_atk2_x_RIGHT = player2_hitbox_x + player2_hitbox_width

        #define hitbox
        player2Hitbox = pygame.Rect(player2_hitbox_x, player2_hitbox_y, player2_hitbox_width, player2_hitbox_height)
        #player2HitboxVisual = pygame.draw.rect(gameWindow, RED, (player2_hitbox_x, player2_hitbox_y, player2_hitbox_width, player2_hitbox_height), 1)


        #boundaries

        #prevents player 1 from exiting map
        if player1_x < (LEFT - (playerW - player1_hitbox_width)//2):
            player1_x = (LEFT - (playerW - player1_hitbox_width)//2)

        if player1_x > (RIGHT - (playerW + player1_hitbox_width)//2):
            player1_x = (RIGHT - (playerW + player1_hitbox_width)//2)

        #prevents player 2 from exiting map
        if player2_x < (LEFT - (playerW - player1_hitbox_width)//2):
            player2_x = (LEFT - (playerW - player1_hitbox_width)//2)

        if player2_x > (RIGHT - (playerW + player2_hitbox_width)//2):
            player2_x = (RIGHT - (playerW + player2_hitbox_width)//2)
            


        #KEYS & CONTROLS
        keys = pygame.key.get_pressed()

        if not player1_takehit_animation and player1_alive and not countdown:

            #p1 controls
            if keys[pygame.K_d]:     #move to right
                if (player1_hitbox_y + player1_hitbox_height) == GROUND_LEVEL:
                    actionP1 = 1

                if player1Direction == "left":
                    player1Direction = "right"
                    frameP1 = 0
                    
                else:
                    dx1 = RUNNING_SPEED


            elif keys[pygame.K_a]:      #move to left
                if (player1_hitbox_y + player1_hitbox_height) == GROUND_LEVEL:
                    actionP1 = 1

                if player1Direction == "right":
                    player1Direction = "left"
                    frameP1 = 0

                else:
                    dx1 = -RUNNING_SPEED

            else:
                dx1 = 0
            

            if (player1_hitbox_y + player1_hitbox_height) == GROUND_LEVEL:

                if keys[pygame.K_w]:     #jump
                    dy1 = JUMP_SPEED

                #ATTACK 1
                if keys[pygame.K_e] and not player1_atk1_animation and not player1_atk2_animation and atk1TimeCounter - lastAtk1TimeP1 > player1_atk1_cooldown: 

                    player1_atk1_animation = True

                    lastAtk1TimeP1 = atk1TimeCounter
                    cdBar1P1 = 0

                if actionP1 == 4 and frameP1 == player1_atk1_hitframe and not player1_attacked_atk1:

                    player1_attacked_atk1 = True

                    if player1Direction == "right":
                        #player1Atk1Visual = pygame.draw.rect(gameWindow, GREEN, (player1_atk1_x_RIGHT, player1_atk1_y, player1_atk1_width, player1_atk1_height), 1)
                        player1Atk1 = pygame.Rect(player1_atk1_x_RIGHT, player1_atk1_y, player1_atk1_width, player1_atk1_height)
                                
                    elif player1Direction == "left":
                        #player1Atk1Visual = pygame.draw.rect(gameWindow, GREEN, (player1_atk1_x_LEFT, player1_atk1_y, player1_atk1_width, player1_atk1_height), 1)
                        player1Atk1 = pygame.Rect(player1_atk1_x_LEFT, player1_atk1_y, player1_atk1_width, player1_atk1_height)


                #ATTACK 2
                if keys[pygame.K_r] and not player1_atk2_animation and not player1_atk1_animation and atk2TimeCounter - lastAtk2TimeP1 > player1_atk2_cooldown:

                    player1_atk2_animation = True

                    lastAtk2TimeP1 = atk2TimeCounter
                    cdBar2P1 = 0
                
                if actionP1 == 5 and frameP1 == player1_atk2_hitframe and not player1_attacked_atk2:

                    player1_attacked_atk2 = True

                    if player1Direction == "right":
                        #player1Atk2Visual = pygame.draw.rect(gameWindow, GREEN, (player1_atk2_x_RIGHT, player1_atk2_y, player1_atk2_width, player1_atk2_height), 1)
                        player1Atk2 = pygame.Rect(player1_atk2_x_RIGHT, player1_atk2_y, player1_atk2_width, player1_atk2_height)
                                
                    elif player1Direction == "left":
                        #player1Atk2Visual = pygame.draw.rect(gameWindow, GREEN, (player1_atk2_x_LEFT, player1_atk2_y, player1_atk2_width, player1_atk2_height), 1)
                        player1Atk2 = pygame.Rect(player1_atk2_x_LEFT, player1_atk2_y, player1_atk2_width, player1_atk2_height)


        if not player2_takehit_animation and player2_alive and not countdown:
            
            #p2 controls
            if keys[pygame.K_l]:    #move right
                if (player2_hitbox_y + player2_hitbox_height) == GROUND_LEVEL:
                    actionP2 = 1

                if player2Direction == 'left':
                    player2Direction = "right"
                    frameP2 = 0

                else:
                    dx2 = RUNNING_SPEED


            elif keys[pygame.K_j]:   #move left
                if (player2_hitbox_y + player2_hitbox_height) == GROUND_LEVEL:
                    actionP2 = 1

                if player2Direction == 'right':
                    player2Direction = "left"
                    frameP2 = 0

                else:
                    dx2 = -RUNNING_SPEED
                    
            else:
                dx2 = 0

            if (player2_hitbox_y + player2_hitbox_height) == GROUND_LEVEL:

                if keys[pygame.K_i]:    #jump
                    dy2 = JUMP_SPEED

                #ATTACK 1
                if keys[pygame.K_o] and not player2_atk1_animation and not player2_atk2_animation and atk1TimeCounter - lastAtk1TimeP2 > player2_atk1_cooldown:
                    
                    player2_atk1_animation = True

                    lastAtk1TimeP2 = atk1TimeCounter
                    cdBar1P2 = 0

                if actionP2 == 4 and frameP2 == player2_atk1_hitframe and not player2_attacked_atk1:

                    player2_attacked_atk1 = True

                    if player2Direction == "left":
                        #player2Atk1Visual = pygame.draw.rect(gameWindow, GREEN, (player2_atk1_x_LEFT, player2_atk1_y, player2_atk1_width, player2_atk1_height), 1)
                        player2Atk1 = pygame.Rect(player2_atk1_x_LEFT, player2_atk1_y, player2_atk1_width, player2_atk1_height)

                    elif player2Direction == "right":
                        #player2Atk1Visual = pygame.draw.rect(gameWindow, GREEN, (player2_atk1_x_RIGHT, player2_atk1_y, player2_atk1_width, player2_atk1_height), 1)
                        player2Atk1 = pygame.Rect(player2_atk1_x_RIGHT, player2_atk1_y, player2_atk1_width, player2_atk1_height)
                

                #ATTACK 2
                if keys[pygame.K_p] and not player2_atk2_animation and not player2_atk1_animation and atk2TimeCounter - lastATk2TimeP2 > player2_atk2_cooldown:

                    player2_atk2_animation = True

                    lastATk2TimeP2 = atk2TimeCounter
                    cdBar2P2 = 0

                if actionP2 == 5 and frameP2 == player2_atk2_hitframe and not player2_attacked_atk2:

                    player2_attacked_atk2 = True

                    if player2Direction == "left":
                        #player2Atk2Visual = pygame.draw.rect(gameWindow, GREEN, (player2_atk2_x_LEFT, player2_atk2_y, player2_atk2_width, player2_atk2_height), 1)
                        player2Atk2 = pygame.Rect(player2_atk2_x_LEFT, player2_atk2_y, player2_atk2_width, player2_atk2_height)

                    elif player2Direction == "right":
                        #player2Atk2Visual = pygame.draw.rect(gameWindow, GREEN, (player2_atk2_x_RIGHT, player2_atk2_y, player2_atk2_width, player2_atk2_height), 1)
                        player2Atk2 = pygame.Rect(player2_atk2_x_RIGHT, player2_atk2_y, player2_atk2_width, player2_atk2_height)


        if keys[pygame.K_ESCAPE]:
            sys.exit()


        #MOVEMENTS

        #p1
        player1_x += dx1
        dy1 += GRAVITY
        player1_y += dy1

        if player1_y > GROUND_LEVEL - playerH:
            player1_y = GROUND_LEVEL - playerH
            dy1 = 0


        #p2
        player2_x += dx2
        dy2 += GRAVITY
        player2_y += dy2

        if player2_y > GROUND_LEVEL - playerH:
            player2_y = GROUND_LEVEL - playerH
            dy2 = 0

        #--------------------------------------------------------------------------------------#


        #--------------------------------------FEATURES----------------------------------------#
        #when colliderect
        playerHit()

        #player gui, including name bar, pfp, cooldown bars, hp bar
        p1GUI()
        p2GUI()
        #--------------------------------------------------------------------------------------#


        #------------------------------------GAMEOVER MENU-------------------------------------#
        if deathAnimationOver:          #if death animation finished playing

            tickSpeed = 1000
            closeTimePassed = pygame.time.get_ticks()

            #countdown to close
            if closeTimePassed - gameCloseTime > tickSpeed:     #updates every second
                gameCloseTime = closeTimePassed
                closeCountdownLength -= 1

            if closeCountdownLength <= 0:    #close the gamewindow when timer reaches 0
                inPlay = False
                sys.exit()

            gameOverText = gameOverTextFont.render('GAME OVER', True, WHITE)
            gameOverTextLocation = gameOverText.get_rect(center = (WIDTH//2, HEIGHT//2))

            gameCloseText = gameCloseTextFont.render(f'Game will auto close in {closeCountdownLength} seconds', True, WHITE)
            gameCloseTextLocation = gameCloseText.get_rect(center = (WIDTH//2, HEIGHT//2 + 50))

            gameWindow.blit(solidBlack, (0, 100))         #translucent image as background
            gameWindow.blit(gameOverText, gameOverTextLocation)
            gameWindow.blit(gameCloseText, gameCloseTextLocation)
        #--------------------------------------------------------------------------------------#

        pygame.display.update()