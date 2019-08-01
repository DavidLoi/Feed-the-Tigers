##
# Create an Xavier themed classic game
# @author David Loi
# @course ICS3U1
# date 2018/06/16

import pygame

import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKYBLUE = (20, 220, 255)
GREEN = (10, 120, 40)
SAND = (225, 205, 175)
GRAY = (170, 180, 190)
DARK_GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
NAVY = (0, 0, 128)

pygame.init()

# Sprites lists
tiger_list = pygame.sprite.Group()
meat_list = pygame.sprite.Group()

words = 1
font = pygame.font.SysFont('Calaibri', 50, True, False)
alt_font = pygame.font.SysFont('Calibri', 100, True, False)

# Set the width and height of the screen [width, height]
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Feed the Tigers")

# Classes
class Tiger(pygame.sprite.Sprite):
    # Class for tiger
    # From "Sprite" class in Python

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BabyTiger.png").convert()
        self.rect = self.image.get_rect()
        self.change_x = " "
        self.image.set_colorkey(GREEN)

    def move(self):
        self.rect.x += self.change_x
        if self.rect.x > 800 or self.rect.x < -100:
            self.change_x = self.change_x * -1

    def reset_pos(self):
        x = random.randrange(1,3)
        if x == 1:
            self.rect.x = -100
            self.rect.y = random.randrange(200, 320)
            self.change_x = random.randrange(1, 5)
        if x == 2:
            self.rect.x = 800
            self.rect.y = random.randrange(200, 320)
            self.change_x = random.randrange(-5, -1)

class Meat(pygame.sprite.Sprite):
    # Class for meat
    # From "Sprite" class in Python
    # Used to hit tigers

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Meat.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 545
        self.change_x = 0
        self.change_y = 0

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def reset_pos(self):
        self.rect.x = 375
        self.rect.y = 545
        self.change_x = 0
        self.change_y = 0

class Tracker():
    # Class for tracker
    # Determines how far meat travels, and the speed

    def __init__(self):
        self.x = 400
        self.y = 560

        self.xspeed = 0
        self.yspeed = 0

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > 800:
            self.xspeed = self.xspeed * -1
            self.yspeed = self.yspeed * -1

        if self.y < 0 or self.y > 560:
            self.xspeed = self.xspeed * -1
            self.yspeed = self.yspeed * -1

    def reset_pos(self):
        self.x = 400
        self.y = 560

class Arrow():
    # Class for arrow
    # Used to aim meat

    def __init__(self):
        self.x = 400
        self.y = 410
        self.changex = 0

    def move(self):
        if arrow.x + arrow.changex >= 150 and arrow.x + arrow.changex <= 650:
            self.x += self.changex

    def draw(self):
        pygame.draw.line(screen, BLACK, [400, 560], [self.x, self.y], 10)

def startScreen():
    # Starting screen

    screen.fill(NAVY)
    name = alt_font.render("FEED THE TIGERS", True, YELLOW)
    start = font.render("PRESS ENTER TO CONTINUE", True, YELLOW)
    screen.blit(name, [50, 100])
    screen.blit(start, [100, 400])

def gameOver():
    # Changes to game over screen

    game_over = alt_font.render("GAME OVER", True, YELLOW)
    final_score = alt_font.render("SCORE: " + str(score_num), True, YELLOW)
    play_again = font.render("PRESS ENTER TO PLAY AGAIN", True, YELLOW)
    screen.fill(NAVY)
    screen.blit(game_over, [150, 100])
    screen.blit(final_score, [150, 300])
    screen.blit(play_again, [100, 500])

for i in range(5):
    tiger = Tiger()
    tiger.rect.x = random.randrange(0, 700)
    tiger.rect.y = random.randrange(200, 335)
    tiger.change_x = random.randrange(-5, 5)
    tiger.image.set_colorkey(GREEN)
    tiger_list.add(tiger)

meat_move = 0
meat = Meat()
meat_list.add(meat)
arrow = Arrow()

tracker = Tracker()

score_num = 0

score = font.render("Score: " + str(score_num), True, YELLOW)

# Loop until the user clicks the close button.
done = False

timer = 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    play = False
    score_num = 0
    meat.reset_pos()
    tracker.reset_pos()
    arrow.draw()

    while not play:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = True
                    ticks = pygame.time.get_ticks()

        startScreen()
        pygame.display.flip()

    while play:

        seconds = int((pygame.time.get_ticks() - ticks)/1000)
        timer = 10 - seconds
        time = font.render("Time left: " + str(timer), True, YELLOW)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    arrow.changex = -5
                if event.key == pygame.K_RIGHT:
                    arrow.changex = 5
                if event.key == pygame.K_SPACE:
                    tracker.reset_pos()
                    tracker.xspeed = trackerxspeed
                    tracker.yspeed = trackeryspeed
                    tracker.move()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    arrow.changex = 0
                    arrow.changey = 0
                if event.key == pygame.K_SPACE:
                    tracker.xspeed = 0
                    tracker.yspeed = 0
                    meat.change_x = int((tracker.x - 400)/50)
                    meat.change_y = int((tracker.y - 560)/50)
                    meat_move = 1
                    draw = 0

        #Color screen SKYBLUE
        screen.fill(SKYBLUE)

        #Drawings
        #Background
        pygame.draw.polygon(screen, DARK_GRAY, [[400, 200], [450, 80], [500, 200]])
        pygame.draw.polygon(screen, BLACK, [[400, 200], [450, 80], [500, 200]], 1)
        pygame.draw.polygon(screen, DARK_GRAY, [[-30, 200], [50, 40], [ 130, 200]])
        pygame.draw.polygon(screen, BLACK, [[-30, 200], [50, 40], [ 130, 200]], 1)
        pygame.draw.polygon(screen, DARK_GRAY, [[80, 200], [180, 50], [280, 200]])
        pygame.draw.polygon(screen, BLACK, [[80, 200], [180, 50], [280, 200]], 1)
        pygame.draw.polygon(screen, DARK_GRAY, [[690, 200], [770, 70], [850, 200]])
        pygame.draw.polygon(screen, BLACK, [[690, 200], [770, 70], [850, 200]], 1)
        pygame.draw.polygon(screen, DARK_GRAY, [[120, 200], [300, 30], [480, 200]])
        pygame.draw.polygon(screen, BLACK, [[120, 200], [300, 30], [480, 200]], 2)
        pygame.draw.polygon(screen, DARK_GRAY, [[430, 200], [580, 0], [730, 200]])
        pygame.draw.polygon(screen, BLACK, [[430, 200], [580, 0], [730, 200]], 2)

        x_offset = 0
        for x_offset in range(0, 800, 200):
            pygame.draw.polygon(screen, GRAY, [[x_offset, 200], [x_offset + 100, 100],
            [x_offset + 200, 200]])
            pygame.draw.polygon(screen, BLACK, [[x_offset, 200], [x_offset + 100, 100],
            [x_offset + 200, 200]], 3)

        pygame.draw.rect(screen, GREEN, [0, 200, 800, 200])
        pygame.draw.rect(screen, SAND, [0, 400, 800, 200])

        #Aiming line
        arrow.move()
        arrow.draw()

        #Tracker
        trackerxspeed = int((arrow.x - 400)/10)
        trackeryspeed = int((arrow.y - 560)/10)
        tracker.move()

        #Meat
        if meat_move == 1:
            meat.move()
            if meat.rect.x == tracker.x or meat.rect.y <= tracker.y:
                meat.reset_pos()

        for tiger in tiger_list:
            tiger.move()

        tiger_hit_list = pygame.sprite.spritecollide(meat, tiger_list, True)
        for tiger in tiger_hit_list:
            score_num += 100
            score = font.render("Score: " + str(score_num), True, YELLOW)
            tiger_list.add(tiger)
            tiger.reset_pos()

        tiger_list.draw(screen)
        meat_list.draw(screen)

        screen.blit(time, [8,6])
        screen.blit(score, [8, 560])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

        if timer <= 0:
            play = False

    # Close the window and quit.
    while not play:

        gameOver()
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = True