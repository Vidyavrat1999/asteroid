import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()  # Change from list to pygame.sprite.Group
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()  # New group for shots

# Set static containers for Asteroid class
Asteroid.containers = (asteroids, updatable, drawable)

# Set static containers for AsteroidField class
AsteroidField.containers = (updatable,)

# Set static containers for Shot class
Shot.containers = (shots, updatable, drawable)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    player1 = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    updatable.add(player1)  # Use .add() for pygame.sprite.Group
    drawable.add(player1)   # Use .add() for pygame.sprite.Group

    # Create an AsteroidField object
    asteroid_field = AsteroidField()
    # No need to manually add asteroid_field to updatable; it's handled by containers

    clock = pygame.time.Clock()
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player1.check_collision(asteroid):
                print("Game over!")
                running = False
                break

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()  # Remove the shot
                    asteroid.split()  # Split the asteroid
                    break  # Exit inner loop to avoid modifying the group during iteration

        # Draw all drawable objects
        screen.fill((0, 0, 0))  # Clear screen
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
