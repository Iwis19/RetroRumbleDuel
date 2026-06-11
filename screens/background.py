import pygame
import os
from config import *

class Background:

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

    def display_background(self, gameWindow):

        title_text = pygame.transform.scale(pygame.image.load(asset_path("MENUBACKGROUND/RetroRumbleDuel.png")), (WIDTH,HEIGHT)).convert_alpha()
        continue_text = continueTextFont.render("Hold SPACEBAR to Continue", True, WHITE)
        continue_text_location = continue_text.get_rect(center = (WIDTH//2, 370))

        update_interval = 150

        time = pygame.time.get_ticks()

        # when update_interval is reached, update the frames and reset timer
        if time - self.background_reference_time > update_interval:
            self.background_reference_time = time
            self.background_frame += 1

        if self.background_frame >= len(self.background):
            self.background_frame = 0

        gameWindow.blit(self.background[self.background_frame], (ORIGIN))
        gameWindow.blit(continue_text, continue_text_location)
        gameWindow.blit(title_text, (0, -30))
