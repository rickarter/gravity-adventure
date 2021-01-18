from physics_world import *
from objects import *
from vector import Vector2D, interpolate
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

def draw_ammo_remain(surface, max_ammo, current_ammo, left_corner, right_corner):
    fill_percentage = current_ammo/max_ammo
    fill_length = interpolate(0, right_corner[0]-left_corner[0], fill_percentage)
    pygame.draw.rect(surface, (255, 0, 0), (left_corner[0], left_corner[1], right_corner[0], right_corner[1]), 10)
    # pygame.draw.rect(surface, (255, 0, 0), (left_corner[0], left_corner[1], left_corner[0]+fill_length, right_corner[1]))
    print(fill_percentage)



def game(surface):
    # Init game variables
    world = physics_world()

    world.add_object(space_ship(Vector2D(200, 1080/2)))
    world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2), 120))
    world.add_object(goal_planet(Vector2D(1920/2+400, 1080/2), 120))
    # world.add_object(black_hole(Vector2D(1920/2, 1080/2), 120))

    is_scoping = False
    scope_object = scope(Vector2D(0, 0))
    slow_motion_scale = 0.1

    bullets = []

    ammo = 500

    run = True
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
                    bullets.append([world.objects[0].position, scope_object.position, Vector2D(0, 0), 0, scope_object.radius])
                    ammo += scope_object.radius
                    print(ammo)

        surface.fill((51, 51, 51))

        world.step(surface)

        if is_scoping:
            scope_object.render(surface)
            addition_speed = world.delta_time*100
            if world.time_scale != 1:
                addition_speed /= slow_motion_scale
            scope_object.radius += addition_speed

        for bullet in bullets:
            bullet[2] = Vector2D.lerp(bullet[0], bullet[1], bullet[3])
            bullet[3] += world.delta_time
            pygame.draw.circle(surface, (0, 0, 0), Vector2D.vector2list(bullet[2]), 5)
            if bullet[3] >= 1:
                bullets.remove(bullet)
                world.add_object(black_hole(bullet[1], bullet[4]))

        '''if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            world.add_object(object(Vector2D(mouse_position[0], mouse_position[1]), 1))'''

        # draw_ammo_remain(surface, 500, ammo, (860, 50), (960, 75))

        pygame.display.update()

def menu(surface):
    game(surface)

menu(window)