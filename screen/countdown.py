from screen.screen import Screen
from entity.map import Map
from config import *
from screen.hud.playerhud import PlayerHUD
import pygame

class Countdown(Screen):

    MAPS = Map.load_all()

    PLAYER_HUDS = [None, PlayerHUD(1), PlayerHUD(2)]
    
    def __init__(self):
        self.background_frame = 0
        self.background_reference_timer = pygame.time.get_ticks()
        self.countdown_start_time = pygame.time.get_ticks()
        self.second = 6

    def display_countdown(self, gameWindow, map_number: int):

        self.display_background(gameWindow, self.MAPS[map_number].map)
        clock.tick(FPS)

        gameWindow.blit(self.BLACK_BACKGROUND, (0, 100))

        time_passed = pygame.time.get_ticks()
        
        if time_passed - self.countdown_start_time >= TICK_SPEED:
            if self.second > 0:
                pygame.mixer.Channel(4).play(countdownSound)
            self.countdown_start_time = time_passed
            self.second -= 1

        countdown_text = countdownFont.render(f"{self.get_time_text()}", True, WHITE)
        countdown_text_location = countdown_text.get_rect(center = (WIDTH//2, HEIGHT//2))

        gameWindow.blit(countdown_text, countdown_text_location)

        self.PLAYER_HUDS[1].display_countdown_information(gameWindow, 90, (WIDTH//4 - 40, 270))
        self.PLAYER_HUDS[2].display_countdown_information(gameWindow, 750, (3*WIDTH//4 + 20, 270))

    def get_time_text(self):
        if self.second > 0:
            return f"{self.second}"
        else:
            return "FIGHT!"

    def display_background(self, gameWindow, frames: list):

        self.display_animation(
            gameWindow=gameWindow, 
            frames=frames, 
            frame_attr="background_frame", 
            reference_time_attr="background_reference_timer"
        )
