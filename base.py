import pygame


class Base:
    def __init__(self, image, x, y) -> None:
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect(center=(x, y))

    def update(self, time_step):
        pass

    def render(self, window):
        window.blit(self.image, self.rect)
