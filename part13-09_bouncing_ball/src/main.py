# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

# Pozycja początkowa
x = 100
y = 100

# Prędkość (kierunek)
speed_x = 3
speed_y = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Aktualizuj pozycję
    x += speed_x
    y += speed_y

    # Odbijanie od krawędzi
    if x + width > 640 or x < 0:
        speed_x = -speed_x
    if y + height > 480 or y < 0:
        speed_y = -speed_y

    # Rysuj
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)