import pygame
import os
from screen.background import Background
from entity.map import Map
from config import *
import sys

class MapSelect:

    MAP_DISPLAY_X = [0, 60, 280, 500, 720, 940]
    MAP_DISPLAY_Y = 288
    MAP_DISPLAY_WIDTH = 200
    MAP_DISPLAY_HEIGHT = 100

    MAP_SELECTION_ARROW_X = [-1000, MAP_DISPLAY_X[1] + MAP_DISPLAY_WIDTH//2, MAP_DISPLAY_X[2] + MAP_DISPLAY_WIDTH//2, MAP_DISPLAY_X[3] + MAP_DISPLAY_WIDTH//2, MAP_DISPLAY_X[4] + MAP_DISPLAY_WIDTH//2, MAP_DISPLAY_X[5] + MAP_DISPLAY_WIDTH//2]
    MAP_SELECTION_ARROW_Y = MAP_DISPLAY_Y + 125

    MAP_DISPLAY_RECTS = [0]
    for i in range(1,len(MAPS)):
        MAP_DISPLAY_RECTS.append(
            pygame.Rect( 
                MAP_DISPLAY_X[i], 
                MAP_DISPLAY_Y, 
                MAP_DISPLAY_WIDTH, 
                MAP_DISPLAY_HEIGHT
            )
        )
    
    MAP_DISPLAYS = [0]
    for i in range(1, len(MAPS)):
        MAP_DISPLAYS.append(Map(i).map_display)

    BACKGROUND_DISPLAY = Background().background[0]

    def __init__(self):   
        pass
        
    def display_map_select(self, gameWindow, selected_map): 

        gameWindow.blit(self.BACKGROUND_DISPLAY, ORIGIN)

        # text and background boxes
        choose_map_text = selectMapFont.render("Select the Duel Stage:", True, WHITE)
        choose_map_text_location = choose_map_text.get_rect(center = (WIDTH//2, 170))
        pygame.draw.rect(gameWindow, BLACK, (20, 20, 1160, 560), False, 3)            #black box background
        pygame.draw.rect(gameWindow, DARKRED, (20, 20 , 1160, 560), 4, 3)           #red outline of the black box
        gameWindow.blit(choose_map_text, choose_map_text_location)

        # forward & backward buttons
        pygame.draw.polygon(gameWindow, WHITE, ((BACK_BUTTON_X, MOVE_BUTTON_Y), (BACK_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (BACK_BUTTON_X - MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))     #back
        pygame.draw.polygon(gameWindow, WHITE if selected_map else GRAY, ((FORWARD_BUTTON_X, MOVE_BUTTON_Y), (FORWARD_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (FORWARD_BUTTON_X + MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))   #forward

        # map squares for choices
        for map_number in range(1, len(MAPS)): # MAPS contains map 1-5 and 0 as place holder for none
            map_text = mapTextFont.render(f"Map {map_number}", True, WHITE)
            map_text_location = map_text.get_rect(center = (self.MAP_DISPLAY_X[map_number] + self.MAP_DISPLAY_WIDTH//2, self.MAP_DISPLAY_Y - 20))

            gameWindow.blit(self.MAP_DISPLAYS[map_number], (self.MAP_DISPLAY_X[map_number], self.MAP_DISPLAY_Y))
            pygame.draw.rect(gameWindow, DARKRED, (self.MAP_DISPLAY_X[map_number], self.MAP_DISPLAY_Y, self.MAP_DISPLAY_WIDTH, self.MAP_DISPLAY_HEIGHT), 3)
            gameWindow.blit(map_text, map_text_location)

        # map selection arrow
        pygame.draw.polygon(gameWindow, WHITE, ((self.MAP_SELECTION_ARROW_X[selected_map] - 20, self.MAP_SELECTION_ARROW_Y), (self.MAP_SELECTION_ARROW_X[selected_map] + 20, self.MAP_SELECTION_ARROW_Y), (self.MAP_SELECTION_ARROW_X[selected_map], self.MAP_SELECTION_ARROW_Y - 15)) )

        chosen_map = selectedMapFont.render(f"Selected: Map {selected_map}", True, WHITE)
        no_chosen_map = selectedMapFont.render(f"Selected: None", True, WHITE)
        chosen_map_location = chosen_map.get_rect(center = (WIDTH//2, 465))

        if selected_map > 0:
            gameWindow.blit(chosen_map, chosen_map_location)
        else: 
            gameWindow.blit(no_chosen_map, chosen_map_location)

    def handle_events(self, selected_map):
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:         #map selections and move between pages
                mouseX, mouseY = pygame.mouse.get_pos()

                for i in range(1, len(self.MAP_DISPLAY_RECTS)):
                    if self.MAP_DISPLAY_RECTS[i].collidepoint(mouseX, mouseY):
                        pygame.mixer.Channel(1).play(selection_sound)
                        return f"{i}"
                    
                if selected_map and FORWARD_BUTTON_RECT.collidepoint(mouseX, mouseY):
                    pygame.mixer.Channel(1).play(button_click_sound)
                    return "FORWARD"

                if BACK_BUTTON_RECT.collidepoint(mouseX, mouseY):
                    pygame.mixer.Channel(1).play(button_click_sound)
                    return "BACK"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    #if escape is pressed, escape game
                    pygame.quit()   
                    sys.exit()




