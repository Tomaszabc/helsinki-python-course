# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Parametry okręgu
center_x = 320
center_y = 240
radius = 150
num_robots = 10

clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    # Rysuj 10 robotów na okręgu
    for i in range(num_robots):
        # Kąt dla każdego robota (przesunięty o 36 stopni = 2π/10)
        robot_angle = angle + i * (2 * math.pi / num_robots)
        
        x = center_x + radius * math.cos(robot_angle) - width / 2
        y = center_y + radius * math.sin(robot_angle) - height / 2
        
        window.blit(robot, (x, y))

    pygame.display.flip()
    
    # Zwiększ kąt dla następnej klatki
    angle += 0.02
    clock.tick(60)