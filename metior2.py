import pygame, random

class metior2(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/metior.png')
    RIGHT_IMAGE = pygame.image.load('resources/metior.png')
    STARTING_POSITION = (400, random.randint(75, 500))
    SIZE = (75, 25)
    SCREEN_DIM = 600, 600
    move_dist = 4
    score = 0


    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = metior2.LEFT_IMAGE if direction == 'Left' else metior2.RIGHT_IMAGE
        self.rect = pygame.Rect((-100, random.randint(75, 550)), metior2.SIZE)
        self.rect.center = metior2.STARTING_POSITION
        self.direction = direction
    

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= metior2.move_dist
            if self.rect.right <= 0:
                self.score += 1
                self.rect = pygame.Rect((-100, random.randint(0, 550)), metior2.SIZE)
                self.rect.centerx = metior2.SCREEN_DIM[0] + (metior2.SIZE[0] / 2)
        else:
            self.rect.centerx += metior2.move_dist
            if self.rect.left >= metior2.SCREEN_DIM[0]:
                self.rect.centerx = - metior2.SIZE[0] / 2
