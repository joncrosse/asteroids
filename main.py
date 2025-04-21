import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfields import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0.0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,shots)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill((0,0,0))


        updatable.update(dt)
        shots.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game Over!")
                sys.exit()
            for s in shots:
                if s.collision(a):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000
        
    #print("Starting Asteroids")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()