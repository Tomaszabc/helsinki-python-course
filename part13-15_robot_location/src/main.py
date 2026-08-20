# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Losowa pozycja początkowa
x = random.randint(0, 640 - width)
y = random.randint(0, 480 - height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Sprawdź, czy kliknięto na robocie
            mouse_x, mouse_y = event.pos
            if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                # Przenieś robota w nowe losowe miejsce
                x = random.randint(0, 640 - width)
                y = random.randint(0, 480 - height)

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)