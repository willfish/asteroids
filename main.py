import pygame
from pygame.event import wait

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FRAMES_PER_SECOND,
    DELTA_IN_SECONDS,
    BLACK
)

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    asteroids = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = updateables, drawables
    Asteroid.containers = asteroids, updateables, drawables
    AsteroidField.containers = updateables
    Shot.containers = shots

    AsteroidField()

    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2
    )

    while True:
        screen.fill(BLACK)

        for updateable in updateables:
            updateable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        for shot in shots:
            shot.draw(screen)
            shot.update(dt)

            for asteroid in asteroids:
                if shot.collides(asteroid):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(FRAMES_PER_SECOND) / DELTA_IN_SECONDS

if __name__ == "__main__":
    main()
