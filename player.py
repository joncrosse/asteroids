import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_COOLDOWN

class Player(CircleShape):
    

    def __init__(self, x, y, shot_group):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_group = shot_group
        self.cooldown = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation - 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        return self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if self.cooldown == 0:
            if keys[pygame.K_SPACE]:
                self.shoot(self.shot_group)
                self.cooldown += PLAYER_COOLDOWN
        if self.cooldown > 0:        
            self.cooldown -= dt
        if self.cooldown < 0:
            self.cooldown = 0
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shot_group):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        start = pygame.Vector2(0,-1).rotate(self.rotation)
        bullet.velocity = start * PLAYER_SHOOT_SPEED
        shot_group.add(bullet)