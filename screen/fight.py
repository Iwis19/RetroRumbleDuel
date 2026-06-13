import pygame
from config import *
from screen.screen import Screen
from entity.player import Player
from entity.map import Map

class Fight(Screen):

    MAPS = Map.load_all()
    
    def __init__(
        self,
        player_1_character: int,
        player_2_character: int,

    ):
        self.background_frame = 0
        self.background_reference_time = pygame.time.get_ticks()
        self.player_1 = Player(player_1_character)
        self.player_2 = Player(player_2_character)

    def display_fight(self, gameWindow, map_number: int):
        
        self.display_background(gameWindow, self.MAPS[map_number].map)
        clock.tick(FPS)

        gameWindow.blit(self.player_1.animations[self.player_1.direction][self.player_1.action][self.player_1.frame], self.player_1.get_location())
        self.player_1.animation()
        
        gameWindow.blit(self.player_2.animations[self.player_2.direction][self.player_2.action][self.player_2.frame], self.player_2.get_location())
        self.player_2.animation()

        self.player_1.update()
        self.player_2.update()


    def display_background(self, gameWindow, frames: list):

        self.display_animation(
            gameWindow, 
            frames=frames, 
            frame_attr="background_frame",
            reference_time_attr="background_reference_time",
            location=ORIGIN
        )

    
    def handle_events(self, map_number: int):

        #if not self.player_1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                # move right
                #if event.key == pygame.K_d:
                pass
                    

    def player_hit(self):
        
        self.player_1.player_hit(self.player_2)
        self.player_2.player_hit(self.player_1)
        