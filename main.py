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

def draw_supply_remain(surface, current, max, position):
    percentage = current/max
    length = interpolate(0, position[2], percentage)
    pygame.draw.rect(surface, (165, 17, 133), position, 8)
    position[2] = length
    pygame.draw.rect(surface, (165, 17, 133), position)

def game(surface, new_world):
    # Init game variables

    is_scoping = False
    scope_object = scope(Vector2D(0, 0))
    slow_motion_scale = 0.1
    fast_mostion_scale = 5

    world = new_world

    supply = 500

    bullets = []

    run = True
    while run and world.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    world.time_scale = fast_mostion_scale
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    world.time_scale = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    world.time_scale = slow_motion_scale
                if event.button == 1:
                    if supply > 0:
                        scope_object = scope(Vector2D.list2vector(pygame.mouse.get_pos()))
                        is_scoping = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    world.time_scale = 1
                if event.button == 1:
                    if is_scoping:
                        is_scoping = False
                        bullets.append([world.objects[0].position, scope_object.position, Vector2D(0, 0), 0, scope_object.radius])

        surface.fill((51, 51, 51))

        world.step(surface)

        if is_scoping:
            scope_object.render(surface)
            addition_speed = world.delta_time*100
            if world.time_scale < 1:
                addition_speed /= slow_motion_scale
            if supply > 0:
                supply -= addition_speed
                scope_object.radius += addition_speed

        draw_supply_remain(window, supply, 500, [760, 40, 400, 20])

        for bullet in bullets:
            bullet[2] = Vector2D.lerp(bullet[0], bullet[1], bullet[3])
            bullet[3] += world.delta_time
            pygame.draw.circle(surface, (0, 0, 0), Vector2D.vector2list(bullet[2]), 5)
            if bullet[3] >= 1:
                bullets.remove(bullet)
                world.add_object(black_hole(bullet[1], bullet[4]))

        pygame.display.update()

def level_menu(surface):

    lv1_button = menu_button(1920/2 - 228 - 228, 1080/2, 128, 128,pygame.image.load('assets\\sprites\\first.png'))
    lv2_button = menu_button(1920/2 - 228, 1080/2 , 128, 128,pygame.image.load('assets\\sprites\\second.png'))
    lv3_button = menu_button(1920/2, 1080/2, 128, 128,pygame.image.load('assets\\sprites\\third.png'))
    lv4_button = menu_button(1920/2 + 228, 1080/2, 128, 128,pygame.image.load('assets\\sprites\\first.png'))
    lv5_button = menu_button(1920/2 + 228 + 228, 1080/2, 128, 128,pygame.image.load('assets\\sprites\\first.png'))
    world = physics_world()
    run = True
    while run:
        surface.fill((51, 51, 51))

        lv1_button.render(surface)
        lv2_button.render(surface)
        lv3_button.render(surface)
        lv4_button.render(surface)
        lv5_button.render(surface)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
                    click_position = pygame.mouse.get_pos()

        if click:
            if lv1_button.is_clicked(click_position):
                world = physics_world()

                world.add_object(space_ship(Vector2D(200, 1080/2)))
                world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2), 120))
                world.add_object(goal_planet(Vector2D(1920/2 + 500, 1080/2), 170))

                game(surface, world)
            elif lv2_button.is_clicked(click_position):
                world = physics_world()

                world.add_object(space_ship(Vector2D(200, 1080/2)))
                world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2 + 460), 140))
                world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2 - 460), 140))

                world.add_object(asteroid(Vector2D(1920/2, 1080/2 + 200), 120))

                world.add_object(asteroid(Vector2D(400, 1080/2 + 120), 80))
                world.add_object(asteroid(Vector2D(400 - 400, 1080/2 - 120), 80))

                world.add_object(asteroid(Vector2D(1920/2, 1080/2 - 200), 120))

                world.add_object(goal_planet(Vector2D(1920/2 + 500, 1080/2), 170))

                game(surface, world)  
            elif lv3_button.is_clicked(click_position):
                world = physics_world()
                world.add_object(space_ship(Vector2D(1920/2, 850)))
                world.add_object(lava_planet(Vector2D(1920/2, 1080/2 - 50), 140))
                world.add_object(lava_planet(Vector2D(200, 200), 140))

                world.add_object(asteroid(Vector2D(1500, 1080/2 - 200), 120))

                world.add_object(asteroid(Vector2D(1200, 1080/2 + 300), 80))
                world.add_object(asteroid(Vector2D(400, 400), 80))

                world.add_object(asteroid(Vector2D(1920/2 + 200, 1080/2 - 200), 120))

                world.add_object(goal_planet(Vector2D(1920/2, 1080/2 - 250), 170))

                game(surface, world)
            elif  lv4_button.is_clicked(click_position):
                world = physics_world()
                world.add_object(space_ship(Vector2D(100, 100)))
                world.add_object(lava_planet(Vector2D(450, 1080/2), 140))
                world.add_object(lava_planet(Vector2D(940, 1080/2), 140))

                world.add_object(asteroid(Vector2D(1400, 1080/2 - 200), 120))

                world.add_object(asteroid(Vector2D(300, 1080/2 - 320), 120))
                world.add_object(asteroid(Vector2D(500, 60), 80))

                world.add_object(asteroid(Vector2D(1920/2 - 200, 300), 120))
                world.add_object(asteroid(Vector2D(1920/2 - 200, 1080 - 100), 120))
                world.add_object(goal_planet(Vector2D(1920/2 + 400,1080/2), 170))

                game(surface, world)
            elif  lv5_button.is_clicked(click_position):
                world = physics_world()
                world.add_object(space_ship(Vector2D(100, 1080/2)))
                world.add_object(lava_planet(Vector2D(400, 300), 140))
                world.add_object(lava_planet(Vector2D(850, 1080/2 - 100), 140))
                world.add_object(lava_planet(Vector2D(1250, 1080 - 300), 140))

                world.add_object(asteroid(Vector2D(1300, 100), 120))

                world.add_object(asteroid(Vector2D(600, 1080/2 - 120), 80))
                world.add_object(asteroid(Vector2D(900, 900), 80))

                world.add_object(asteroid(Vector2D(100, 100), 120))

                world.add_object(goal_planet(Vector2D(1450, 300), 170))
                game(surface, world)
        pygame.display.update()

def main_menu(surface):
    start_button = menu_button(1920/2, 1080/2, 300, 100, pygame.image.load('assets\\sprites\\start_button.png'))
    run = True
    while run:
        
        surface.fill((51, 51, 51))

        start_button.render(surface)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
                    click_position = pygame.mouse.get_pos()

        if click:
            if start_button.is_clicked(click_position):
                level_menu(surface)

        pygame.display.update()    
            
main_menu(window)