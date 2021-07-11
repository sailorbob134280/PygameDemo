from angle_meter import AngleMeter
from power_meter import PowerMeter
from base import Base
from background import Background
from ball import Ball
from cannon import Cannon
import pygame
import time
import os


def play_game():
    pygame.init()

    constants = {
        "screen_width": 1200,
        "screen_height": 900,
        "gravity": 98,
        "ground": 700,
        "fps": 60,
        "font": "Ariel",
        "font_size": 80,
    }

    window = pygame.display.set_mode(
        (constants["screen_width"], constants["screen_height"])
    )
    pygame.display.set_caption("SuperAwesomeTutorial")

    game_objects = []

    background_image = pygame.image.load(os.path.join("resources", "background.png"))
    background_image = pygame.transform.scale(
        background_image, (constants["screen_width"], constants["screen_height"])
    )
    ball_img = pygame.image.load(os.path.join("resources", "Cannonball.png"))
    cannon_img = pygame.image.load(os.path.join("resources", "Cannon.png"))
    base_img = pygame.image.load(os.path.join("resources", "Wheel.png"))

    cannon = Cannon(cannon_img, 100, constants["ground"])
    base = Base(base_img, 100, constants["ground"])
    background = Background(background_image, 0, 0)
    power_meter = PowerMeter(
        80,
        constants["ground"] + 130,
        constants["font"],
        constants["font_size"],
        cannon,
    )
    angle_meter = AngleMeter(
        80, constants["ground"] + 70, constants["font"], constants["font_size"], cannon
    )

    game_objects.append(cannon)
    game_objects.append(base)
    game_objects.append(power_meter)
    game_objects.append(angle_meter)

    curr_time = time.time()
    frame_time = 1 / constants["fps"]

    pygame.mixer.music.load(os.path.join("resources", "AwesomeSoundtrack.wav"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    cannon_sound = pygame.mixer.Sound(os.path.join("resources", "CannonFire.wav"))

    while True:
        last_time = curr_time
        curr_time = time.time()
        dt = curr_time - last_time
        if dt < frame_time:
            time.sleep(frame_time - dt)

        #####################
        ### Handle Events ###
        #####################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = Ball(
                        ball_img,
                        cannon.rect.right,
                        cannon.rect.centery,
                        cannon.angle,
                        cannon.power,
                        constants["gravity"],
                        constants["ground"],
                    )
                    game_objects.append(ball)
                    cannon_sound.play()

        #####################
        ### Handle Inputs ###
        #####################
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:  # UP
            cannon.rotate(0.1)
        if keys_pressed[pygame.K_a]:  # LEFT
            cannon.change_power(-1)
        if keys_pressed[pygame.K_s]:  # DOWN
            cannon.rotate(-0.1)
        if keys_pressed[pygame.K_d]:  # RIGHT
            cannon.change_power(1)

        ######################
        ### Handle Updates ###
        ######################
        for obj in game_objects:
            obj.update(dt)

        #####################
        ### Render Screen ###
        #####################
        # window.blit(background_image, (0, 0))
        # window.blit(ball_img, (400, 300))
        # window.blit(cannon_img, (200, 300))
        # Ensure the background is always at the back
        background.render(window)
        for obj in game_objects:
            obj.render(window)
        pygame.display.flip()


if __name__ == "__main__":
    play_game()
