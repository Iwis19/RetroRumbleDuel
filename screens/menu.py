import pygame
import os
from config import *
from screen.screen import Screen

class Menu(Screen):

    def __init__(self):
        self.background = None
        self.background_reference_time = pygame.time.get_ticks()
        self.background_frame = 0

        self.load_assets()
    
    def load_assets(self):
        background = []
        for frame in range(len(os.listdir(asset_path("MENUBACKGROUND"))) - 1):   # 5 pics total, only 4 are for background
            background_frame = pygame.transform.scale(pygame.image.load(asset_path(f"MENUBACKGROUND/tile00{frame}.png")), (WIDTH,HEIGHT)).convert_alpha()
            background.append(background_frame)
        self.background = background

    def display_menu(self, gameWindow):

        title_text = pygame.transform.scale(pygame.image.load(asset_path("MENUBACKGROUND/RetroRumbleDuel.png")), (WIDTH,HEIGHT)).convert_alpha()
        continue_text = continueTextFont.render("Hold SPACEBAR to Continue", True, WHITE)
        continue_text_location = continue_text.get_rect(center = (WIDTH//2, 370))

        self.display_background(gameWindow)

        gameWindow.blit(continue_text, continue_text_location)
        gameWindow.blit(title_text, (0, -30))

    def display_background(self, gameWindow):

        self.display_animation(gameWindow, self.background, frame_attr="background_frame", reference_time_attr="background_reference_time", location=ORIGIN)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:         #if space is pressed, go to next menu
                    return "FORWARD"

                self.handle_exit_button(event)