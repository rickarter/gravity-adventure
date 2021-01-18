from vector import Vector2D, interpolate
import pygame
import random
import math

class menu_button():
    def __init__(self, center_x, center_y, width, height, sprite):
        self.left = center_x-width/2
        self.top = center_y-height/2
        self.width = width
        self.height = height
        self.sprite = sprite

        self.rect = pygame.Rect(self.left, self.top, width, height)
        self.sprite = pygame.transform.scale(sprite, (width, height))
    
    def render(self, surface):
        surface.blit(self.sprite, (self.left, self.top))

    def is_clicked(self, position):
        if self.rect.collidepoint(position):
            return True
        else:
            return False

class object:
    def __init__(self, position, mass, radius):
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.force = Vector2D(0, 0)
        self.mass = mass
        self.radius = radius
        self.collider_radius = self.radius * 0.5
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
        # pygame.draw.circle(surface, (255, 255, 255), Vector2D.vector2list(self.position), self.radius * 0.5)
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
        self.collider_radius = 3
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
        # self.collider_radius = 0
        self.has_won = False
        self.mass = 1
        self.to_break = False
        self.exit_button = menu_button(1920/2, 1080/2, 300, 100, pygame.image.load('assets\\sprites\\exit_button.png'))
    
    def on_collision(self, other):
        if not (self.is_destroyed or self.has_won):
            _type = type(other)
            if _type is goal_planet:
                self.has_won = True
                self.is_dynamic = False
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
            ''' mx, my = pygame.mouse.get_pos()
            button_exit = pygame.Rect(1920/2 - 200, 1080/2 - 100, 300, 100)
            Exit = pygame.transform.scale(pygame.image.load('assets\\sprites\\exit_button.png'), (300, 100))
            surface.blit(Exit, (1920/2 - 200, 1080/2 - 100))

            click = pygame.mouse.get_pressed()[0]
            if button_exit.collidepoint((mx, my)):
            if click:
            self.to_break = True'''

        if self.has_won or self.is_destroyed:
                '''mx, my = pygame.mouse.get_pos()
                button_exit = pygame.Rect(1920/2 - 200, 1080/2 - 100, 300, 100)
                Exit = pygame.transform.scale(pygame.image.load('assets\\sprites\\exit_button.png'), (300, 100))
                surface.blit(Exit, (1920/2 - 200, 1080/2 - 100))  

                click = pygame.mouse.get_pressed()[0]
                if button_exit.collidepoint((mx, my)):
                    if click:
                        self.to_break = True  
                '''

                self.exit_button.render(surface)

                click = pygame.mouse.get_pressed()[0]
                if click:
                    click_position = pygame.mouse.get_pos()
                    print(click_position)
                    if self.exit_button.is_clicked(click_position):
                        self.to_break = True

    def update(self, delta_time):
        self.sprite = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets\\sprites\\space_ship.png'), (self.radius, self.radius)), -self.velocity.get_angle() * 180 / math.pi)