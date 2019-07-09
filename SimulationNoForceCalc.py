import pygame
from pygame.locals import *
import random, math, sys
import numpy as np
pygame.init()

# width and height of the frame
width = 800
height = 600

# initializing the frame
Surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
Circles = []

class Circle:
    def __init__(self):
        # radius of the ball
        self.radius = 15
        # Random area of spawning but making sure that it is within the area
        self.x = random.randint(self.radius, width-self.radius-10)
        self.y = random.randint(self.radius, height-self.radius-10)
        # assigning mass based on radius
        self.mass = math.sqrt(self.radius)/2
        # scaling down speeds based on the mass of the particle and giving it a random value
        self.speedx = 1*(random.random()+1.0)/self.mass
        self.speedy = 1*(random.random()+1.0)/self.mass

# Same class as circle but with different mass
class BigCircle:
    def __init__(self):
        self.radius = 35
        # self.x = random.randint(self.radius, width-self.radius-10)
        # self.y = random.randint(self.radius, height-self.radius-10)
        self.x = 750
        self.y = 50
        self.mass = math.sqrt(self.radius)/2
        self.speedx = 1*(random.random()+1.0)/self.mass
        self.speedy = 1*(random.random()+1.0)/self.mass

# no of small or large circles required in simulation
no_of_small_circles = 80
no_of_large_circles = 1

# Creating small circles
for _ in range(no_of_small_circles):
    Circles.append(Circle())

# Creating big circles
for _ in range(no_of_large_circles):
    Circles.append(BigCircle())

# Function for circle collision
def CircleCollide(C1,C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.speedx = XSpeed
    C1.speedy = YSpeed

# Move function
def Move():
    for i,Circle in enumerate(Circles):

        if Circle.x > 700 or Circle.x < 100 or Circle.y > 500 or Circle.y < 100:
            Circle.x += 3*Circle.speedx 
            Circle.y += 3*Circle.speedy
        else:
            Circle.x += 2*Circle.speedx + np.random.normal(0,3,1)[0]
            Circle.y += 2*Circle.speedy + np.random.normal(0,3,1)[0]


        # (0,0) is at the bottom left corner instead of the top
        left_limit_x = Circle.x - Circle.radius
        right_limit_x = Circle.x + Circle.radius
        up_limit_y = Circle.y + Circle.radius
        down_limit_y = Circle.y - Circle.radius

        # use the commented logic if you want the smaller particles to disappear after the condition
        # if i < no_of_small_circles:
        #     if left_limit_x < 10 or right_limit_x > 790 or down_limit_y < 10 or up_limit_y > 590:
        #         Circle.x = random.randint(Circle.radius, width-Circle.radius-10)
        #         Circle.y = random.randint(Circle.radius, height-Circle.radius-10) 

        # else:
        #     if left_limit_x < 20 :
        #         print("1")
        #         Circle.x = Circle.x + 20
        #     elif right_limit_x > 780 :
        #         print("2")
        #         Circle.x = Circle.x - 20          
        #     elif up_limit_y > 580:
        #         print("3")
        #         Circle.y = Circle.y - 20            
        #     elif down_limit_y < 20:
        #         print("4")
        #         Circle.y = Circle.y + 20
        #     else:
        #         pass

        if left_limit_x < 20 :
            Circle.x = Circle.x + 20
        elif right_limit_x > 780 :
            Circle.x = Circle.x - 20          
        elif up_limit_y > 580:
            Circle.y = Circle.y - 20            
        elif down_limit_y < 20:
            Circle.y = Circle.y + 20
        else:
            pass


# Function for collision detection
def CollisionDetect():
    global detected
    for i,Circle in enumerate(Circles):
        if Circle.x-30 < Circle.radius or Circle.x > width-Circle.radius-30: 
               Circle.speedx *= -1
        if Circle.y-30 < Circle.radius or Circle.y > height-Circle.radius-30:  
                Circle.speedy *= -1
    for i,Circle in enumerate(Circles):
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    CircleCollide(Circle,Circle2)

# Function for drawing the circles
def Draw():
    Surface.fill((0,0,0))
    for Circle in Circles[:-no_of_large_circles]:
        pygame.draw.circle(Surface,(0,0,255),(int(Circle.x),int(height-Circle.y)),Circle.radius)
    for Circle in Circles[-no_of_large_circles:]:
        pygame.draw.circle(Surface,(255,0,0),(int(Circle.x),int(height-Circle.y)),Circle.radius)
    pygame.display.flip()

# Function for getting keyboard input
def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    while True:
        GetInput()
        Move()
        CollisionDetect()
        Draw()
        clock.tick(100)

if __name__ == '__main__': 
    main()
