import pygame
import random   # for random functions
import sys
import time

#bg_color = green
MAX_X = 1366
MAX_Y = 768
MAX_SNOW = 100
SNOW_SIZE = 40


# to initialize new Class "SNOW"
class Snow():
    def __init__(self, x, y):   # to define class params
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.img_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.img_filename).convert()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):   # to define movement function in class
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)

        i = random.randint(1, 4)
        if i == 1:   # move right
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:   # move left
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X
        elif i == 3:   # move 2 right
            self.x += 2
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 4:   # move 2 left
            self.x -= 2
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X





    def draw_snow(self):   # to define draw_snow function in class
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(max_snow, snowfall):   # to define function to create new images in random pos-s
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_X)   # random X coordinate for each image
        yy = random.randint(0, MAX_Y)  # random Y coordinate for each image
        snowfall.append(Snow(xx, yy))   # to append object Snow (random images with random coord-s) to snowfall list


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


#   __________MAIN____________

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 250, 0)
snowfall = []

initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.012)
    pygame.display.flip()



