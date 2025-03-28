import math

class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity_x_direction = 0
        self.velocity_y_direction = 0
        self.acceleration_x_direction = 0
        self.acceleration_y_direction = 0
    
    def apply_force(self, force_x, force_y):
        self.acceleration_x_direction += force_x / self.mass
        self.acceleration_y_direction += force_y / self.mass

    def update(selt, dt):
        self.velocity_x_direction += self.acceleration_x_direction * dt
        self.velocity_y_direction += self.acceleration_y_direction * dt
        self.x += self.velocity_x_direction * dt
        self.y += self.velocity_y_direction * dt
    
    def reset_acceleration(self):
        self.acceleration_x_direction = 0
        self.acceleration_y_direction = 0