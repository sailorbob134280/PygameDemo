import pygame


class PowerMeter:
    def __init__(self, x, y, font, font_size, cannon) -> None:
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, font_size)
        self.cannon = cannon

    def update(self, time_step):
        pass

    def render(self, window):
        text = self.font.render(
            str(self.cannon.power / 10), 1, pygame.Color(255, 255, 255)
        )
        window.blit(text, (self.x, self.y))
