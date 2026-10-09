from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.cool_down = 0 # Rate Limit
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cool_down -= dt

        if keys[pygame.K_q]:
            self.rotate(-dt)

        if keys[pygame.K_e]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self,dt):
        unit_vector = pygame.Vector2(0,1).rotate(self.rotation)
        rotate_vector_speed = unit_vector * PLAYER_SPEED * dt
        self.position += rotate_vector_speed
    
    def shoot(self):
        # Create a new shot object 
        if self.cool_down > 0:
            return False
        else:
            self.cool_down = PLAYER_SHOOT_COOLDOWN_SECONDS
        shoots = Shot(self.position.x,self.position.y)
        shoots.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        
