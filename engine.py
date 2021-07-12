from angle_meter import AngleMeter
from power_meter import PowerMeter
from base import Base
from background import Background
from ball import Ball
from cannon import Cannon
import pygame
import time
import os


def play_game() -> bool:
    """The main game function. This isn't a bad idea to get into the habit of. It can
    be useful to separate different levels this way, and it will make it easier to
    integrate into the arcade.

    Returns:
        bool: True if complete
    """
    pygame.init()

    # Define some useful constants in one place
    constants = {
        "screen_width": 1200,
        "screen_height": 900,
        "gravity": 98,
        "ground": 700,
        "fps": 60,
        "font": "Ariel",
        "font_size": 80,
    }

    # Set up our window
    window = pygame.display.set_mode(
        (constants["screen_width"], constants["screen_height"])
    )
    pygame.display.set_caption("SuperAwesomeTutorial")

    # Empty list to eventually store game objects
    game_objects = []

    # Bring in our images
    background_image = pygame.image.load(os.path.join("resources", "background.png"))
    background_image = pygame.transform.scale(
        background_image, (constants["screen_width"], constants["screen_height"])
    )
    ball_img = pygame.image.load(os.path.join("resources", "Cannonball.png"))
    cannon_img = pygame.image.load(os.path.join("resources", "Cannon.png"))
    base_img = pygame.image.load(os.path.join("resources", "Wheel.png"))

    # Set up our objects
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

    # Add our objects to our game object list so they get updated and rendered
    game_objects.append(cannon)
    game_objects.append(base)
    game_objects.append(power_meter)
    game_objects.append(angle_meter)

    # Set up our FPS cap and timekeeping variables
    curr_time = time.time()
    frame_time = 1 / constants["fps"]

    # Load our awesome soundtrack
    pygame.mixer.music.load(os.path.join("resources", "AwesomeSoundtrack.wav"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    # Load our cannon soundfx
    cannon_sound = pygame.mixer.Sound(os.path.join("resources", "CannonFire.wav"))

    # The main loop! Lets goooooooooooooo
    while True:
        # Lock the framerate so we don't get any wonky behavior
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
                    # Fire the ball by making the ball, giving it a velocity, and
                    # adding it to our objects list. Finally, play the sound
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
        # Update everything. Currently, every ball we fire needs this
        for obj in game_objects:
            obj.update(dt)

        #####################
        ### Render Screen ###
        #####################
        # Ensure the background is always at the back
        background.render(window)

        # Render everythin in front of the background
        for obj in game_objects:
            obj.render(window)

        # Update the display with all the images we just rendered
        pygame.display.flip()


if __name__ == "__main__":
    play_game()
