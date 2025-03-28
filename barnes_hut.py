from utils import *
import math

# gravitational constant 
G = 1

def calculate_gravitational_force(particle1, particle2):
    dx = particle2.x - particle1.x
    dy = particle2.y - particle1.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance == 0:
        return 0

    force = G * (particle1.mass * particle2.mass) / (distance**2)

    force_x = force * dx / distance
    force_y = force * dy / distance

    return force_x, force_y

def compute_force_with_barnes_hut_algorithm(particle, quadtree, theta=0.5):
    force_x = 0
    force_y = 0

    if quadtree.divided:
        for quadrant in [quadtree.northwest, quadtree.northeast, quadtree.southwest, quadtree.southeast]:
            if quadrant:
                if quadrant.boundary.width / (math.sqrt(particle.x**2 + particle.y**2)) < theta:
                    center_of_mass_x = quadrant.boundary.x
                    center_of_mass_y = quadrant.boundary.y
                    center_mass = sum([p.mass for p in quadrant.particles])
                    force_x_quadtree, force_y_quadtree = calculate_gravitational_force(particle, Particle(center_of_mass_x, center_of_mass_y, center_mass))
                    force_x += force_x_quadtree
                    force_y += force_y_quadtree
                else:
                    for p in quadrant.particles:
                        if p != particle:
                            force_x_part, force_y_part = calculate_gravitational_force(particle, p)
                            force_x += force_x_part
                            force_y += force_y_part
    return force_x, force_y        