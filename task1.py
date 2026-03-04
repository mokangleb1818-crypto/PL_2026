import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cat Scene")

# Цвета
WALL = (102, 80, 0)
FLOOR = (140, 110, 0)
CAT = (196, 114, 52)
EAR_IN = (230, 180, 150)
GREEN = (140, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_FRAME = (180, 220, 200)
GLASS = (120, 180, 200)
GRAY = (160, 160, 160)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Фон
    screen.fill(WALL)
    pygame.draw.rect(screen, FLOOR, (0, 350, 800, 250))

    # Окно
    pygame.draw.rect(screen, WINDOW_FRAME, (500, 50, 250, 200))
    pygame.draw.rect(screen, GLASS, (520, 70, 90, 70))
    pygame.draw.rect(screen, GLASS, (640, 70, 90, 70))
    pygame.draw.rect(screen, GLASS, (520, 150, 90, 80))
    pygame.draw.rect(screen, GLASS, (640, 150, 90, 80))

    # Тело кота
    pygame.draw.ellipse(screen, CAT, (200, 300, 400, 150))
    pygame.draw.ellipse(screen, CAT, (120, 280, 180, 120))  # голова
    pygame.draw.ellipse(screen, CAT, (500, 320, 150, 100))  # задняя лапа
    pygame.draw.ellipse(screen, CAT, (520, 380, 70, 120))   # лапа вниз
    pygame.draw.ellipse(screen, CAT, (250, 350, 150, 60))   # передняя лапа

    # Хвост
    pygame.draw.ellipse(screen, CAT, (580, 300, 250, 100))

    # Уши
    pygame.draw.polygon(screen, CAT, [(140, 290), (170, 250), (200, 280)])
    pygame.draw.polygon(screen, CAT, [(240, 280), (270, 250), (260, 300)])
    pygame.draw.polygon(screen, EAR_IN, [(150, 285), (170, 260), (185, 280)])
    pygame.draw.polygon(screen, EAR_IN, [(245, 280), (260, 260), (255, 290)])

    # Глаза
    pygame.draw.ellipse(screen, GREEN, (160, 300, 40, 30))
    pygame.draw.ellipse(screen, GREEN, (210, 300, 40, 30))
    pygame.draw.line(screen, BLACK, (180, 300), (180, 330), 3)
    pygame.draw.line(screen, BLACK, (230, 300), (230, 330), 3)

    # Нос
    pygame.draw.polygon(screen, BLACK, [(200, 330), (190, 340), (210, 340)])
    pygame.draw.line(screen, BLACK, (200, 340), (200, 350), 2)

    # Усы
    pygame.draw.line(screen, BLACK, (140, 335), (90, 330), 1)
    pygame.draw.line(screen, BLACK, (140, 345), (90, 350), 1)
    pygame.draw.line(screen, BLACK, (260, 335), (310, 330), 1)
    pygame.draw.line(screen, BLACK, (260, 345), (310, 350), 1)

    # Клубок
    pygame.draw.circle(screen, GRAY, (500, 500), 60)
    pygame.draw.arc(screen, BLACK, (460, 460, 80, 80), 0, 3.14, 1)
    pygame.draw.arc(screen, BLACK, (450, 470, 100, 60), 0, 3.14, 1)
    pygame.draw.arc(screen, BLACK, (470, 450, 60, 100), 1.5, 4.7, 1)

    pygame.display.flip()
    clock.tick(60)