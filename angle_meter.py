from cannon import Cannon
import pygame


class AngleMeter:
    def __init__(
        self, x: int, y: int, font: str, font_size: int, cannon: Cannon
    ) -> None:
        """Constructor

        Args:
            x (int): The x position in pixels
            y (int): The y position in pixels
            font (str): The name of the desired font
            font_size (int): The size of the font in pixels
            cannon (Cannon): The cannon object to read the angle from
        """
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, font_size)
        self.cannon = cannon

    def update(self, time_step: float) -> None:
        """Empty update function. Must be here because it is a game object

        Args:
            time_step (float): Time since last frame
        """
        pass

    def render(self, window: pygame.display) -> None:
        """Renders the angle meter

        Args:
            window (pygame.display): The window to blit the text to
        """
        text = self.font.render(
            str(round(self.cannon.angle, 2)), 1, pygame.Color(255, 255, 255)
        )
        window.blit(text, (self.x, self.y))
