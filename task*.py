import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Cats Scene")

# Цвета
WALL = (102, 80, 0)
FLOOR = (140, 110, 0)
FRAME = (190, 230, 210)
GLASS = (120, 180, 200)
ORANGE = (196, 114, 52)
GRAY_CAT = (120, 110, 100)
GREEN = (140, 200, 0)
BLUE = (50, 200, 255)
YARN = (170, 170, 170)
BLACK = (0, 0, 0)
EAR_IN = (230, 180, 150)

clock = pygame.time.Clock()


def draw_window(x, y):
    pygame.draw.rect(screen, FRAME, (x, y, 220, 160))
    pygame.draw.rect(screen, GLASS, (x+15, y+15, 85, 55))
    pygame.draw.rect(screen, GLASS, (x+120, y+15, 85, 55))
    pygame.draw.rect(screen, GLASS, (x+15, y+80, 85, 65))
    pygame.draw.rect(screen, GLASS, (x+120, y+80, 85, 65))


def draw_cat(x, y, color, eye_color, scale=1):
    # тело
    pygame.draw.ellipse(screen, color, (x, y, 300*scale, 100*scale))
    pygame.draw.ellipse(screen, color, (x-80*scale, y-20*scale, 120*scale, 80*scale))
    pygame.draw.ellipse(screen, color, (x+220*scale, y+20*scale, 90*scale, 70*scale))
    pygame.draw.ellipse(screen, color, (x+240*scale, y+60*scale, 40*scale, 80*scale))
    pygame.draw.ellipse(screen, color, (x+40*scale, y+50*scale, 100*scale, 40*scale))

    # уши
    pygame.draw.polygon(screen, color,
                        [(x-60*scale, y-10*scale),
                         (x-40*scale, y-40*scale),
                         (x-10*scale, y-10*scale)])
    pygame.draw.polygon(screen, color,
                        [(x+10*scale, y-10*scale),
                         (x+30*scale, y-40*scale),
                         (x+40*scale, y-5*scale)])

    # глаза
    pygame.draw.ellipse(screen, eye_color,
                        (x-50*scale, y+5*scale, 30*scale, 20*scale))
    pygame.draw.ellipse(screen, eye_color,
                        (x-10*scale, y+5*scale, 30*scale, 20*scale))

    pygame.draw.line(screen, BLACK,
                     (x-35*scale, y+5*scale),
                     (x-35*scale, y+25*scale), 2)
    pygame.draw.line(screen, BLACK,
                     (x+5*scale, y+5*scale),
                     (x+5*scale, y+25*scale), 2)

    # нос
    pygame.draw.polygon(screen, BLACK,
                        [(x-20*scale, y+30*scale),
                         (x-25*scale, y+38*scale),
                         (x-15*scale, y+38*scale)])


def draw_yarn(x, y, r):
    # основной шар
    pygame.draw.circle(screen, (180, 180, 180), (x, y), r)
    pygame.draw.circle(screen, (120, 120, 120), (x, y), r, 2)

    # внутренние нити (дуги под разными углами)
    for i in range(-3, 4):
        pygame.draw.arc(
            screen,
            (90, 90, 90),
            (x - r + i*4, y - r//2, 2*r - i*8, r),
            0,
            math.pi,
            2
        )

    for i in range(-2, 3):
        pygame.draw.arc(
            screen,
            (100, 100, 100),
            (x - r//2, y - r + i*5, r, 2*r - i*10),
            math.pi/2,
            3*math.pi/2,
            2
        )

    # хвостик нитки (волнистая линия)
    points = []
    for i in range(40):
        px = x + r + i * 4
        py = y + 10 * math.sin(i * 0.4)
        points.append((px, py))

    if len(points) > 1:
        pygame.draw.lines(screen, (110, 110, 110), False, points, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # фон
    screen.fill(WALL)
    pygame.draw.rect(screen, FLOOR, (0, 300, 1000, 400))

    # окна
    draw_window(80, 40)
    draw_window(390, 40)
    draw_window(700, 40)

    # большие коты
    draw_cat(550, 350, ORANGE, GREEN, 1)
    draw_cat(250, 450, GRAY_CAT, BLUE, 1)

    # маленькие котята
    draw_cat(150, 360, ORANGE, GREEN, 0.4)
    draw_cat(800, 500, ORANGE, GREEN, 0.4)
    draw_cat(450, 560, ORANGE, GREEN, 0.5)
    draw_cat(200, 620, GRAY_CAT, BLUE, 0.4)
    draw_cat(820, 620, GRAY_CAT, BLUE, 0.4)

    # клубки
    draw_yarn(350, 370, 40)
    draw_yarn(650, 500, 60)
    draw_yarn(500, 620, 80)
    draw_yarn(250, 580, 40)
    draw_yarn(750, 600, 60)
    draw_yarn(600, 650, 35)

    pygame.display.flip()
    clock.tick(60)