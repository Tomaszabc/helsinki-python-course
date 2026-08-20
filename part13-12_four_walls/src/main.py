# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 0
y = 480 - height

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
                if x < 0:
                    x = 0
            if event.key == pygame.K_RIGHT:
                x += 10
                if x + width > 640:
                    x = 640 - width
            if event.key == pygame.K_DOWN:
                y += 10
                if y + height > 480:
                    y = 480 - height
            if event.key == pygame.K_UP:
                y -= 10
                if y < 0:
                    y = 0

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()