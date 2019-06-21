import pygame
import random
import math

def inititialization(width = 800 , height = 600):
    '''
    For initializing the pygame window

    Args: 
    width: To set the window width. Default = 800
    height : To set window hright. Default = 600
    '''
    pygame.init()
    inititialization.display_width = width
    inititialization.display_height = height
    inititialization.Display = pygame.display.set_mode(( inititialization.display_width, inititialization.display_height))
    pygame.display.set_caption("Brownian Motion Simulation")
    inititialization.Brownian = True
    inititialization.clock = pygame.time.Clock()
    inititialization.colors = {"white":(255,255,255) , "blue":(0,0,255) , 
                "red":(255,0,0) , "green":(0,255,0) , "black":(0,0,0)}
    inititialization.Display.fill(inititialization.colors["white"])
    pygame.display.update()

def gameloop():
    '''
    This is the gameloop having the while loop and interfacing all events

    Args: None
    '''
    radius = 10
    angle = random.uniform(0, math.pi*2)
    print(angle)
    inititialization()
    x = random.randint(radius, inititialization.display_width-radius)
    y = random.randint(radius, inititialization.display_height-radius)
    obj= objects(400,400,angle,radius,10)
    while inititialization.Brownian:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inititialization.Brownian = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    inititialization.Brownian = False
        
        inititialization.Display.fill(inititialization.colors["white"])
        obj.move(10)
        obj.bounce()
        pygame.display.update()
        # More the number faster is the object
        # More the frame rate the smoother it is
        inititialization.clock.tick(100)

class objects:
    '''
    This class is for drawing objects like circle , square , polygons , line

    Args:
    '''
    def __init__(self , x , y , angle ,radius,speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.speed = speed

    def addvectors(self , angle1, length1, angle2, length2):
        x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
        length = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y, x)
        return (angle, length)

    def move(self , thickness):
        gravity = (math.pi, 0.002)
        (self.angle, self.speed) = self.addvectors(self.angle, self.speed, math.pi , 0.002)
        self.x += int(math.sin(self.angle) * self.speed)
        self.y -= int(math.cos(self.angle) * self.speed)
        drag = 0.999
        pygame.draw.circle(inititialization.Display, (255,0,255), (self.x, self.y), self.radius, thickness)
        self.speed *= drag
    def bounce(self):
        elasticity = 0.75
        if self.x > inititialization.display_width - self.radius:
            self.x = 2 * (inititialization.display_width - self.radius) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.radius:
            self.x = 2 * self.radius - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > inititialization.display_height - self.radius:
            self.y = 2 * (inititialization.display_height - self.radius) - self.y
            self.speed *= elasticity
            self.angle = math.pi - self.angle
        elif self.y < self.radius:
            self.y = 2 * self.radius - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

def main():
    gameloop()     
if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
