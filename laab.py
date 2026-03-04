import pygame
import sys

pygame.init()

# Размер окна
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Angry Smile")

# Цвета
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GRAY)

    # Голова
    pygame.draw.circle(screen, YELLOW, (250, 250), 120)

    # Глаза (красные круги)
    pygame.draw.circle(screen, RED, (210, 220), 25)
    pygame.draw.circle(screen, RED, (290, 220), 25)

    # Зрачки
    pygame.draw.circle(screen, BLACK, (210, 220), 10)
    pygame.draw.circle(screen, BLACK, (290, 220), 10)

    # Брови
    pygame.draw.line(screen, BLACK, (160, 180), (240, 210), 10)
    pygame.draw.line(screen, BLACK, (340, 180), (260, 210), 10)

    # Рот
    pygame.draw.rect(screen, BLACK, (200, 290, 100, 20))

    pygame.display.flip()
    clock.tick(60)