import pygame
import sys
from config import *

class Screen:

    BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load(asset_path("COUNTDOWNBACKGROUND/solid_black.png")), (WIDTH, 400)).convert().set_alpha(210)

    def handle_view_button(self, mouse_position: tuple, information: int, condition: bool):
        if FORWARD_BUTTON_RECT.collidepoint(mouse_position) and condition:
            pygame.mixer.Channel(2).play(button_click_sound)
            return ("FORWARD", information)

        if BACK_BUTTON_RECT.collidepoint(mouse_position):
            pygame.mixer.Channel(2).play(button_click_sound)
            return ("BACK", information)
        
        return None
        
    def handle_exit_button(self, event):
        if event.key == pygame.K_ESCAPE:    #if escape is pressed, escape game
            pygame.quit()   
            sys.exit()


    def display_view_buttons(self, gameWindow, condition: bool):

        # forward & backward buttons
        pygame.draw.polygon(gameWindow, WHITE, ((BACK_BUTTON_X, MOVE_BUTTON_Y), (BACK_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (BACK_BUTTON_X - MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))     #back
        pygame.draw.polygon(gameWindow, WHITE if condition else GRAY, ((FORWARD_BUTTON_X, MOVE_BUTTON_Y), (FORWARD_BUTTON_X, MOVE_BUTTON_Y + MOVE_BUTTON_H), (FORWARD_BUTTON_X + MOVE_BOTTON_W, MOVE_BUTTON_Y + MOVE_BUTTON_H//2)))   #forward


    def display_animation(self, gameWindow, frames: list, frame_attr: str, reference_time_attr: str, location: tuple=ORIGIN):
        
        time = pygame.time.get_ticks()
        
        frame = getattr(self, frame_attr)
        reference_time = getattr(self, reference_time_attr)

        if time - reference_time > UPDATE_INTERVAL:
            setattr(self, reference_time_attr, time)
            frame += 1

        if frame == len(frames):
            frame = 0

        setattr(self, frame_attr, frame)
        gameWindow.blit(frames[frame], location)
