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


if __name__ == "__main__":
    play_game()
