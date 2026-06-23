import pygame
from config import *
from entity.map import Map
from entity.player import Player
from screens.screen import Screen
from screens.hud.playerhud import PlayerHUD

class Countdown(Screen):

    MAPS = Map.load_all()
    
    def __init__(
            self,
            player_1_character: int,
            player_2_character: int
        ):
        self.background_frame = 0
        self.background_reference_timer = pygame.time.get_ticks()
        self.countdown_start_time = pygame.time.get_ticks()
        self.second = 6
        self.player_1 = Player(1, player_1_character)
        self.player_2 = Player(2, player_2_character)

    def display_countdown(self, gameWindow, map_number: int, p1_character: int, p2_character: int):

        self.display_background(gameWindow, self.MAPS[map_number].animations)
        clock.tick(FPS)

        gameWindow.blit(self.BLACK_BACKGROUND, (0, 100))

        time_passed = pygame.time.get_ticks()
        
        if time_passed - self.countdown_start_time >= TICK_SPEED:
            if self.second > 0:
                pygame.mixer.Channel(4).play(countdownSound)
            self.countdown_start_time = time_passed
            self.second -= 1

        countdown_text = countdown_text_font.render(f"{self.get_time_text()}", True, WHITE)
        countdown_text_location = countdown_text.get_rect(center = (WIDTH//2, HEIGHT//2))

        gameWindow.blit(countdown_text, countdown_text_location)

        PlayerHUD(self.player_1).display_countdown_information(gameWindow)
        PlayerHUD(self.player_2).display_countdown_information(gameWindow)

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.handle_exit_button(event)