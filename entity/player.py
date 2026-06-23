from __future__ import annotations
import pygame
from config import *
from entity.character import Character
from entity.map import Map


class Player:

    PLAYER_W, PLAYER_H = 900, 400
    
    controls = {
        "right": [0, pygame.K_d, pygame.K_l],
        "left": [0, pygame.K_a, pygame.K_j],
        "jump": [0, pygame.K_w, pygame.K_i],
        "atk1": [0, pygame.K_e, pygame.K_o],
        "atk2": [0, pygame.K_r, pygame.K_p]
    }

    def __init__(
        self,
        player_number,  # 1 or 2
        character_number
    ):
        self.cooldown = 80
        self.health = MAX_HEALTH
        self.action = 0
        self.dx, self.dy = 0, 0

        self.ground_level = 0
        self.character_number = character_number
        self.player_number = player_number

        self.frame = 0
        self.time = pygame.time.get_ticks()

        self.direction = None
        self.character = None
        
        self.atk1_animation = False
        self.atk2_animation = False
        self.takehit_animation = False
        self.death_animation = False
        self.stop_animation = False

        self.x = None
        self.y = None

        self.profile_picture = None
        self.animations = None

        self.hitbox_width = None
        self.hitbox_height = None
        self.hitbox_x = None
        self.hitbox_y = None
        self.hitbox = None

        self.atk1_y = None
        self.atk1_x = None
        self.atk2_y = None
        self.atk2_x = None

        self.atk1_width = None
        self.atk1_height = None
        self.atk1_hitframe = None
        self.atk1_y_shift = None
        self.atk1_damage = None
        self.atk1_cooldown = None

        self.atk2_width = None
        self.atk2_height = None
        self.atk2_hitframe = None
        self.atk2_y_shift = None
        self.atk2_damage = None
        self.atk2_cooldown = None

        self.atk1_has_hit = False
        self.atk2_has_hit = False

        self.atk1_hitbox = None
        self.atk2_hitbox = None

        self.last_atk1_time = None
        self.last_atk2_time = None
        self.last_animation_time = None

        self.load_properties()

    def load_properties(self):
        if self.player_number == 1:
            self.direction = 1
        elif self.player_number == 2:
            self.direction = 0

        self.character = Character(self.character_number)

        self.x = INITIAL_X[self.player_number]
        self.y = INITIAL_Y

        self.profile_picture = self.character.profile_picture
        self.animations = self.character.animation_list
        self.hitbox_width = HITBOX_WIDTH[self.character_number]
        self.hitbox_height = HITBOX_HEIGHT[self.character_number]

        self.atk1_width = ATK1_WIDTH[self.character_number]
        self.atk1_height = ATK1_HEIGHT[self.character_number]
        self.atk1_hitframe = ATK1_HIT_FRAME[self.character_number]
        self.atk1_y_shift = ATK1_Y_SHIFT[self.character_number]
        self.atk1_damage = ATK1_DAMAGE[self.character_number]
        self.atk1_cooldown = ATK1_COOLDOWN[self.character_number]

        self.atk2_width = ATK2_WIDTH[self.character_number]
        self.atk2_height = ATK2_HEIGHT[self.character_number]
        self.atk2_hitframe = ATK2_HIT_FRAME[self.character_number]
        self.atk2_y_shift = ATK2_Y_SHIFT[self.character_number]
        self.atk2_damage = ATK2_DAMAGE[self.character_number]
        self.atk2_cooldown = ATK2_COOLDOWN[self.character_number]

        self.last_atk1_time = pygame.time.get_ticks()
        self.last_atk2_time = pygame.time.get_ticks()
        self.last_animation_time = pygame.time.get_ticks()

        self.hitbox_y = self.y + (self.PLAYER_H - self.hitbox_height)
        self.hitbox_x = self.x + (self.PLAYER_W - self.hitbox_width)//2

        self.atk1_y = self.hitbox_y + self.atk1_y_shift
        self.atk1_x = [self.hitbox_x - self.atk1_width, self.hitbox_x + self.hitbox_width]

        self.atk2_y = self.hitbox_y + self.atk2_y_shift

        if self.character_number == 1:
            self.atk2_x = [self.hitbox_x - (self.atk2_width - self.hitbox_width)//2, self.hitbox_x - (self.atk2_width - self.hitbox_width)//2]
        elif self.character_number == 4:
            self.atk2_x = [self.hitbox_x - (self.atk2_width - self.hitbox_width)//2 + 20, self.hitbox_x - (self.atk2_width - self.hitbox_width)//2 - 20]
        else:
            self.atk2_x = [self.hitbox_x - self.atk2_width, self.hitbox_x + self.hitbox_width]

        self.atk1_hitbox = pygame.Rect(0,0,0,0)
        self.atk2_hitbox = pygame.Rect(0,0,0,0)
        self.hitbox = pygame.Rect(self.hitbox_x, self.hitbox_y, self.hitbox_width, self.hitbox_height)
    
    def update(self):

        self.time = pygame.time.get_ticks()

        self.hitbox_y = self.y + (self.PLAYER_H - self.hitbox_height)
        self.hitbox_x = self.x + (self.PLAYER_W - self.hitbox_width)//2

        self.atk1_y = self.hitbox_y + self.atk1_y_shift
        self.atk1_x = [self.hitbox_x - self.atk1_width, self.hitbox_x + self.hitbox_width]

        self.atk2_y = self.hitbox_y + self.atk2_y_shift

        if self.character_number == 1:
            self.atk2_x = [self.hitbox_x - (self.atk2_width - self.hitbox_width)//2, self.hitbox_x - (self.atk2_width - self.hitbox_width)//2]
        elif self.character_number == 4:
            self.atk2_x = [self.hitbox_x - (self.atk2_width - self.hitbox_width)//2 + 20, self.hitbox_x - (self.atk2_width - self.hitbox_width)//2 - 20]
        else:
            self.atk2_x = [self.hitbox_x - self.atk2_width, self.hitbox_x + self.hitbox_width]

        self.hitbox = pygame.Rect(self.hitbox_x, self.hitbox_y, self.hitbox_width, self.hitbox_height)

        self.x += self.dx
        self.dy += GRAVITY
        self.y += self.dy

        if self.y >= self.ground_level - self.PLAYER_H:
            self.y = self.ground_level - self.PLAYER_H
            self.dy = 0

        self.check_boundaries()


    def check_boundaries(self):
        if self.x <= (LEFT - (self.PLAYER_W - self.hitbox_width)//2):
            self.x = (LEFT - (self.PLAYER_W - self.hitbox_width)//2)

        if self.x >= (RIGHT - (self.PLAYER_W + self.hitbox_width)//2):
            self.x = (RIGHT - (self.PLAYER_W + self.hitbox_width)//2)

    def animation(self):

        if not self.stop_animation:

            cooldown = self.cooldown

            if self.dx == 0 and not self.atk1_animation and not self.atk2_animation and not self.takehit_animation and not self.death_animation:
                self.update_action(0)

            if self.dy < 0:
                cooldown = 150
                self.update_action(2)
            
            if self.dy > 0:
                cooldown = 100
                self.update_action(3)

            if self.atk1_animation and self.dx == 0:
                self.update_action(4)
                if self.frame >= len(self.animations[self.direction][self.action]) - 1:
                    self.action = 0
                    self.frame = 0
                    self.atk1_animation = False
            
            if self.atk2_animation and self.dx == 0:
                self.update_action(5)
                if self.frame >= len(self.animations[self.direction][self.action]) - 1:
                    self.action = 0
                    self.frame = 0
                    self.atk2_animation = False

            if self.takehit_animation and self.is_alive:
                self.update_action(6)
                if self.frame >= len(self.animations[self.direction][self.action]) - 1:
                    self.action = 0
                    self.frame = 0
                    self.takehit_animation = False

            if self.death_animation:
                self.update_action(7)
                if self.frame >= len(self.animations[self.direction][self.action]) - 1:
                    self.frame = len(self.animations[self.direction][self.action]) - 1
                    self.stop_animation = True

            if self.time - self.last_animation_time > cooldown:
                self.last_animation_time = self.time
                self.frame += 1

            if self.frame >= len(self.animations[self.direction][self.action]) and self.action != 7:
                self.frame = 0

    
    def update_action(self, new_action: int):  
        if self.action != new_action:
            self.action = new_action
            self.frame = 0
            self.last_animation_time = pygame.time.get_ticks()


    def handle_player_events(self, events):

        if not self.takehit_animation and self.is_alive:
            
            keys = pygame.key.get_pressed()

            # move right
            if keys[self.controls["right"][self.player_number]]:
                if self.on_ground:
                    self.action = 1
                
                if self.direction == 0:
                    self.direction = 1
                    self.frame = 0
                
                else:
                    self.dx = RUNNING_SPEED

            # move left
            elif keys[self.controls["left"][self.player_number]]:
                if self.on_ground:
                    self.action = 1
                
                if self.direction == 1:
                    self.direction = 0
                    self.frame = 0
                
                else:
                    self.dx = -RUNNING_SPEED

            else:
                self.dx = 0

            for event in events:
                if event.type == pygame.KEYDOWN:
                
                    if self.on_ground:

                        # jump
                        if event.key == self.controls["jump"][self.player_number]:
                            self.dy = JUMP_SPEED

                        if not self.atk1_animation and not self.atk2_animation:

                            # atk 1
                            if event.key == self.controls["atk1"][self.player_number] and self.can_use_atk1:
                                self.atk1_animation = True
                                self.last_atk1_time = self.time
                                self.atk1_has_hit = False

                            # atk 2
                            if event.key == self.controls["atk2"][self.player_number] and self.can_use_atk2:
                                self.atk2_animation = True
                                self.last_atk2_time = self.time
                                self.atk2_has_hit = False


    def update_attack_hitboxes(self):
        self.atk1_hitbox = pygame.Rect(0, 0, 0, 0)
        self.atk2_hitbox = pygame.Rect(0, 0, 0, 0)

        if self.action == 4 and self.frame == self.atk1_hitframe and not self.atk1_has_hit:
            self.atk1_hitbox = pygame.Rect(
                self.atk1_x[self.direction],
                self.atk1_y,
                self.atk1_width,
                self.atk1_height
            )
            self.atk1_has_hit = True

        if self.action == 5 and self.frame == self.atk2_hitframe and not self.atk2_has_hit:
            self.atk2_hitbox = pygame.Rect(
                self.atk2_x[self.direction],
                self.atk2_y,
                self.atk2_width,
                self.atk2_height
            )
            self.atk2_has_hit = True


    def player_hit(self, enemy: Player):
        if self.atk1_hitbox.colliderect(enemy.hitbox):
            enemy.health -= self.atk1_damage
            enemy.takehit_animation = True
            if enemy.health <= 0:
                enemy.death_animation = True

        if self.atk2_hitbox.colliderect(enemy.hitbox):
            enemy.health -= self.atk2_damage
            enemy.takehit_animation = True
            if enemy.health <= 0:
                enemy.death_animation = True

    def enter_stage(self, stage: Map):
        self.ground_level = stage.ground_level

    def get_location(self):
        return (self.x, self.y)

    def get_health_percentage(self):
        return self.health / MAX_HEALTH
    
    def get_atk1_recharge_percentage(self):
        return (self.time - self.last_atk1_time) / self.atk1_cooldown
    
    def get_atk2_recharge_percentage(self):
        return (self.time - self.last_atk2_time) / self.atk2_cooldown

    @property
    def is_alive(self):
        return self.health > 0

    @property
    def can_use_atk1(self):
        return self.time - self.last_atk1_time > self.atk1_cooldown
    
    @property
    def can_use_atk2(self):
        return self.time - self.last_atk2_time > self.atk2_cooldown
        
    @property
    def on_ground(self):
        return (self.hitbox_y + self.hitbox_height) == self.ground_level     
