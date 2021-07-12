class Background:
    """Background class to represent the background image. Probably unnecessary,
    but good practice regardless.
    """

    def __init__(self, image, x: int, y: int) -> None:
        """Constructor

        Args:
            image (pygame.image): The background image
            x (int): The x position in pixels.
            y (int): The y position in pixels
        """
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, time_step: float) -> None:
        """Empty update function. Must be here because it is a game object

        Args:
            time_step (float): Time since last frame
        """
        pass

    def render(self, window) -> None:
        """Renders the background

        Args:
            window (pygame.display): The window to blit the image to
        """
        window.blit(self.image, self.rect)
