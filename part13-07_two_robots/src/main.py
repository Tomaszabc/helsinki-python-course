# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Pozycje początkowe
x1 = 0
y1 = 50
speed1 = 1

x2 = 0
y2 = 150
speed2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Aktualizuj pozycje
    x1 += speed1
    x2 += speed2

    # Odbijanie od krawędzi
    if x1 + width > 640 or x1 < 0:
        speed1 = -speed1
    if x2 + width > 640 or x2 < 0:
        speed2 = -speed2

    # Rysuj
    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)