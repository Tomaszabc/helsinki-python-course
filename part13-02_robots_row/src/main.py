# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

total_width = 10 * width
start_x = (640 - total_width) // 2

# Rysuj 10 robotów obok siebie
for i in range(10):
    window.blit(robot, (start_x + i * width, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()