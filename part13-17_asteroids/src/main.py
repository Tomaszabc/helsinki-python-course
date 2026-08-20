# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
asteroid = pygame.image.load("rock.png")  # Jeśli nie masz, użyj kółka

# Użyj kółka jeśli nie masz asteroid.png
# asteroid = pygame.Surface((30, 30))
# asteroid.fill((200, 200, 200))

width = robot.get_width()
height = robot.get_height()

asteroid_width = asteroid.get_width() if asteroid else 30
asteroid_height = asteroid.get_height() if asteroid else 30

# Gracz
x = 320 - width // 2
y = 480 - height - 20
speed = 5

# Asteroidy
asteroids = []
score = 0
game_over = False

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if not game_over:
        # Sterowanie robotem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
            if x < 0:
                x = 0
        if keys[pygame.K_RIGHT]:
            x += speed
            if x + width > 640:
                x = 640 - width

        # Dodawanie asteroid
        if random.randint(1, 30) == 1:
            asteroid_x = random.randint(0, 640 - asteroid_width)
            asteroid_y = -asteroid_height
            asteroids.append([asteroid_x, asteroid_y, random.randint(1, 3)])  # x, y, speed_y

        # Aktualizacja asteroid
        for a in asteroids[:]:
            a[1] += a[2]  # Spadanie

            # Sprawdzenie kolizji z robotem
            if (a[0] < x + width and a[0] + asteroid_width > x and
                a[1] < y + height and a[1] + asteroid_height > y):
                asteroids.remove(a)
                score += 1
                continue

            # Sprawdzenie, czy asteroida spadła poniżej ekranu
            if a[1] > 480:
                game_over = True

    # Rysowanie
    window.fill((0, 0, 0))

    # Punkty
    text = font.render(f"Points: {score}", True, (255, 255, 255))
    window.blit(text, (10, 10))

    # Asteroidy
    for a in asteroids:
        window.blit(asteroid, (a[0], a[1]))

    # Robot
    window.blit(robot, (x, y))

    # Game Over
    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        window.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)