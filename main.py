from physics_world import *
from objects import *
from vector import Vector2D
import pygame


window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gravity Adventure")

class scope():
    def __init__(self, position):
        self.position = position
        self.radius = 1
         
    def render(self, surface):
        pygame.draw.circle(surface, (0, 0, 0), Vector2D.vector2list(self.position), self.radius)
        print(self.radius)

def game(surface):
    # Init game variables
    world = physics_world()

    world.add_object(object(Vector2D(250, 250), 90))
    world.add_object(object(Vector2D(1920/2, 1080/2), 90))
    world.add_object(lava_planet(Vector2D(1920/2+100, 1080/2-300), 50))

    run = True
    is_scoping = False
    scope_object = scope(Vector2D(0, 0))
    radius = 1
    slow_motion_scale = 0.1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    world.time_scale = slow_motion_scale
                if event.button == 1:
                    scope_object = scope(Vector2D.list2vector(pygame.mouse.get_pos()))
                    is_scoping = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    world.time_scale = 1
                if event.button == 1:
                    is_scoping = False

        surface.fill((51, 51, 51))

        world.step(surface)

        if is_scoping:
            scope_object.render(surface)
            scope_object.radius += world.delta_time*100

        '''if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            world.add_object(object(Vector2D(mouse_position[0], mouse_position[1]), 1))'''

        pygame.display.update()

def menu(surface):
    game(surface)

menu(window)