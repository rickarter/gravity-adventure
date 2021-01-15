import pygame
from objects import *

class physics_world:
    def __init__(self):
        self.objects = []
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.G = 1000000#0.00000000006672
        self.groups = []

    def resolve_groups(self):
        self.groups.clear()
        the_last_index = self.objects.__len__()
        for i in range(0, the_last_index-1):
            for j in range(i+1, the_last_index):
                self.groups.append([i, j])
        print(self.groups)

    def step(self, surface):
        self.resolve_groups()
        '''for object in self.objects:
            # Calculating resultant force
            resultant_force = Vector2D(0, 0)
            distance_vector = Vector2D(0, 0)
            for other_object in self.objects:
                if other_object != object:
                    distance_vector = other_object.position - object.position
                    force = distance_vector.normalized() * (object.mass*other_object.mass)/distance_vector.length_squared() * self.G
                    resultant_force += force


            object.force = resultant_force
            object.velocity += object.force/object.mass * self.delta_time
            object.position += object.velocity * self.delta_time
            object.render(surface)'''
        # Applyinh forces
        for object in self.objects:
            object.velocity += object.force/object.mass * self.delta_time
            object.position += object.velocity * self.delta_time

            object.render(surface)
            object.force = Vector2D(0, 0)

        distance_vector = Vector2D(0, 0)
        for group in self.groups:
            distance_vector = self.objects[group[1]].position - self.objects[group[0]].position
            current_force = distance_vector.normalized() * (self.objects[group[0]].mass*self.objects[group[1]].mass)/distance_vector.length_squared() * self.G
            self.objects[group[0]].force += current_force
            self.objects[group[1]].force += -current_force

        self.delta_time = self.clock.tick(1000)/1000

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
