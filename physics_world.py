from objects import *

class physics_world:
    def __init__(self):
        self.objects = []
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.G = 10000
        self.groups = []
        self.time_scale = 1

    def resolve_groups(self):
        self.groups.clear()
        the_last_index = self.objects.__len__()
        for i in range(0, the_last_index - 2):
            for j in range(i + 1, the_last_index - 1):
                    self.groups.append([i, j, (objects[i].radius + objects[j].radius)^2])

    def step(self, surface):

        # Applying forces
        for object in self.objects:
            object.velocity += object.force / object.mass * self.delta_time
            object.position += object.velocity * self.delta_time

            object.render(surface)
            object.force = Vector2D(0, 0)

        distance_vector = Vector2D(0, 0)
        for group in self.groups:
            distance_vector = self.objects[group[1]].position - self.objects[group[0]].position
            distance_squared = distance_vector.length_squared()
            if distance_squared <= self.objects[group[3]]:
                self.objects[group[0]].on_collision(self.objects[group[1]])
                self.objects[group[1]].on_collision(self.objects[group[0]])

            current_force = distance_vector.normalized() * (self.objects[group[0]].mass * self.objects[
            group[1]].mass) / distance_squared * self.G
            self.objects[group[0]].force += current_force
            self.objects[group[1]].force += -current_force

        self.delta_time = self.clock.tick(60) / 1000 * self.time_scale

    def add_object(self, object):
        self.objects.append(object)
        self.resolve_groups()

    def remove_object(self, object):
        self.objects.remove(object)
        self.resolve_groups()
