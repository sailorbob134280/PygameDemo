import pygame
import time
import os


def play_game():
    pygame.init()

    constants = {"screen_width": 800, "screen_height": 600}

    window = pygame.display.set_mode(
        (constants["screen_width"], constants["screen_height"])
    )
    pygame.display.set_caption("SuperAwesomeTutorial")

    game_objects = []

    background_image = pygame.image.load(os.path.join("resources", "background.png"))
    background_image = pygame.transform.scale(background_image, (800, 600))
    ball_img = pygame.image.load(os.path.join("resources", "Cannonball.png"))
    cannon_img = pygame.image.load(os.path.join("resources", "Cannon.png"))

    while True:

        #####################
        ### Handle Events ###
        #####################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        #####################
        ### Handle Inputs ###
        #####################
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:  # UP
            pass
        if keys_pressed[pygame.K_a]:  # LEFT
            pass
        if keys_pressed[pygame.K_s]:  # DOWN
            pass
        if keys_pressed[pygame.K_d]:  # RIGHT
            pass
        if keys_pressed[pygame.K_SPACE]:  # FIRE
            pass

        ######################
        ### Handle Updates ###
        ######################

        #####################
        ### Render Screen ###
        #####################
        window.blit(background_image, (0, 0))
        window.blit(ball_img, (400, 300))
        window.blit(cannon_img, (200, 300))
        pygame.display.update()


if __name__ == "__main__":
    play_game()
