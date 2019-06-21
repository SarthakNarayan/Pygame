import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

width = 800
height = 600
Surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

Circles = []
class Circle:
    def __init__(self):
        self.radius = 15
        self.x = random.randint(self.radius, width-self.radius-10)
        self.y = random.randint(self.radius, height-self.radius-10)
        self.mass = math.sqrt(self.radius)/2
        self.speedx = 2*(random.random()+1.0)/self.mass
        self.speedy = 2*(random.random()+1.0)/self.mass

class BigCircle():
    def __init__(self):
        self.radius = 35
        self.x = random.randint(self.radius, width-self.radius-10)
        self.y = random.randint(self.radius, height-self.radius-10)
        self.mass = math.sqrt(self.radius)/2
        self.speedx = 1*(random.random()+1.0)/self.mass
        self.speedy = 1*(random.random()+1.0)/self.mass
        
no_of_small_circles = 30
no_of_large_circles = 1
for _ in range(no_of_small_circles):
    Circles.append(Circle())

for _ in range(no_of_large_circles):
    Circles.append(BigCircle())

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
def Move():
    for Circle in Circles:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy
        # if (Circle.x + Circle.radius) >= width:
        #     for i in range (200):
        #         Circle.x -=Circle.speedx
        # if (Circle.x - Circle.radius) <= 0:
        #     for i in range (200):
        #         Circle.x +=Circle.speedx
        # if (Circle.y + Circle.radius) >= height:
        #     for i in range (200):
        #         Circle.y -=Circle.speedy
        # if (Circle.y - Circle.radius) <= 0:
        #     for i in range (200):
        #         Circle.y +=Circle.speedy


def CollisionDetect():
    for Circle in Circles:
        if Circle.x-10 < Circle.radius or Circle.x > width-Circle.radius-10:    Circle.speedx *= -1
        if Circle.y-10 < Circle.radius or Circle.y > height-Circle.radius-10:    Circle.speedy *= -1
    for Circle in Circles:
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    CircleCollide(Circle,Circle2)
def Draw():
    Surface.fill((0,0,0))
    for Circle in Circles[:-no_of_large_circles]:
        pygame.draw.circle(Surface,(0,0,255),(int(Circle.x),int(height-Circle.y)),Circle.radius)
    for Circle in Circles[-no_of_large_circles:]:
        pygame.draw.circle(Surface,(255,0,0),(int(Circle.x),int(height-Circle.y)),Circle.radius)
    pygame.display.flip()
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
        clock.tick(1000)
if __name__ == '__main__': 
    main()
