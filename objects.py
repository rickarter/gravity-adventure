from vector import Vector2D, interpolate
import pygame
import random

class object:
    def __init__(self, position, mass, radius):
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.force = Vector2D(0, 0)
        self.mass = mass
        self.radius = radius
        self.collider_radius = self.radius
        self.is_dynamic = True
        self.to_delete = False

    def render(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), 5)
        
    def on_collision(self, other):
        pass

    def update(self, delta_time):
        pass

class planet(object):
    def __init__(self, position, radius):
        self.half_of_the_radius = radius/2
        self.sprite = self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\placeholder.png'), (int(radius), int(radius)))
        super().__init__(position, radius*0.5, radius)
    def render(self, surface):
        surface.blit(self.sprite, (self.position.x - self.half_of_the_radius, self.position.y - self.half_of_the_radius))

class lava_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\lava_planet.png'), (int(radius), int(radius)))
        self.is_dynamic = False

class goal_planet(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\goal_planet.png'), (int(radius), int(radius)))
        self.is_dynamic = False

class black_hole(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\black_hole.png'), (int(radius), int(radius)))
        self.radius_t = 0
        self.is_dynamic = False
        self.mass = self.radius * 2

    def update(self, delta_time):
        if self.radius_t < 1:
            current_radius = interpolate(7, self.radius, self.radius_t)
            self.half_of_the_radius = current_radius/2
            self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\black_hole.png'), (int(current_radius), int(current_radius)))
            self.radius_t += delta_time

class asteroid(planet):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\asteroid.png'), (int(radius), int(radius)))
        self.collider_radius = 0
        self.is_destroyed = False
        self.particles = []

    def on_collision(self, other):
        if not self.is_destroyed:
            for i in range(0, 30):
                self.particles.append([Vector2D.vector2list(self.position), [random.randint(-50, 50)/10-1, random.randint(-50, 50)/10-1], random.randint(5, 20)])
            self.is_destroyed = True

    def render(self, surface):
        if not self.is_destroyed:
            super().render(surface)
        else:
            for particle in self.particles:
                pygame.draw.circle(surface, (188, 71, 42), particle[0], particle[2])

                particle[2] -= 0.1
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[1][1] += 0.001
            if self.particles.__len__() == 0:
                self.to_delete = True
        

class space_ship(planet):
    def __init__(self, position):
        super().__init__(position, 70)
        self.sprite = pygame.transform.scale(pygame.image.load('assets\\sprites\\space_ship.png'), (self.radius, self.radius))
        self.is_destroyed = False
        self.particles = []
        self.collider_radius = 0
        self.has_won = False
        self.mass = 1
        self.to_break = False
    
    def on_collision(self, other):
        if not (self.is_destroyed or self.has_won):
            _type = type(other)
            if _type is goal_planet:
                print('Collided with "goal" planet')
            else:
                if _type is not black_hole:
                    self.is_destroyed = True
                    for i in range(0, 30):
                        self.particles.append([Vector2D.vector2list(self.position), [random.randint(-50, 50)/10-1, random.randint(-50, 50)/10-1], random.randint(5, 20)])

    def render(self, surface):
        if not self.is_destroyed:
            super().render(surface)
        else:
            for particle in self.particles:
                pygame.draw.circle(surface, (188, 71, 42), particle[0], particle[2])

                particle[2] -= 0.1
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[1][1] += 0.001
            
            # Make exit button
                mx, my = pygame.mouse.get_pos()
                button_1 = pygame.Rect(1920/2 - 200, 1080/2 - 100, 300, 100)
                Exit = pygame.transform.scale(pygame.image.load('assets\\sprites\\exit_button.png'), (300, 100))
                surface.blit(Exit, (1920/2 - 200, 1080/2 - 100))

                click = False
                if button_1.collidepoint((mx, my)):
                    if click:
                        self.to_break = True  

                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True  

        if self.has_won:
                mx, my = pygame.mouse.get_pos()
                button_1 = pygame.Rect(1920/2 - 200, 1080/2 - 100, 300, 100)
                Exit = pygame.transform.scale(pygame.image.load('assets\\sprites\\exit_button.png'), (300, 100))
                surface.blit(Exit, (1920/2 - 200, 1080/2 - 100))  

                click = False
                if button_1.collidepoint((mx, my)):
                    if click:
                        self.to_break = True  

                for event in pygame.event.get():        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
