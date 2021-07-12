import pygame


class Cannon:
    """Cannon class to represent the cannon. It is responsible for tracking the
    angle and power to fire the ball at."""

    def __init__(self, image: pygame.image, x: int, y: int) -> None:
        """Constructor

        Args:
            image (PyGame Image): The sprite image of the cannon
            x (int): The x position in pixels of the center of the rect
            y (int): The y position in pixels of the center of the rect
        """
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect(center=(x, y))
        self.angle = 0
        self.power = 0

    def rotate(self, da: float) -> None:
        """Rotates the cannon by updating the angle attribute.

        Args:
            da (float): The amount by which to change the angle
        """
        self.angle += da

    def change_power(self, dp: float) -> None:
        """Changes the power to fire the ball at

        Args:
            dp (float): The amount by which to change the power
        """
        self.power += dp
        if self.power < 0:
            self.power = 0
        if self.power > 1000:
            self.power = 1000

    def update(self, time_step: float) -> None:
        """Empty update function. Must be here because it is a game object

        Args:
            time_step (float): Time since last frame
        """
        pass

    def render(self, window: pygame.display) -> None:
        """Renders the cannon

        Args:
            window (pygame.display): The window to blit the sprite to
        """
        new_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = new_image.get_rect(center=(self.x, self.y))
        window.blit(new_image, new_rect)
