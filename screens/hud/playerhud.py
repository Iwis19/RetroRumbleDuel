from config import *
from entity.player import Player

class PlayerHUD:

    player_info_location_x = [0, 90, 750]
    player_info_location_center = [(0,0), (WIDTH//4 - 40, 270), (3*WIDTH//4 + 20, 270)]

    pfp_box_y = 55
    pfp_box_width = 83
    pfp_box_height = 80
    pfp_box_x = [0, REFERENCE_BAR_X[1] - pfp_box_width + 3, REFERENCE_BAR_X[2] - 3]

    name_bar_y = 55
    name_bar_width = 120
    name_bar_height = 30
    name_bar_x = [0, REFERENCE_BAR_X[1], REFERENCE_BAR_X[2] - name_bar_width]

    health_bar_y = 80
    health_bar_width = 210
    health_bar_height = 30
    health_bar = health_bar_width - 10
    health_bar_x = [0, REFERENCE_BAR_X[1], REFERENCE_BAR_X[2] - health_bar_width]

    atk1_cd_bar_width = 150
    atk1_cd_bar_height = 30
    atk1_cd_bar_y = 105
    atk1_cd_bar = atk1_cd_bar_width - 10
    atk1_cd_bar_x = [0, REFERENCE_BAR_X[1], REFERENCE_BAR_X[2] - atk1_cd_bar_width]

    atk2_cd_bar_width = 250
    atk2_cd_bar_height = 30
    atk2_cd_bar_y = 130
    atk2_cd_bar = atk1_cd_bar_width - 10
    atk2_cd_bar_x = [0, REFERENCE_BAR_X[1] - pfp_box_width + 3, REFERENCE_BAR_X[2] - atk2_cd_bar_width + pfp_box_width - 3]

    def __init__(
        self,
        player: Player
    ):
        self.player_number = player.player_number
        self.player = player

    def display_countdown_information(self, gameWindow):

        player_info_1 = gui_font.render(f"Player {self.player_number} User Interface:", True, WHITE)
        player_info_2 = gui_information_font.render(f"Healthbar: RED, HP: {self.player.health}", True, WHITE)
        player_info_3 = gui_information_font.render(f"Attack 1 Cooldown Bar: BLUE, COOLDOWN: {self.player.atk1_cooldown/1000}s", True, WHITE)
        player_info_4 = gui_information_font.render(f"Attack 2 Cooldown Bar: YELLOW, COOLDOWN: {self.player.atk2_cooldown/1000}s", True, WHITE)

        player_info_1_location = player_info_1.get_rect(center=self.player_info_location_center[self.player_number])
        player_info_2_location = (self.player_info_location_x[self.player_number], 310)
        player_info_3_location = (self.player_info_location_x[self.player_number], 340)
        player_info_4_location = (self.player_info_location_x[self.player_number], 370)

        gameWindow.blit(player_info_1, player_info_1_location)
        gameWindow.blit(player_info_2, player_info_2_location)
        gameWindow.blit(player_info_3, player_info_3_location)
        gameWindow.blit(player_info_4, player_info_4_location)

    def display_fight_gui(self, gameWindow):

        player_text = name_text_font.render(f"Player {self.player_number}", True, BLACK)

        player_health_bar_width = self.player.get_health_percentage() * self.health_bar if self.player.is_alive else 0

        player_atk1_cd_bar_width = self.player.get_atk1_recharge_percentage() * (self.atk1_cd_bar_width - 10) if not self.player.can_use_atk1 else self.atk1_cd_bar_width - 10
        
        player_atk2_cd_bar_width = self.player.get_atk2_recharge_percentage() * (self.atk2_cd_bar_width - 10) if not self.player.can_use_atk2 else self.atk2_cd_bar_width - 10
        
        pygame.draw.rect(gameWindow, BAR_COLOR, (self.pfp_box_x[self.player_number], self.pfp_box_y, self.pfp_box_width, self.pfp_box_height), False)
        gameWindow.blit(self.player.profile_picture, (self.pfp_box_x[self.player_number] + 4, self.pfp_box_y + 4, self.pfp_box_width - 8, self.pfp_box_height - 8))
        pygame.draw.rect(gameWindow, BLACK, (self.pfp_box_x[self.player_number] + 4, self.pfp_box_y + 4, self.pfp_box_width - 8, self.pfp_box_height - 8), 2)

        pygame.draw.rect(gameWindow, BAR_COLOR, (self.name_bar_x[self.player_number], self.name_bar_y, self.name_bar_width, self.name_bar_height), False, 5)
        gameWindow.blit(player_text, (self.name_bar_x[self.player_number] + 10, self.name_bar_y))

        pygame.draw.rect(gameWindow, BAR_COLOR, (self.health_bar_x[self.player_number], self.health_bar_y, self.health_bar_width, self.health_bar_height), False, 5)
        pygame.draw.rect(gameWindow, RED, (self.health_bar_x[self.player_number] + 5, self.health_bar_y + 5, player_health_bar_width, self.health_bar_height - 10), False, 4)
        pygame.draw.rect(gameWindow, BLACK, (self.health_bar_x[self.player_number] + 5, self.health_bar_y + 5, self.health_bar_width - 10, self.health_bar_height - 10), 2, 4)

        pygame.draw.rect(gameWindow, BAR_COLOR, (self.atk1_cd_bar_x[self.player_number], self.atk1_cd_bar_y, self.atk1_cd_bar_width, self.atk1_cd_bar_height), False, 5)
        pygame.draw.rect(gameWindow, CD_BLUE, (self.atk1_cd_bar_x[self.player_number] + 5, self.atk1_cd_bar_y + 5, player_atk1_cd_bar_width, self.atk1_cd_bar_height - 10), False, 4)
        pygame.draw.rect(gameWindow, BLACK, (self.atk1_cd_bar_x[self.player_number] + 5, self.atk1_cd_bar_y + 5, self.atk1_cd_bar_width - 10, self.atk1_cd_bar_height - 10), 2, 4)

        pygame.draw.rect(gameWindow, BAR_COLOR, (self.atk2_cd_bar_x[self.player_number], self.atk2_cd_bar_y, self.atk2_cd_bar_width, self.atk2_cd_bar_height), False, 5)
        pygame.draw.rect(gameWindow, YELLOW, (self.atk2_cd_bar_x[self.player_number] + 5, self.atk2_cd_bar_y + 5, player_atk2_cd_bar_width, self.atk2_cd_bar_height - 10), False, 4)
        pygame.draw.rect(gameWindow, BLACK, (self.atk2_cd_bar_x[self.player_number] + 5, self.atk2_cd_bar_y + 5, self.atk2_cd_bar_width - 10, self.atk2_cd_bar_height - 10), 2, 4)