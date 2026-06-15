import pygame
import sys
from config import *
from screen.screen import Screen

class GameOver(Screen):

    def __init__(self):
        self.game_close_reference_time = pygame.time.get_ticks()
        self.seconds = 10

    def display_gameover(self, gameWindow):

        close_time = pygame.time.get_ticks()

        if close_time - self.game_close_reference_time > TICK_SPEED:
            self.game_close_reference_time = close_time
            self.seconds -= 1

        if self.seconds <= 0:
            sys.exit()

        game_over_text = game_over_font.render('GAME OVER', True, WHITE)
        game_over_text_location = game_over_text.get_rect(center = (WIDTH//2, HEIGHT//2))

        game_close_text = game_close_font.render(f'Game will auto close in {self.seconds} seconds', True, WHITE)
        game_close_text_location = game_close_text.get_rect(center = (WIDTH//2, HEIGHT//2 + 50))

        gameWindow.blit(self.BLACK_BACKGROUND, (0, 100))
        gameWindow.blit(game_over_text, game_over_text_location)
        gameWindow.blit(game_close_text, game_close_text_location)