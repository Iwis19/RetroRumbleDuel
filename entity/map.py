import pygame
import os
from config import *

class Map:
    
    def __init__(
        self,
        map_number
    ):
        self.map_number = map_number   # 0, 1, 2, 3, 4, 5
        self.map = None
        self.map_display = None

        self.load_assets()

    # TODO: CHANGE BACKGROUND NAME TO MENU
    def load_map(self):
        map = []

        if self.map_number > 0:
            for frame in range(len(os.listdir(asset_path(f"MAP{self.map_number}")))):
                map_frame = pygame.transform.scale(pygame.image.load(asset_path(f"MAP{self.map_number}", f"tile00{frame}.png")), (WIDTH, HEIGHT)).convert_alpha()
                map.append(map_frame)
        else:
            print("Error: map_type cannot be 0")

        self.map = map

    def load_assets(self):
        self.map_display = pygame.transform.scale(pygame.image.load(asset_path(f"MAP{self.map_number}", "tile000.png")), MAP_DISPLAY_SIZE).convert_alpha()
        
        self.load_map()
