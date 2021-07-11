import pygame
import math


class Ball:
    def __init__(self, image, x, y, angle, vel, gravity) -> None:
        self.image = image
        self.x = x
        self.y = y
        self.vel_x = math.cos(math.radians(angle)) * vel
        self.vel_y = -math.sin(math.radians(angle)) * vel
        self.gravity = gravity
        self.rect = image.get_rect(center=(x, y))
        self.on_ground = False

    def update(self, time_step):
        if not self.on_ground:
            self.x += self.vel_x * time_step
            self.y += self.vel_y * time_step + self.gravity * (time_step ** 2) * 0.5
            self.vel_y += self.gravity * time_step

            self.rect = self.image.get_rect(center=(self.x, self.y))

            if self.y > 460:
                self.on_ground = True

    def render(self, window):
        window.blit(self.image, self.rect)
