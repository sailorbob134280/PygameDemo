import pygame


class Cannon:
    def __init__(self, image, x, y) -> None:
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect(center=(x, y))
        self.angle = 0
        self.power = 0

    def rotate(self, da):
        self.angle += da

    def change_power(self, dp):
        self.power += dp

    def update(self, time_step):
        pass

    def render(self, window):
        new_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = new_image.get_rect(center=(self.x, self.y))
        window.blit(new_image, new_rect)
