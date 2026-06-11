import os
import pygame

class Character:

    CHARACTER_NAMES = ['None Selected', 'Fire Knight', 'Wind Hashashin', 'Water Priestess', 'Metal Bladekeeper']

    PFP_WIDTH = 72
    PFP_HEIGHT = 72
    PFP_DIMENSION = (PFP_WIDTH, PFP_HEIGHT)

    PORTRAIT_HEIGHT = 130
    PORTRAIT_WIDTH = 130
    PORTRAIT_DIMENSION = (PORTRAIT_WIDTH, PORTRAIT_HEIGHT)

    IMAGE_WIDTH = 900
    IMAGE_HEIGHT = 400
    CHARACTER_DIMENSION = (IMAGE_WIDTH, IMAGE_HEIGHT)
    
    # possible actions
    ACTIONS = ["idle", "run", "jump_up", "jump_down", "atk1", "atk2", "take_hit", "death"]

    def __init__(
        self,
        character_number
    ):
        self.character_number = character_number
        self.animation_list = [[], []]    # 0: left, 1: right
        self.profile_picture = None
        self.selection_picture = None


    def load_animation(self):

        for animation in range(len(self.ACTIONS)):
            right, left = [], []
            frames = len(os.listdir(f"character{self.character_number}/png/0{animation + 1}_{self.ACTIONS[animation]}"))
            for items in range(frames):
                right_frame = pygame.transform.scale(pygame.image.load(f"character{self.character_number}/png/0{animation + 1}_{self.ACTIONS[animation]}/{self.ACTIONS[animation]}_{items + 1}.png"), self.CHARACTER_DIMENSION).convert_alpha()
                left_frame = pygame.transform.flip(right_frame, True, False).convert_alpha()
                right.append(right_frame)
                left.append(left_frame)
            self.animation_list[0].append(left)
            self.animation_list[1].append(right)

    def load_assets(self):

        self.profile_picture = pygame.transform.scale(pygame.image.load(f"character{self.character_number}/{self.CHARACTER_NAMES[self.character_number]}.png"), self.PFP_DIMENSION).convert_alpha()
        self.selection_picture = pygame.transform.scale(pygame.image.load(f"character{self.character_number}/{self.CHARACTER_NAMES[self.character_number]}.png"), self.PORTRAIT_DIMENSION).convert_alpha()
        self.load_animation()

        