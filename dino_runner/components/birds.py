import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Birds(Obstacle):
    def __init__(self,image):
        bird_heights = [260,220,170]
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.choice(bird_heights)