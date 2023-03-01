import pygame
import random

k = 0
vy = 1
vx = 1
a = random.randint(1, 1000)


def enemygen():
    enemy = pygame.image.load("data/W2.png")
    x1, y1 = 530, 0
    return [enemy, x1, y1]



