# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Lista robotów: [x, y, prędkość_pozioma, stan]
# stan: 0 = spada, 1 = porusza się w poziomie
robots = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Dodaj nowego robota z prawdopodobieństwem 1/30
    if random.randint(1, 30) == 1:
        x = random.randint(0, 640 - width)
        y = -height  # Pojawia się nad ekranem
        robots.append([x, y, 0, 0])  # [x, y, speed_x, state]

    # Aktualizuj pozycje robotów
    for robot_data in robots:
        # State 0: spada w dół
        if robot_data[3] == 0:
            robot_data[1] += 2  # Prędkość spadania

            # Jeśli dotknął podłoża, zmień stan
            if robot_data[1] + height >= 480:
                robot_data[1] = 480 - height  # Ustaw na ziemi
                robot_data[3] = 1  # Zmień stan na "chodzenie"
                robot_data[2] = random.choice([-2, 2])  # Losowy kierunek

        # State 1: porusza się w poziomie
        else:
            robot_data[0] += robot_data[2]

    # Usuń roboty, które wyszły poza ekran (w poziomie)
    robots = [r for r in robots if 0 <= r[0] <= 640]

    # Rysuj
    window.fill((0, 0, 0))
    for robot_data in robots:
        window.blit(robot, (robot_data[0], robot_data[1]))

    pygame.display.flip()
    clock.tick(60)