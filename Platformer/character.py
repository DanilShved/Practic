from pygame.math import Vector2
import pygame


class Character:
    def __init__(self, x, y):
        # Позиция и физика
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        # Параметры физики
        self.speed = 5
        self.jump_power = -15
        self.gravity = 0.8
        self.friction = 0.85

        # Состояния
        self.is_jumping = False
        self.is_grounded = False
        self.facing_right = True

        # Размеры персонажа
        self.width = 50
        self.height = 70

        # Загрузка текстур персонажа (только влево/вправо)
        try:
            self.texture_right = pygame.image.load('imgs/character.png').convert_alpha()
            self.texture_left = pygame.image.load('imgs/character_inv.png').convert_alpha()

            # Масштабируем текстуры
            self.texture_right = pygame.transform.scale(self.texture_right, (self.width, self.height))
            self.texture_left = pygame.transform.scale(self.texture_left, (self.width, self.height))

        except pygame.error as e:
            print(f"Ошибка загрузки текстур персонажа: {e}")
            # Запасные цветные прямоугольники
            self.texture_right = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.rect(self.texture_right, (255, 0, 0), (0, 0, self.width, self.height))
            self.texture_left = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.rect(self.texture_left, (200, 0, 0), (0, 0, self.width, self.height))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Сбрасываем горизонтальное ускорение
        self.acc.x = 0

        # Движение влево/вправо
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acc.x = -0.8
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acc.x = 0.8
            self.facing_right = True

        # Прыжок
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.is_grounded:
            self.vel.y = self.jump_power
            self.is_grounded = False
            self.is_jumping = True

    def update(self, platforms):
        # Применяем ускорение к скорости
        self.vel.x += self.acc.x
        self.vel.y += self.gravity

        # Применяем трение когда на земле
        if self.is_grounded:
            self.vel.x *= self.friction

        # Ограничиваем максимальную скорость
        self.vel.x = max(-self.speed, min(self.vel.x, self.speed))

        # Обновляем позицию по X
        self.pos.x += self.vel.x
        self.handle_collisions_x(platforms)

        # Обновляем позицию по Y
        self.pos.y += self.vel.y
        self.handle_collisions_y(platforms)

        # Проверяем выход за границы экрана
        self.check_bounds()

    def handle_collisions_x(self, platforms):
        for platform in platforms:
            if (self.pos.x < platform.rect.x + platform.rect.width and
                    self.pos.x + self.width > platform.rect.x and
                    self.pos.y < platform.rect.y + platform.rect.height and
                    self.pos.y + self.height > platform.rect.y):

                if self.vel.x > 0:  # Движение вправо
                    self.pos.x = platform.rect.x - self.width
                elif self.vel.x < 0:  # Движение влево
                    self.pos.x = platform.rect.x + platform.rect.width
                self.vel.x = 0

    def handle_collisions_y(self, platforms):
        self.is_grounded = False
        for platform in platforms:
            if (self.pos.x < platform.rect.x + platform.rect.width and
                    self.pos.x + self.width > platform.rect.x and
                    self.pos.y < platform.rect.y + platform.rect.height and
                    self.pos.y + self.height > platform.rect.y):

                if self.vel.y > 0:  # Падение вниз
                    self.pos.y = platform.rect.y - self.height
                    self.vel.y = 0
                    self.is_grounded = True
                    self.is_jumping = False
                elif self.vel.y < 0:  # Движение вверх
                    self.pos.y = platform.rect.y + platform.rect.height
                    self.vel.y = 0

    def check_bounds(self):
        # Ограничение по левой границе
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x = 0
        # Если упал за экран - респавн
        if self.pos.y > 1000:
            self.reset_position()

    def reset_position(self):
        self.pos = Vector2(100, 100)
        self.vel = Vector2(0, 0)

    def draw(self, screen):
        # Просто выбираем текстуру в зависимости от направления
        if self.facing_right:
            current_texture = self.texture_right
        else:
            current_texture = self.texture_left

        screen.blit(current_texture, (self.pos.x, self.pos.y))