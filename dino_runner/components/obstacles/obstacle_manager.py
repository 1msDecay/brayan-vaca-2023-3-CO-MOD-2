import pygame
import random
from dino_runner.components.cactus import Cactus
from dino_runner.components.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.next_obstacle = []

    def update(self, game):
        # Add obstacle to list
        if len(self.obstacles) == 0:
            cactus_small = Cactus(SMALL_CACTUS)
            cactus_large = Cactus(LARGE_CACTUS)
            birds = Birds(BIRD)
            self.obstacles.append(cactus_small)
            self.obstacles.append(cactus_large)
            self.obstacles.append(birds)
            #self.next_obstacle.extend(cactus_small)
            #self.next_obstacle.extend(cactus_large)
            #self.next_obstacle.extend(birds)
            #self.obstacles.append(random.choice(self.next_obstacle))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            #pygame.time.delay(100)
            #print(game.player.dino_rect.colliderect(obstacle.rect))
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)