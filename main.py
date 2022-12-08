import random, pygame, sys, math
from robot import Robot
from metior1 import metior1
from metior2 import metior2
from metior3 import metior3 as Metior3

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (21, 237, 32)
YELLOW = (237, 233, 21)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 255)
robot = Robot()
metior1 = metior1(metior1.STARTING_POSITION, 'Left')
metior2 = metior2(metior2.STARTING_POSITION, 'Left')
metior3 = Metior3(Metior3.STARTING_POSITION, 'Left')
pygame.init()
ICON = pygame.image.load("resources/robot_logo.png")
score_mode = False
pygame.display.set_icon(ICON)
# music_file = pygame.mixer.Sound("resources/backround music.mp3")
# music_file.play()

def play(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

background_music = "resources/background_music.ogg"
play(background_music)
pygame.mixer.music.set_volume(0.3)
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Robo Flyer')
CLOCK = pygame.time.Clock()
FPS = 60
FONT = pygame.font.Font('resources/font.ttf', 20)
MENU_BIG = pygame.font.Font('resources/font.ttf', 60)
MENU_MED = pygame.font.Font('resources/font.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/font.ttf', 15)
MENU_IMAGE = pygame.image.load('resources/menu_robot.png')
END_IMAGE = pygame.image.load('resources/dead robot.png')
level = 0
START_MENU = True
END_MENU = False
boss_mode = False
score = 0
wait_timer = 0
momentum = 0
current_best = 0
high_score = 0
score_file = open("score.txt", "r+")
win_music_play = 1
try:
    high_score = int(score_file.readline().strip())
except:
    print("No high score, reseting")
    score_file.truncate(0)
    score_file.seek(0)
    score_file.write(str(0))
best_score = high_score
#background code
scroll = 0
window = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = pygame.image.load('resources/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))
boss_music_play = 1
tiles = math.ceil(600  /BACKGROUND.get_width()) + 1
BACKGROUND_MENU = pygame.image.load('resources/menu_image.png')
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU,(WIDTH,HEIGHT))
while(True):
    score = metior1.score + metior2.score + metior3.score
    metior2.move()
    metior1.move()
    metior3.move()
    pygame.display.update()
    # pygame.mixer.music.load("resources/background music.ogg")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    momentum += 0.1
    robot.rect.centery += 4.3 + momentum
    robot.update()
    while START_MENU:
        CLOCK.tick(15)
        window.blit(BACKGROUND_MENU,(0,0))
        name = MENU_BIG.render('ROBO FLYER', True, WHITE)
        instructions = MENU_SMALL.render('Press Space To Start', True, WHITE)
        SCREEN.blit(name, (75, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 260))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False

    while END_MENU:
        CLOCK.tick(15)
        window.blit(BACKGROUND_MENU,(0,0))
        thx = MENU_MED.render('You Died', True, RED)
        scores = MENU_MED.render('Your Final Score: %d' % (score), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(END_IMAGE, (145, 260))
        SCREEN.blit(instructions, (130, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if high_score > best_score:
                    score_file.seek(0)
                    score_file.truncate(0)
                    score_file.write(str(high_score))
                score_file.close()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play(background_music)
                    END_MENU = False
                    score_mode = False
                    current_best = 0
                    score = 0
                    metior1.score = 0
                    metior2.score = 0
                    metior3.score = 0
        pygame.display.update()

        pygame.display.update()

    CLOCK.tick(FPS)
    window.blit(BACKGROUND,(0,0))
    if END_MENU == False:
        SCREEN.blit(robot.image, (robot.rect.x, robot.rect.y))
        SCREEN.blit(metior1.image, metior1.rect)
        SCREEN.blit(metior2.image, metior2.rect)
        SCREEN.blit(metior3.image, metior3.rect)
    if robot.rect.bottom >= 600:
        END_MENU = True
        robot.reset_position()
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_SPACE]:
        robot.jump()
        robot.image = pygame.image.load('resources/robot_p.png')
        momentum = 0
    else:
        robot.image = pygame.image.load('resources/robot_f.png')
        robot.MOMENTUM = 0
    if robot.rect.colliderect(metior1.rect) or robot.rect.colliderect(metior2.rect) or robot.rect.colliderect(metior3.rect):
            END_MENU = True
            robot.reset_position()
            metior2.rect = pygame.Rect((-100, random.randint(0, 550)), metior1.SIZE)
            if metior2.rect.colliderect(metior1.rect):
                metior2.rect = pygame.Rect((-100, random.randint(0, 550)), metior1.SIZE)
            metior1.rect = pygame.Rect((-100, random.randint(0, 550)), metior1.SIZE)
            if metior1.rect.colliderect(metior2.rect):
                metior1.rect = pygame.Rect((-100, random.randint(0, 550)), metior1.SIZE)
            metior3.rect = pygame.Rect((-100, random.randint(0, 550)), metior3.SIZE)
            if metior3.rect.colliderect(metior3.rect):
                metior3.rect = pygame.Rect((-100, random.randint(0, 550)), metior3.SIZE)
    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))

    pygame.display.update()


    
    
    if score + current_best >= high_score:
        high_score = score + current_best

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if high_score > best_score:
                score_file.seek(0)
                score_file.truncate(0)
                score_file.write(str(high_score))
            score_file.close()
            pygame.mixer.music.unload()
            sys.exit()
    pygame.display.flip()

