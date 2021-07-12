import math


class Ball:
    """Ball class to represent the ball. Responsible for tracking its position
    and velocity, ground detection, and rendering"""

    def __init__(
        self,
        image,
        x: int,
        y: int,
        angle: float,
        vel: float,
        gravity: float,
        ground: int,
    ) -> None:
        """Constructor

        Args:
            image (pygame.image): The sprite image of the ball
            x (int): The initial x position in pixels of the center of the rect
            y (int): The initial y position in pixels of the center of the rect
            angle (float): The angle the ball is fired at
            vel (float): The initial velocity the ball is fired at
            gravity (float): The value of gravity for this world
            ground (int): The ground y location in pixels
        """
        self.image = image
        self.x = x
        self.y = y
        self.vel_x = math.cos(math.radians(angle)) * vel
        self.vel_y = -math.sin(math.radians(angle)) * vel
        self.gravity = gravity
        self.ground = ground
        self.rect = image.get_rect(center=(x, y))
        self.on_ground = False

    def update(self, time_step: float) -> None:
        """Update function that actually moves the ball. If the ball is on the
        ground, it stops moving

        Args:
            time_step (float): The time since the last frame
        """
        if not self.on_ground:
            self.x += self.vel_x * time_step
            self.y += self.vel_y * time_step + self.gravity * (time_step ** 2) * 0.5
            self.vel_y += self.gravity * time_step

            self.rect = self.image.get_rect(center=(self.x, self.y))

            if self.y > self.ground + 20:
                self.on_ground = True

    def render(self, window) -> None:
        """Renders the ball

        Args:
            window (pygame.window): Window to blit the sprite to
        """
        window.blit(self.image, self.rect)
