from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.shoot_timer = 0  # Timer for shooting cooldown

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer <= 0:  # Only shoot if timer is 0 or less
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            Shot(self.position.x, self.position.y, velocity)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer

    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt  # Decrease the timer by dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
