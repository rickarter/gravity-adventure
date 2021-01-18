import pygame
from vector import interpolate

class BreakGame(Exception): pass

'''window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
pygame.display.set_caption("Gravity Adventure")

def draw_supply_remain(surface, current, max, position):
    percentage = current/max
    length = interpolate(0, position[2], percentage)
    pygame.draw.rect(surface, (165, 17, 133), position, 8)
    position[2] = length
    pygame.draw.rect(surface, (165, 17, 133), position)
ammo = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    window.fill((51, 51, 51))

    draw_ammo_remain(window, ammo, 500, [760, 40, 400, 95])

    if pygame.mouse.get_pressed()[0]:
        ammo += 1
    if pygame.mouse.get_pressed()[2]:
        ammo -= 1

    pygame.display.update()'''

world = physics_world()

world.add_object(space_ship(Vector2D(200, 1080/2)))
world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2 + 460), 140))
world.add_object(lava_planet(Vector2D(1920/2-200, 1080/2 - 460), 140))

world.add_object(asteroid(Vector2D(1920/2, 1080/2 + 200), 120))

world.add_object(asteroid(Vector2D(400, 1080/2 + 120), 80))
world.add_object(asteroid(Vector2D(400 - 400, 1080/2 - 120), 80))

world.add_object(asteroid(Vector2D(1920/2, 1080/2 - 200), 120))

world.add_object(goal_planet(Vector2D(1920/2 + 500, 1080/2), 170))