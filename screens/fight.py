import pygame
from config import *
from entity.player import Player
from entity.map import Map
from screens.screen import Screen
from screens.hud.playerhud import PlayerHUD


class Fight(Screen):

    MAPS = Map.load_all()
    
    def __init__(
        self,
        player_1_character: int,
        player_2_character: int,
        map_number: int
    ):  
        self.stage = self.MAPS[map_number]
        self.background_frame = 0
        self.background_reference_time = pygame.time.get_ticks()
        self.player_1 = Player(1, player_1_character)
        self.player_2 = Player(2, player_2_character)
        self.player_1.enter_stage(self.stage)
        self.player_2.enter_stage(self.stage)
        self.player_1_HUD = PlayerHUD(self.player_1)
        self.player_2_HUD = PlayerHUD(self.player_2)

    def display_fight(self, gameWindow):
        
        self.display_background(gameWindow, self.stage.animations)
        clock.tick(FPS)

        gameWindow.blit(self.player_1.animations[self.player_1.direction][self.player_1.action][self.player_1.frame], self.player_1.get_location())
        self.player_1.animation()
        
        gameWindow.blit(self.player_2.animations[self.player_2.direction][self.player_2.action][self.player_2.frame], self.player_2.get_location())
        self.player_2.animation()

        self.handle_events()

        self.player_1.update()
        self.player_2.update()

        self.player_1_HUD.display_fight_gui(gameWindow)
        self.player_2_HUD.display_fight_gui(gameWindow)

        self.player_hit()


    def display_background(self, gameWindow, frames: list):

        self.display_animation(
            gameWindow, 
            frames=frames, 
            frame_attr="background_frame",
            reference_time_attr="background_reference_time",
            location=ORIGIN
        )

    def handle_events(self):
        events = pygame.event.get()

        self.player_1.handle_player_events(events=events)
        self.player_2.handle_player_events(events=events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_exit_button(event)
                    
    def player_hit(self):
        
        self.player_1.player_hit(self.player_2)
        self.player_2.player_hit(self.player_1)


    @property
    def death_animation_over(self):
        return self.player_1.stop_animation or self.player_2.stop_animation