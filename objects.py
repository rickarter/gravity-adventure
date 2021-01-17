from vector import Vector2D
import pygame

class object:
    def __init__(self, position, mass):
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.force = Vector2D(0, 0)
        self.mass = mass

    def render(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), 5)
        
    def is_colliding(self, other):
        pass

    def update(self):
        pass
