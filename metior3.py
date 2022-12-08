import pygame, random

class metior3(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/metior2.png')
    RIGHT_IMAGE = pygame.image.load('resources/metior2.png')
    STARTING_POSITION = (400, random.randint(75, 500))
    SIZE = (75, 25)
    SCREEN_DIM = 600, 600
    move_dist = 6
    score = 0


    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = metior3.LEFT_IMAGE if direction == 'Left' else metior3.RIGHT_IMAGE
        self.rect = pygame.Rect((-100, random.randint(75, 550)), metior3.SIZE)
        self.rect.center = metior3.STARTING_POSITION
        self.direction = direction
    

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= metior3.move_dist
            if self.rect.right <= 0:
                self.score += 1
                self.rect = pygame.Rect((-100, random.randint(0, 550)), metior3.SIZE)
                self.rect.centerx = metior3.SCREEN_DIM[0] + (metior3.SIZE[0] / 2)
        else:
            self.rect.centerx += metior3.move_dist
            if self.rect.left >= metior3.SCREEN_DIM[0]:
                self.rect.centerx = - metior3.SIZE[0] / 2