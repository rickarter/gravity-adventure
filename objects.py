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
        
    def on_collision(self, other):
        pass

    def update(self):
        pass

class planet(object):
    def __init__(self, position, radius):
        self.radius = radius
        self.half_of_the_radius = radius/2
        self.sprite = self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\placeholder.png'), (int(self.radius), int(self.radius)))
        super().__init__(position, self.radius)

    def render(self, surface):
        surface.blit(self.sprite, (self.position.x - self.half_of_the_radius, self.position.y - self.half_of_the_radius))

class lava_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\lava_planet.png'), (radius, radius))

class goal_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\goal_planet.png'), (radius, radius))

class black_hole(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        # self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\black_hole.png'), (radius, radius))

class space_ship(planet):
    def __init__(self, position):
        super().__init__(position, 70)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\space_ship.png'), (self.radius, self.radius))
    
    def on_collision(self, other):
        _type = type(other)
        if _type is goal_planet:
            print('Collided with "goal" planet')
        else:
            pass