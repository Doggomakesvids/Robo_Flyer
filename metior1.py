import pygame, random
class metior1(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/metior1.png')
    RIGHT_IMAGE = pygame.image.load('resources/metior1.png')
    STARTING_POSITION = (300, random.randint(75, 500))
    SIZE = (75, 25)
    SCREEN_DIM = 600, 600
    move_dist = 3
    score = 0

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = metior1.LEFT_IMAGE if direction == 'Left' else metior1.RIGHT_IMAGE
        self.rect = pygame.Rect((-100, random.randint(75, 550)), metior1.SIZE)
        self.rect.center = metior1.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= metior1.move_dist
            if self.rect.right <= 0:
                self.score += 1
                self.rect = pygame.Rect((-100, random.randint(0, 550)), metior1.SIZE)
                self.rect.centerx = metior1.SCREEN_DIM[0] + (metior1.SIZE[0] / 2)
        else:
            self.rect.centerx += metior1.move_dist
            if self.rect.left >= metior1.SCREEN_DIM[0]:
                self.rect.centerx = - metior1.SIZE[0] / 2
