from config import *
from entity.player import Player

class PlayerHUD:

    def __init__(
        self,
        player_number
    ):
        self.player = Player(player_number)

    def display_countdown_information(self, gameWindow, x, center):

        player_info_1 = gui_font.render(f"Player {self.player.player_number} User Interface:", True, WHITE)
        player_info_2 = gui_information_font.render(f"Healthbar: RED, HP: {self.player.health}", True, WHITE)
        player_info_3 = gui_information_font.render(f"Attack 1 Cooldown Bar: BLUE, COOLDOWN: {self.player.atk1_cooldown/1000}s", True, WHITE)
        player_info_4 = gui_information_font.render(f"Attack 2 Cooldown Bar: YELLOW, COOLDOWN: {self.player.atk2_cooldown/1000}s", True, WHITE)

        player_info_1_location = player_info_1.get_rect(center = center)
        player_info_2_location = (x, 310)
        player_info_3_location = (x, 340)
        player_info_4_location = (x, 370)

        gameWindow.blit(player_info_1, player_info_1_location)
        gameWindow.blit(player_info_2, player_info_2_location)
        gameWindow.blit(player_info_3, player_info_3_location)
        gameWindow.blit(player_info_4, player_info_4_location)