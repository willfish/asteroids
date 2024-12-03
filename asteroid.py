import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLIER, WHITE, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=WHITE,
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
        )

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > 20:
            left, right = self.random_directions()
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            a = Asteroid(self.position.x, self.position.y, new_radius)
            a.velocity = left * ASTEROID_SPLIT_SPEED_MULTIPLIER

            b = Asteroid(self.position.x, self.position.y, new_radius)
            b.velocity = right * ASTEROID_SPLIT_SPEED_MULTIPLIER

        self.kill()

    def random_directions(self):
        direction = random.uniform(20, 50)
        left = self.velocity.rotate(direction)
        right = self.velocity.rotate(-direction)

        return (left, right)
