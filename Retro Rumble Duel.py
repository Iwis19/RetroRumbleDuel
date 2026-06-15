import pygame

pygame.init()

import sys
import os
from config import *

pygame.mixer.pre_init(44100, -16, 2, 0)
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Rumble Duel")

from screens.menu import Menu
from screens.mapselect import MapSelect
from screens.characterselect import CharacterSelect
from screens.countdown import Countdown
from screens.fight import Fight
from screens.gameover import GameOver
from helper.game_state import GameState

#CONSTANTS
FPS = 30

MAP1_GROUND_LEVEL = 500
MAP2_GROUND_LEVEL = 550
MAP3_GROUND_LEVEL = 565
MAP4_GROUND_LEVEL = 575
MAP5_GROUND_LEVEL = 553

JUMP_SPEED = -25
GRAVITY = 2
RUNNING_SPEED = 12
MAX_HEALTH = 100

#-------------------------------------------------------------------------------------------#


#----------------------------------LOADING CHARACTERS---------------------------------------#
character_names = ['None Selected', 'Fire Knight', 'Wind Hashashin', 'Water Priestess', 'Metal Bladekeeper']

#character 1
character1_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character1_ANIMATIONLIST_RIGHT = []
character1_ANIMATIONLIST_LEFT = []
character1ProfilePicture = pygame.transform.scale(pygame.image.load(asset_path("character1", "fire_knight.png")), PFP_DIMENSION).convert_alpha()
character1SelectionPicture = pygame.transform.scale(pygame.image.load(asset_path("character1", "fire_knight.png")), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character1_ACTIONS)):
    temp_list1_right = []
    temp_list1_left = []
    frames1 = len(os.listdir(asset_path("character1", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}")))
    for items in range (frames1):
        tile1right = pygame.transform.scale(pygame.image.load(asset_path("character1", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}", f"{character1_ACTIONS[animation]}_{items + 1}.png")), CHARACTER_DIMENSION).convert_alpha()
        tile1left = pygame.transform.flip(tile1right, True, False).convert_alpha()
        temp_list1_right.append(tile1right)
        temp_list1_left.append(tile1left)
    character1_ANIMATIONLIST_RIGHT.append(temp_list1_right)
    character1_ANIMATIONLIST_LEFT.append(temp_list1_left)


#character 2
character2_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character2_ANIMATIONLIST_RIGHT = []
character2_ANIMATIONLIST_LEFT = []
character2ProfilePicture = pygame.transform.scale(pygame.image.load(asset_path("character2", "wind_hashashin.png")), PFP_DIMENSION).convert_alpha()
character2SelectionPicture = pygame.transform.scale(pygame.image.load(asset_path("character2", "wind_hashashin.png")), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character2_ACTIONS)):
    temp_list2_right = []
    temp_list2_left = []
    frames2 = len(os.listdir(asset_path("character2", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}")))
    for items in range (frames2):
        tile2right = pygame.transform.scale(pygame.image.load(asset_path("character2", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}", f"{character1_ACTIONS[animation]}_{items + 1}.png")), CHARACTER_DIMENSION).convert_alpha()
        tile2left = pygame.transform.flip(tile2right, True, False).convert_alpha()
        temp_list2_right.append(tile2right)
        temp_list2_left.append(tile2left)
    character2_ANIMATIONLIST_RIGHT.append(temp_list2_right)
    character2_ANIMATIONLIST_LEFT.append(temp_list2_left)


#character 3
character3_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character3_ANIMATIONLIST_RIGHT = []
character3_ANIMATIONLIST_LEFT = []
character3ProfilePicture = pygame.transform.scale(pygame.image.load(asset_path("character3", "water_priestess.png")), PFP_DIMENSION).convert_alpha()
character3SelectionPicture = pygame.transform.scale(pygame.image.load(asset_path("character3", "water_priestess.png")), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character3_ACTIONS)):
    temp_list3_right = []
    temp_list3_left = []
    frames3 = len(os.listdir(asset_path("character3", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}")))
    for items in range (frames3):
        tile3right = pygame.transform.scale(pygame.image.load(asset_path("character3", "png", f"0{animation + 1}_{character3_ACTIONS[animation]}", f"{character3_ACTIONS[animation]}_{items + 1}.png")), CHARACTER_DIMENSION).convert_alpha()
        tile3left = pygame.transform.flip(tile3right, True, False).convert_alpha()
        temp_list3_right.append(tile3right)
        temp_list3_left.append(tile3left)
    character3_ANIMATIONLIST_RIGHT.append(temp_list3_right)
    character3_ANIMATIONLIST_LEFT.append(temp_list3_left)


#character 4
character4_ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]
character4_ANIMATIONLIST_RIGHT = []
character4_ANIMATIONLIST_LEFT = []
character4ProfilePicture = pygame.transform.scale(pygame.image.load(asset_path("character4", "metal_bladekeeper.png")), PFP_DIMENSION).convert_alpha()
character4SelectionPicture = pygame.transform.scale(pygame.image.load(asset_path("character4", "metal_bladekeeper.png")), PORTRAIT_DIMENSION).convert_alpha()

for animation in range(len(character4_ACTIONS)):
    temp_list4_right = []
    temp_list4_left = []
    frames4 = len(os.listdir(asset_path("character4", "png", f"0{animation + 1}_{character1_ACTIONS[animation]}")))
    for items in range (frames4):
        tile4right = pygame.transform.scale(pygame.image.load(asset_path("character4", "png", f"0{animation + 1}_{character4_ACTIONS[animation]}", f"{character4_ACTIONS[animation]}_{items + 1}.png")), CHARACTER_DIMENSION).convert_alpha()
        tile4left = pygame.transform.flip(tile4right, True, False).convert_alpha()
        temp_list4_right.append(tile4right)
        temp_list4_left.append(tile4left)
    character4_ANIMATIONLIST_RIGHT.append(temp_list4_right)
    character4_ANIMATIONLIST_LEFT.append(temp_list4_left)

#all animation list:
displayCharacterList = [character1_ANIMATIONLIST_RIGHT, character2_ANIMATIONLIST_RIGHT, character3_ANIMATIONLIST_RIGHT, character4_ANIMATIONLIST_RIGHT]
#-------------------------------------------------------------------------------------------#




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


#map attributes
mapGroundLevel = [0, MAP1_GROUND_LEVEL, MAP2_GROUND_LEVEL, MAP3_GROUND_LEVEL, MAP4_GROUND_LEVEL, MAP5_GROUND_LEVEL]
mapPool = [0, [], [], [], [], []]


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

    player1_PFP = pfp[GameState.p1_character]
    player1_ANIMATIONLIST_LEFT = animationlist_left[GameState.p1_character]
    player1_ANIMATIONLIST_RIGHT = animationlist_right[GameState.p1_character]
    player1_hitbox_width = HITBOX_WIDTH[GameState.p1_character]
    player1_hitbox_height = HITBOX_HEIGHT[GameState.p1_character]
    player1_atk1_width = ATK1_WIDTH[GameState.p1_character]
    player1_atk1_height = ATK1_HEIGHT[GameState.p1_character]
    player1_atk1_hitframe = ATK1_HIT_FRAME[GameState.p1_character]
    player1_atk1_y_shift = ATK1_Y_SHIFT[GameState.p1_character]
    player1_atk1_damage = ATK1_DAMAGE[GameState.p1_character]
    player1_atk1_cooldown = ATK1_COOLDOWN[GameState.p1_character]
    player1_atk2_width = ATK2_WIDTH[GameState.p1_character]
    player1_atk2_height = ATK2_HEIGHT[GameState.p1_character]
    player1_atk2_hitframe = ATK2_HIT_FRAME[GameState.p1_character]
    player1_atk2_y_shift = ATK2_Y_SHIFT[GameState.p1_character]
    player1_atk2_damage = ATK2_DAMAGE[GameState.p1_character]
    player1_atk2_cooldown = ATK2_COOLDOWN[GameState.p1_character]



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

    player2_PFP = pfp[GameState.p2_character]
    player2_ANIMATIONLIST_LEFT = animationlist_left[GameState.p2_character]
    player2_ANIMATIONLIST_RIGHT = animationlist_right[GameState.p2_character]
    player2_hitbox_width = HITBOX_WIDTH[GameState.p2_character]
    player2_hitbox_height = HITBOX_HEIGHT[GameState.p2_character]
    player2_atk1_width = ATK1_WIDTH[GameState.p2_character]
    player2_atk1_height = ATK1_HEIGHT[GameState.p2_character]
    player2_atk1_hitframe = ATK1_HIT_FRAME[GameState.p2_character]
    player2_atk1_y_shift = ATK1_Y_SHIFT[GameState.p2_character]
    player2_atk1_damage = ATK1_DAMAGE[GameState.p2_character]
    player2_atk1_cooldown = ATK1_COOLDOWN[GameState.p2_character]
    player2_atk2_width = ATK2_WIDTH[GameState.p2_character]
    player2_atk2_height = ATK2_HEIGHT[GameState.p2_character]
    player2_atk2_hitframe = ATK2_HIT_FRAME[GameState.p2_character]
    player2_atk2_y_shift = ATK2_Y_SHIFT[GameState.p2_character]
    player2_atk2_damage = ATK2_DAMAGE[GameState.p2_character]
    player2_atk2_cooldown = ATK2_COOLDOWN[GameState.p2_character]



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

    #atk 2 animation
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

in_play = True
display_background = True
display_map_select = False
display_character_select_1 = False
display_character_select_2 = False
display_countdown = False
display_fight = False

print("Hold ESC to Exit Game Window.")

menuBackgroundMusic.play(-1)

########################IN GAME STATE NOW####################
# selected_map = 0
# p1_character = 0
# p2_character = 0

background = Menu()
map_select = MapSelect()
character_select_1 = CharacterSelect(1)
character_select_2 = CharacterSelect(2)
countdown = Countdown()
fight = None
gameover = GameOver()

while in_play: 

    while display_background:
        background.display_menu(gameWindow)
        event = background.handle_events()

        if event == "FORWARD":
            display_background = False
            display_map_select = True

        pygame.display.update()
        

    while display_map_select:
        map_select.display_map_select(gameWindow)
        event, committed_map = map_select.handle_events()

        pygame.display.update()
        
        if event == "FORWARD":
            GameState.selected_map = committed_map
            display_map_select = False
            display_character_select_1 = True
        if event == "BACK":
            display_map_select = False
            display_background = True


    while display_character_select_1:

        character_select_1.display_character_select(gameWindow)
        event, committed_character = character_select_1.handle_events()

        pygame.display.update()
        
        if event == "FORWARD":
            GameState.p1_character = committed_character
            display_character_select_1 = False
            display_character_select_2 = True
            
        if event == "BACK":
            display_character_select_1 = False
            display_map_select = True



    while display_character_select_2:

        character_select_2.display_character_select(gameWindow, taken_character=GameState.p1_character)
        event, committed_character = character_select_2.handle_events(taken_character=GameState.p1_character)

        pygame.display.update()
        
        if event == "FORWARD":
            GameState.p2_character = committed_character

            fight = Fight(GameState.p1_character, GameState.p2_character, GameState.selected_map)

            display_character_select_2 = False
            display_countdown = True
            
        if event == "BACK":
            display_character_select_2 = False
            display_character_select_1 = True

    
    while display_countdown:

        countdown.display_countdown(gameWindow, map_number=GameState.selected_map)

        pygame.display.update()

        if countdown.second < 0:
            display_countdown = False
            display_fight = True



    while display_fight:

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
        if GameState.p1_character == 1:
            player1_atk2_x_RIGHT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2
            player1_atk2_x_LEFT = player1_hitbox_x - (player1_atk2_width - player1_hitbox_width)//2
        elif GameState.p1_character == 4:
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
        if GameState.p2_character == 1:
            player2_atk2_x_LEFT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2
            player2_atk2_x_RIGHT = player2_hitbox_x - (player2_atk2_width - player2_hitbox_width)//2
        elif GameState.p2_character == 4:
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

        if not player1_takehit_animation and player1_alive and not display_countdown:

            #p1 controls
            if keys[pygame.K_d]:     #move to right
                if (player1_hitbox_y + player1_hitbox_height) == MAP_GROUND_LEVEL:
                    actionP1 = 1

                if player1Direction == "left":
                    player1Direction = "right"
                    frameP1 = 0
                    
                else:
                    dx1 = RUNNING_SPEED


            elif keys[pygame.K_a]:      #move to left
                if (player1_hitbox_y + player1_hitbox_height) == MAP_GROUND_LEVEL:
                    actionP1 = 1

                if player1Direction == "right":
                    player1Direction = "left"
                    frameP1 = 0

                else:
                    dx1 = -RUNNING_SPEED

            else:
                dx1 = 0
            

            if (player1_hitbox_y + player1_hitbox_height) == MAP_GROUND_LEVEL:

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


        if not player2_takehit_animation and player2_alive and not display_countdown:
            
            #p2 controls
            if keys[pygame.K_l]:    #move right
                if (player2_hitbox_y + player2_hitbox_height) == MAP_GROUND_LEVEL:
                    actionP2 = 1

                if player2Direction == 'left':
                    player2Direction = "right"
                    frameP2 = 0

                else:
                    dx2 = RUNNING_SPEED


            elif keys[pygame.K_j]:   #move left
                if (player2_hitbox_y + player2_hitbox_height) == MAP_GROUND_LEVEL:
                    actionP2 = 1

                if player2Direction == 'right':
                    player2Direction = "left"
                    frameP2 = 0

                else:
                    dx2 = -RUNNING_SPEED
                    
            else:
                dx2 = 0

            if (player2_hitbox_y + player2_hitbox_height) == MAP_GROUND_LEVEL:

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

        if player1_y > MAP_GROUND_LEVEL - playerH:
            player1_y = MAP_GROUND_LEVEL - playerH
            dy1 = 0


        #p2
        player2_x += dx2
        dy2 += GRAVITY
        player2_y += dy2

        if player2_y > MAP_GROUND_LEVEL - playerH:
            player2_y = MAP_GROUND_LEVEL - playerH
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

            gameover.display_gameover(gameWindow)
        #--------------------------------------------------------------------------------------#

        pygame.display.update()
