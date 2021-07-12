class Base:
    """Base class to represent the base of the cannon"""

    def __init__(self, image, x: int, y: int) -> None:
        """Constructor

        Args:
            image (pygame.image): The sprite image of the base
            x (int): The x position in pixels of the center of the rect
            y (int): The y position in pixels of the center of the rect
        """
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect(center=(x, y))

    def update(self, time_step) -> None:
        """Empty update function. Must be here because it is a game object

        Args:
            time_step (float): Time since last frame
        """
        pass

    def render(self, window) -> None:
        """Renders the base

        Args:
            window (pygame.display): The window to blit the sprite to
        """
        window.blit(self.image, self.rect)
