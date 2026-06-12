import os
import pygame
from config import *

class Character:
    
    # possible actions
    ACTIONS = [None, "idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]

    def __init__(
        self,
        character_number
    ):
        self.character_number = character_number
        self.animation_list = [[], []]    # 0: left, 1: right
        self.profile_picture = None
        self.selection_picture = None

        self.load_assets()


    def load_animation(self):

        for animation in range(1, len(self.ACTIONS)):
            right, left = [], []
            frames = len(os.listdir(asset_path(f"character{self.character_number}/png/0{animation}_{self.ACTIONS[animation]}")))
            for frame in range(frames):
                right_frame = pygame.transform.scale(pygame.image.load(asset_path(f"character{self.character_number}/png/0{animation}_{self.ACTIONS[animation]}/{self.ACTIONS[animation]}_{frame + 1}.png")), CHARACTER_DIMENSION).convert_alpha()
                left_frame = pygame.transform.flip(right_frame, True, False).convert_alpha()
                right.append(right_frame)
                left.append(left_frame)
            self.animation_list[0].append(left)
            self.animation_list[1].append(right)

    def load_assets(self):

        self.profile_picture = pygame.transform.scale(pygame.image.load(asset_path(f"character{self.character_number}/{CHARACTER_FILE_NAMES[self.character_number]}.png")), PFP_DIMENSION).convert_alpha()
        self.selection_picture = pygame.transform.scale(pygame.image.load(asset_path(f"character{self.character_number}/{CHARACTER_FILE_NAMES[self.character_number]}.png")), PORTRAIT_DIMENSION).convert_alpha()
        self.load_animation()

        