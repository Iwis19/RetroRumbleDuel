import pygame

class Map:

    MAPS = [0, 1, 2, 3, 4, 5]
    MAP_DISPLAY_SIZE = (200, 100)

    WIDTH, HEIGHT = 1200, 600 

    def __init__(
        self,
        map_type
    ):
        self.map_type = map_type   # 0, 1, 2, 3, 4, 5
        self.map = None
        self.map_display = None

    # TODO: CHANGE BACKGROUND NAME TO MENU
    def load_map(self):
        map = []

        if self.map_type > 0:
            for frame in range(len(os.listdir(f"MAP{self.map_type}"))):
                map_frame = pygame.transform.scale(pygame.image.load(f"MAP{self.map_type}/tile00{frame}.png"), (self.WIDTH, self.HEIGHT)).convert_alpha()
                map.append(map_frame)
        else:
            print("Error: map_type cannot be 0")

        self.map = map

    def load_assets(self):
        self.map_display = pygame.transform.scale(pygame.image.load(f"MAP{self.map_type}/tile000.png"), self.MAP_DISPLAY_SIZE).convert_alpha()
        
        self.load_map()
