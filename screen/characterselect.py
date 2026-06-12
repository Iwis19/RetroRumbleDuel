import sys
import pygame
from entity.character import Character
from screen.background import Background
from config import *

class CharacterSelect:

    CHARACTER_SELECTION_PICTURE = [None]
    for i in range(1, len(CHARACTER_NAMES)):
        picture = Character(i).selection_picture
        CHARACTER_SELECTION_PICTURE.append(picture)

    CHARACTER_SELECTION_PICTURE_X = [0, 205, 385, 205, 385]
    CHARACTER_SELECTION_PICTURE_Y = [0, 160, 160, 350, 350]

    CHARACTER_SELECTION_RECTS = [None]
    for i in range(1, len(CHARACTER_NAMES)):
        CHARACTER_SELECTION_RECTS.append(
            pygame.Rect(
                CHARACTER_SELECTION_PICTURE_X[i], 
                CHARACTER_SELECTION_PICTURE_Y[i], 
                PORTRAIT_WIDTH, 
                PORTRAIT_HEIGHT
            )
        )

    character_selection_arrow_x = [-1000, CHARACTER_SELECTION_PICTURE_X[1] + PORTRAIT_WIDTH//2, CHARACTER_SELECTION_PICTURE_X[2] + PORTRAIT_WIDTH//2, CHARACTER_SELECTION_PICTURE_X[3] + PORTRAIT_WIDTH//2, CHARACTER_SELECTION_PICTURE_X[4] + PORTRAIT_WIDTH//2]
    character_selection_arrow_y = 0

    BACKGROUND_DISPLAY = Background().background[0]

    PLAYER_CONTROL_TEXT = [
        ["Jump: W", "Run: A, D", "Attack 1: E", "Attack 2: R"], 
        ["Jump: I", "Run: J, L", "Attack 1: O", "Attack 2: P"]
    ]
    PLAYER_CONTROL_TEXT_LOCATION = [(835, 478), (835, 500), (975, 478), (975, 500)]
    

    def __init__(
        self,
        player: int
    ):
        self.player = player
        self.selected_character_frame = 0
        self.selected_character_reference_time = pygame.time.get_ticks()

    
    def display_character_select(self, gameWindow, selected_character, taken_character):

        gameWindow.blit(self.BACKGROUND_DISPLAY, ORIGIN)
        
        # main boxes
        pygame.draw.rect(gameWindow, BLACK, (20, 20, 700, 560), False, 6)            
        pygame.draw.rect(gameWindow, DARKRED, (20, 20 , 700, 560), 4, 6) 

        pygame.draw.rect(gameWindow, BLACK, (740, 20, 440, 560), False, 6)            
        pygame.draw.rect(gameWindow, DARKRED, (740, 20, 440, 560), 4, 6)

        # forward & backward buttons
        pygame.draw.polygon(gameWindow, WHITE, ((BACK_BUTTON_X, MOVE_BUTTON_Y), (BACK_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (BACK_BUTTON_X - MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))     #back
        pygame.draw.polygon(gameWindow, WHITE, ((FORWARD_BUTTON_X, MOVE_BUTTON_Y), (FORWARD_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (FORWARD_BUTTON_X + MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))      #forward
        
        self.display_selected_character(gameWindow, selected_character)

        player_select_text = selectCharacterFont.render(f"Choose your character: (P{self.player})", True, WHITE)
        gameWindow.blit(player_select_text, (140, 75))

        player_control_title = controlFont.render(f"Player {self.player} Controls:", True, WHITE)
        player_control_title_location = player_control_title.get_rect(center = (960, 437))
        gameWindow.blit(player_control_title, player_control_title_location)

        for i in range(len(self.PLAYER_CONTROL_TEXT[self.player])):
            control_text = controlKeysFont.render(self.PLAYER_CONTROL_TEXT[self.player][i], True, WHITE)
            gameWindow.blit(control_text, self.PLAYER_CONTROL_TEXT_LOCATION[i])

        player_character_name_text = playerCharacterNameTextFont.render(f"{CHARACTER_NAMES[selected_character]}", True, WHITE)
        player_character_name_text_location = player_character_name_text.get_rect(center = (960, 95))
        gameWindow.blit(player_character_name_text, player_character_name_text_location)

        if 1 <= selected_character <= 2:
            self.character_selection_arrow_y = self.CHARACTER_SELECTION_PICTURE_Y[1] + PORTRAIT_HEIGHT + 25
    
        elif 3 <= selected_character <= 4:
            self.character_selection_arrow_y = self.CHARACTER_SELECTION_PICTURE_Y[3] + PORTRAIT_HEIGHT + 25

        pygame.draw.polygon(gameWindow, WHITE, ((self.character_selection_arrow_x[selected_character] - 20, self.character_selection_arrow_y), (self.character_selection_arrow_x[selected_character] + 20, self.character_selection_arrow_y), (self.character_selection_arrow_x[selected_character], self.character_selection_arrow_y - 15)))

        for i in range(1, len(CHARACTER_NAMES)):
            gameWindow.blit(self.CHARACTER_SELECTION_PICTURE[i], (self.CHARACTER_SELECTION_PICTURE_X[i], self.CHARACTER_SELECTION_PICTURE_Y[i]))
            pygame.draw.rect(gameWindow, DARKRED, (self.CHARACTER_SELECTION_PICTURE_X[i], self.CHARACTER_SELECTION_PICTURE_Y[i], PORTRAIT_WIDTH, PORTRAIT_HEIGHT), 4)

        # if player is 2, they have a restriction from choosing p1's character
        if self.player == 2:
            taken_character_display_x = self.character_selection_arrow_x[taken_character]
            taken_character_display_y = self.character_selection_arrow_y[taken_character]
            pygame.draw.rect(gameWindow, DARKRED, (taken_character_display_x, taken_character_display_y, PORTRAIT_WIDTH, PORTRAIT_HEIGHT))
            taken_character_text_1 = taken_character_text_font.render("Taken", True, WHITE)
            taken_character_text_2 = taken_character_text_font.render("By P1", True, WHITE)
            taken_character_text_1_location = taken_character_text_1.get_rect(center = (taken_character_display_x + PORTRAIT_WIDTH//2, taken_character_display_y + PORTRAIT_HEIGHT//2 - 15))
            taken_character_text_2_location = taken_character_text_1.get_rect(center = (taken_character_display_x + PORTRAIT_WIDTH//2, taken_character_display_y + PORTRAIT_HEIGHT//2 - 15))
            gameWindow.blit(taken_character_text_1, taken_character_text_1_location)
            gameWindow.blit(taken_character_text_2, taken_character_text_2_location)



    def display_selected_character(self, gameWindow, selected_character):
        
        if selected_character > 0:
            
            character = Character(selected_character)
            idle_frames = character.animation_list[1][0]

            update_interval = 150
            time = pygame.time.get_ticks()

            if time - self.selected_character_reference_time > update_interval:
                self.selected_character_reference_time = time
                self.selected_character_frame += 1

            if self.selected_character_frame >= len(idle_frames):
                self.selected_character_frame = 0

            gameWindow.blit(idle_frames[self.selected_character_frame], (513, -60))


    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()

                for i in range(1, len(self.CHARACTER_SELECTION_RECTS)):
                    if self.CHARACTER_SELECTION_RECTS[i].collidepoint(mouseX, mouseY):
                        pygame.mixer.Channel(2).play(selection_sound)
                        print(f"{CHARACTER_NAMES[i]}, character #{i}")
                        return f"{i}"    # character selection

                if FORWARD_BUTTON_RECT.collidepoint(mouseX, mouseY):
                    pygame.mixer.Channel(2).play(button_click_sound)
                    return "FORWARD"

                if BACK_BUTTON_RECT.collidepoint(mouseX, mouseY):
                    pygame.mixer.Channel(2).play(button_click_sound)
                    return "BACK"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    #if escape is pressed, escape game
                    pygame.quit()   
                    sys.exit()

            