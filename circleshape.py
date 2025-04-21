import pygame

# Base class for game objects
updatable = []
drawable = []


class CircleShape(pygame.sprite.Sprite):
    containers = (updatable, drawable)


    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, target):
        r1 = self.radius
        r2 = target.radius
        distance = self.position.distance_to(target.position)

        if distance <= (r1+r2):
            return True
        return False