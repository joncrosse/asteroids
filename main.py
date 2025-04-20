import pygame
from constants import *
from player import Player
from asteroids import Asteroids

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0.0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill((0,0,0))


        updatable.update(dt)
        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000
        
    #print("Starting Asteroids")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()