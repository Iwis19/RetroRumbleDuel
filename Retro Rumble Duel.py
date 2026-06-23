import pygame

pygame.init()

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

background = Menu()
map_select = MapSelect()
character_select_1 = CharacterSelect(1)
character_select_2 = CharacterSelect(2)
countdown = None
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

            countdown = Countdown(GameState.p1_character, GameState.p2_character)
            fight = Fight(GameState.p1_character, GameState.p2_character, GameState.selected_map)

            display_character_select_2 = False
            display_countdown = True
            
        if event == "BACK":
            display_character_select_2 = False
            display_character_select_1 = True


    
    while display_countdown:

        countdown.display_countdown(gameWindow, map_number=GameState.selected_map, p1_character=GameState.p1_character, p2_character=GameState.p2_character)
        countdown.handle_events()

        pygame.display.update()

        if countdown.second < 0:
            display_countdown = False
            display_fight = True



    while display_fight:

        fight.display_fight(gameWindow)
        
        if fight.death_animation_over:          #if death animation finished playing
            gameover.display_gameover(gameWindow)
            gameover.handle_events()
        
        pygame.display.update()
