class Background:
    def __init__(self, image, x, y) -> None:
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, time_step):
        pass

    def render(self, window):
        window.blit(self.image, self.rect)
