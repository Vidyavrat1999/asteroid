import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def split(self):
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid, no further splitting

        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new asteroids
        Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2)

