import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вариант 4")

# Цвета
WALL = (110, 85, 0)
CAT = (195, 110, 50)
CAT_DARK = (150, 80, 30)
EAR_IN = (230, 180, 160)
GREEN = (140, 200, 0)
BLUE = (130, 185, 210)
FRAME = (210, 235, 225)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_scene(screen):
    screen.fill(WALL)

    # --- ОКНО ---
    pygame.draw.rect(screen, FRAME, (520, 60, 240, 210))
    pygame.draw.rect(screen, BLUE, (550, 85, 80, 80))
    pygame.draw.rect(screen, BLUE, (650, 85, 80, 80))
    pygame.draw.rect(screen, BLUE, (550, 175, 80, 80))
    pygame.draw.rect(screen, BLUE, (650, 175, 80, 80))
    pygame.draw.line(screen, FRAME, (640, 60), (640, 270), 6)
    pygame.draw.line(screen, FRAME, (520, 165), (760, 165), 6)

    # --- ТЕЛО ---
    pygame.draw.ellipse(screen, CAT, (260, 310, 420, 170))
    pygame.draw.ellipse(screen, CAT_DARK, (260, 310, 420, 170), 2)

    # --- ХВОСТ ---
    pygame.draw.ellipse(screen, CAT, (640, 340, 260, 110))
    pygame.draw.ellipse(screen, CAT_DARK, (640, 340, 260, 110), 2)

    # --- ГОЛОВА ---
    pygame.draw.ellipse(screen, CAT, (130, 280, 200, 150))
    pygame.draw.ellipse(screen, CAT_DARK, (130, 280, 200, 150), 2)

    # --- УШИ ---
    pygame.draw.polygon(screen, CAT, [(150,260),(190,235),(170,295)])
    pygame.draw.polygon(screen, CAT_DARK, [(150,260),(190,235),(170,295)],2)

    pygame.draw.polygon(screen, CAT, [(270,260),(310,235),(290,295)])
    pygame.draw.polygon(screen, CAT_DARK, [(270,260),(310,235),(290,295)],2)

    # Внутренние уши
    pygame.draw.polygon(screen, EAR_IN, [(160,260),(185,245),(172,285)])
    pygame.draw.polygon(screen, EAR_IN, [(280,260),(305,245),(292,285)])

    # --- ГЛАЗА ---
    pygame.draw.ellipse(screen, GREEN, (165, 320, 45, 55))
    pygame.draw.ellipse(screen, GREEN, (235, 320, 45, 55))
    pygame.draw.ellipse(screen, BLACK, (185, 325, 12, 45))
    pygame.draw.ellipse(screen, BLACK, (255, 325, 12, 45))

    # Блики
    pygame.draw.circle(screen, WHITE, (195, 335), 6)
    pygame.draw.circle(screen, WHITE, (265, 335), 6)

    # --- НОС И РОТ ---
    pygame.draw.polygon(screen, CAT_DARK, [(220,360),(205,375),(235,375)])
    pygame.draw.line(screen, BLACK, (220,375),(220,390),2)
    pygame.draw.arc(screen, BLACK, (200,385,40,30), math.radians(200), math.radians(340),2)

    # --- УСЫ ---
    for i in range(3):
        pygame.draw.line(screen, BLACK, (150,360+i*8),(95,350+i*10),2)
        pygame.draw.line(screen, BLACK, (290,360+i*8),(345,350+i*10),2)

    # --- ЛАПЫ ---
    pygame.draw.ellipse(screen, CAT, (310, 390, 120, 60))
    pygame.draw.ellipse(screen, CAT_DARK, (310, 390, 120, 60),2)

    pygame.draw.ellipse(screen, CAT, (520, 360, 140, 110))
    pygame.draw.ellipse(screen, CAT_DARK, (520, 360, 140, 110),2)

    pygame.draw.ellipse(screen, CAT, (600, 430, 60, 110))
    pygame.draw.ellipse(screen, CAT_DARK, (600, 430, 60, 110),2)

    # --- КЛУБОК ---
    pygame.draw.ellipse(screen, GRAY, (460, 480, 150, 100))
    pygame.draw.ellipse(screen, BLACK, (460, 480, 150, 100), 2)

    # Линии ниток
    for i in range(5):
        pygame.draw.arc(screen, BLACK, (470+i*10, 500, 100, 60),
                        math.radians(180), math.radians(360), 1)

    # Нитка
    pygame.draw.arc(screen, GRAY, (350, 520, 150, 60),
                    math.radians(200), math.radians(360), 2)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_scene(screen)
    pygame.display.update()
    clock.tick(60)