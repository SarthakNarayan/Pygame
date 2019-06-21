import pygame
import random
import math

background_colour = (0,0,0)
(width, height) = (800, 600)
# mass_of_air = 0.2
elasticity = 1
clock = pygame.time.Clock()

def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass, angle, 2*p2.speed*p2.mass/total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass, angle+math.pi, 2*p1.speed*p1.mass/total_mass)
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5*(p1.size + p2.size - dist+1)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap

class Particle():
    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.mass = mass
        # self.drag = (self.mass/(self.mass + mass_of_air)) ** self.size

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        # self.speed *= self.drag

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Brownian Motion Simulation')

number_of_particles_small = 100
number_of_particles_big = 1
my_particles = []

for _ in range(number_of_particles_small):
    size_small = 15
    density = 4
    mass = density*size_small**2
    x = random.randint(size_small, width-size_small)
    y = random.randint(size_small, height-size_small)

    particle = Particle(x, y, size_small, mass)
    particle.speed = 2*random.random()
    particle.angle = random.uniform(0, math.pi*2)

    my_particles.append(particle)

for _ in range(number_of_particles_big):
    size_big = 35
    density = 7
    mass = density*size_big**2
    x = random.randint(size_big, width-size_big)
    y = random.randint(size_big, height-size_big)

    particle = Particle(x, y, size_big, mass)
    particle.colour = (255, 0, 0)
    particle.speed = 2*random.random()
    particle.angle = random.uniform(0, math.pi*2)

    my_particles.append(particle)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

    screen.fill(background_colour)

    for i, particle in enumerate(my_particles):
        particle.move()
        particle.bounce()
        for particle2 in my_particles[i+1:]:
            collide(particle, particle2)
        particle.display()

    pygame.display.flip()
    # clock.tick(300)

pygame.quit()
quit()