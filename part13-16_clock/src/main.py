# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

# Załaduj tło zegara (jeśli masz)
# clock_face = pygame.image.load("clock.png")

# Parametry zegara
center_x = 320
center_y = 240
radius = 200
clock_radius = 180

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Pobierz aktualny czas
    now = datetime.datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    # Oblicz kąty wskazówek (w radianach)
    # 360 stopni = 12 godzin, 60 minut, 60 sekund
    second_angle = (seconds / 60) * 2 * math.pi - math.pi / 2
    minute_angle = (minutes / 60) * 2 * math.pi - math.pi / 2
    hour_angle = (hours / 12 + minutes / 720) * 2 * math.pi - math.pi / 2

    # Długości wskazówek
    hour_length = clock_radius * 0.5
    minute_length = clock_radius * 0.7
    second_length = clock_radius * 0.8

    # Wyczyść ekran
    window.fill((0, 0, 0))

    # Rysuj tarczę zegara (okrąg)
    pygame.draw.circle(window, (200, 200, 200), (center_x, center_y), radius, 2)

    # Rysuj kropki na godzinach
    for i in range(12):
        angle = (i / 12) * 2 * math.pi - math.pi / 2
        x = center_x + (radius - 20) * math.cos(angle)
        y = center_y + (radius - 20) * math.sin(angle)
        pygame.draw.circle(window, (200, 200, 200), (int(x), int(y)), 5)

    # Rysuj wskazówkę godzinową
    hour_x = center_x + hour_length * math.cos(hour_angle)
    hour_y = center_y + hour_length * math.sin(hour_angle)
    pygame.draw.line(window, (255, 255, 255), (center_x, center_y), (hour_x, hour_y), 6)

    # Rysuj wskazówkę minutową
    minute_x = center_x + minute_length * math.cos(minute_angle)
    minute_y = center_y + minute_length * math.sin(minute_angle)
    pygame.draw.line(window, (200, 200, 200), (center_x, center_y), (minute_x, minute_y), 4)

    # Rysuj wskazówkę sekundową
    second_x = center_x + second_length * math.cos(second_angle)
    second_y = center_y + second_length * math.sin(second_angle)
    pygame.draw.line(window, (255, 0, 0), (center_x, center_y), (second_x, second_y), 2)

    # Rysuj środek zegara
    pygame.draw.circle(window, (255, 255, 255), (center_x, center_y), 8)

    pygame.display.flip()
    clock.tick(60)