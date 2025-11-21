import pygame


class Platform:
    def __init__(self, x, y, width, height, texture_type="ground"):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture_type = texture_type

        # Загрузка текстур блоков
        try:
            if texture_type == "ground":
                self.texture = pygame.image.load('imgs/block_ground.png').convert_alpha()
            elif texture_type == "grass":
                self.texture = pygame.image.load('imgs/block_grass.png').convert_alpha()
            elif texture_type == "stone":
                self.texture = pygame.image.load('imgs/block_stone.png').convert_alpha()
            else:
                self.texture = pygame.image.load('imgs/block_default.png').convert_alpha()

            # Масштабируем текстуру под размер платформы
            self.texture = pygame.transform.scale(self.texture, (width, height))

        except pygame.error as e:
            print(f"Ошибка загрузки текстуры платформы: {e}")
            # Запасной цвет
            self.texture = pygame.Surface((width, height))
            if texture_type == "ground":
                self.texture.fill((139, 69, 19))  # Коричневый
            elif texture_type == "grass":
                self.texture.fill((34, 139, 34))  # Зеленый
            elif texture_type == "stone":
                self.texture.fill((128, 128, 128))  # Серый
            else:
                self.texture.fill((100, 100, 100))

    def draw(self, screen):
        screen.blit(self.texture, self.rect)