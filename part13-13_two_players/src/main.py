# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Gracz 1 (strzałki) – lewy robot
x1 = 50
y1 = 240 - height // 2

# Gracz 2 (WASD) – prawy robot
x2 = 590 - width
y2 = 240 - height // 2

speed = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Klawisze gracza 1 (strzałki)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1 -= speed
        if x1 < 0:
            x1 = 0
    if keys[pygame.K_RIGHT]:
        x1 += speed
        if x1 + width > 640:
            x1 = 640 - width
    if keys[pygame.K_UP]:
        y1 -= speed
        if y1 < 0:
            y1 = 0
    if keys[pygame.K_DOWN]:
        y1 += speed
        if y1 + height > 480:
            y1 = 480 - height

    # Klawisze gracza 2 (WASD)
    if keys[pygame.K_a]:
        x2 -= speed
        if x2 < 0:
            x2 = 0
    if keys[pygame.K_d]:
        x2 += speed
        if x2 + width > 640:
            x2 = 640 - width
    if keys[pygame.K_w]:
        y2 -= speed
        if y2 < 0:
            y2 = 0
    if keys[pygame.K_s]:
        y2 += speed
        if y2 + height > 480:
            y2 = 480 - height

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    clock.tick(60)