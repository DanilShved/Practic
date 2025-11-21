import pygame
import sys
from character import Character
from Platform import Platform

# Инициализация Pygame
pygame.init()

# Настройки окна
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

# Загрузка фона
try:
    background = pygame.image.load('imgs/background.png').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((135, 206, 235))  # Голубой фон

# Создание объектов
player = Character(100, 300)

# Создание уровня вручную
platforms = [
    # Земля
    Platform(0, 600, 1200, 100, "ground"),

    # Платформы первого уровня
    Platform(200, 500, 200, 30, "grass"),
    Platform(500, 500, 150, 30, "grass"),
    Platform(800, 500, 250, 30, "grass"),

    # Платформы второго уровня
    Platform(100, 400, 150, 30, "stone"),
    Platform(350, 400, 200, 30, "stone"),
    Platform(650, 400, 100, 30, "stone"),
    Platform(900, 400, 180, 30, "stone"),

    # Платформы третьего уровня
    Platform(250, 300, 120, 30, "grass"),
    Platform(500, 300, 200, 30, "grass"),
    Platform(800, 300, 150, 30, "grass"),

    # Платформы четвертого уровня
    Platform(150, 200, 100, 30, "stone"),
    Platform(400, 200, 150, 30, "stone"),
    Platform(700, 200, 120, 30, "stone"),
    Platform(950, 200, 100, 30, "stone"),

    # Финальная платформа
    Platform(500, 100, 200, 30, "grass"),
]

# Игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Обновление
    player.handle_input()
    player.update(platforms)

    # Отрисовка
    screen.blit(background, (0, 0))

    # Рисуем платформы
    for platform in platforms:
        platform.draw(screen)

    # Рисуем персонажа
    player.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
sys.exit()