from vector import Vector2D, interpolate
import pygame

class object:
    def __init__(self, position, mass, radius):
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.force = Vector2D(0, 0)
        self.mass = mass
        self.radius = radius
        self.is_dynamic = True

    def render(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), 5)
        
    def on_collision(self, other):
        pass

    def update(self, delta_time):
        pass

class planet(object):
    def __init__(self, position, radius):
        self.half_of_the_radius = radius/2
        self.sprite = self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\placeholder.png'), (int(radius), int(radius)))
        super().__init__(position, radius*0.5, radius)
    def render(self, surface):
        surface.blit(self.sprite, (self.position.x - self.half_of_the_radius, self.position.y - self.half_of_the_radius))

class lava_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\lava_planet.png'), (int(radius), int(radius)))
        self.is_dynamic = False

class goal_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\goal_planet.png'), (int(radius), int(radius)))
        self.is_dynamic = False

class black_hole(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        # self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\black_hole.png'), (int(radius), int(radius)))
        self.radius_t = 0
        self.is_dynamic = False
        self.mass = self.radius * 2

    def update(self, delta_time):
        if self.radius_t < 1:
            current_radius = interpolate(7, self.radius, self.radius_t)
            self.half_of_the_radius = current_radius/2
            self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\placeholder.png'), (int(current_radius), int(current_radius)))
            self.radius_t += delta_time

class asteroid(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\sprites\asteroid.png'), (int(radius), int(radius)))
        

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