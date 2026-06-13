from config import *

class Player:

    #---------------------------------------#
    #            VARRRRRRSSSSSSSS           #
    #---------------------------------------#

    def __init__(
        self,
        player_number  # 1 or 2
    ):
        self.player_number = player_number
        self.health = 100

        self.atk1_cooldown = None
        self.atk2_cooldown = None

        self.load_properties()

    def load_properties(self):
        self.atk1_cooldown = ATK1_COOLDOWN[self.player_number]
        self.atk2_cooldown = ATK2_COOLDOWN[self.player_number]

