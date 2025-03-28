import pygame
import random
from utils import Particle
from quadtree import Quadtree, Boundary
from barnes_hut import compute_force_with_barnes_hut_algorithm

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Body Simulation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

NUM_PARTICLES = 10
particles = []
for _ in range(NUM_PARTICLES):
    particle = Particle(random.uniform(-50, 50), random.uniform(-50, 50), random.uniform(1, 10))
    particles.append(particle)

boundary = Boundary(0, 0, 50, 50)
dt = 0.1

while True:
    screen.fill(BLACK)

    quadtree = Quadtree(boundary)
    for particle in particles:
        quadtree.insert(particle)

    for particle in particles:
        particle.reset_acceleration()

    for particle in particles:
        force_x, force_y = compute_force_with_barnes_hut_algorithm(particle, quadtree)
        particle.apply_force(force_x, force_y)
        particle.update(dt)
    
    for particle in particles:
        x_screen = int((particle.x + 50) * (WIDTH / 100))
        y_screen = int((particle.y + 50) * (HEIGHT / 100))
        pygame.draw.circle(screen, WHITE, (x_screen, y_screen), max(2, int(particle.mass)))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()