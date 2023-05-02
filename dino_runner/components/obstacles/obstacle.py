import pygame
import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        #Image is a list
        self.image = image
        #Obstacle_type is an index
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
    

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()
            print("Objeto eliminado")

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type],(self.rect.x, self.rect.y))
