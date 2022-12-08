import time
import pygame


class Robot(pygame.sprite.Sprite):
    STARTING_POSITION = (20, 250)
    SIZE = (64, 64)
    image = pygame.image.load('resources/robot_f.png')
    MOVE_DIST = 7
    SCREEN_DIM = 600, 500
    MOMENTUM = 0
    def __init__(self):
        super().__init__()
        self.image = Robot.image
        self.rect = pygame.Rect((0, 0), Robot.SIZE)
        self.rect.center = Robot.STARTING_POSITION
    
    def reset_position(self):
        self.rect.center = Robot.STARTING_POSITION

    def jump(self):
        if self.rect.top >= 0:
            self.rect.centery -= Robot.MOVE_DIST + self.MOMENTUM
        self.MOMENTUM += 0.05
