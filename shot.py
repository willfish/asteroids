import pygame

from circleshape import CircleShape
from constants import WHITE, LINE_WIDTH, PLAYER_SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOT_RADIUS)

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
