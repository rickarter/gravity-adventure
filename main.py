from physics_world import *
from objects import *
from vector import Vector2D
import pygame


window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gravity Adventure")
# Init game variables
world = physics_world()

world.add_object(object(Vector2D(250, 250), 90))
world.add_object(object(Vector2D(1920/2, 1080/2), 90))

world.objects[0].velocity = Vector2D(100, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = False

    window.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        mouse_position = pygame.mouse.get_pos()
        world.add_object(object(Vector2D(mouse_position[0], mouse_position[1]), 1))

    world.step(window)

    pygame.display.update()
    pass
