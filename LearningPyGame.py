import pygame
import time
import random
import cv2

image = pygame.image.load(r"C:\Users\Lenovo\Desktop\mypic1.jpg")

# defining the colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
# initializes pygame
pygame.init()
Display = pygame.display.set_mode((800,600))
# Name of the window
pygame.display.set_caption("Brownian Motion Simulation")

def message(msg , color):
    font = pygame.font.SysFont(None , 50)
    screen_text = font.render(msg , True , color)
    Display.blit(screen_text , [100 , 100])

clock = pygame.time.Clock()
playGame = True
i = 0

fruitx = 0
fruity = 0
# While is our game handling loop
while playGame:
    # for is our event handling group
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        if event.type == pygame.KEYDOWN:
            fruitx = random.randrange( 0 , 500)
            fruity = random.randrange( 0 , 500)
            if event.key == pygame.K_LEFT:
                i = i - 10
            if event.key == pygame.K_RIGHT:
                i = i +10 
            if event.key == pygame.K_q:
                playGame = False
                message("Quitting the game" , red)
                pygame.display.update()
                time.sleep(2)
                

    # To fill the background with that specific color
    Display.fill(white)
    pygame.draw.rect(Display , black , [400+i,300,100,84])
    # Using your own picture
    Display.blit(image , (400+i , 300))
    pygame.draw.rect(Display , red , [fruitx,fruity,10,10])
    # or you can use Display.fill(black , rect = [])
    # The commented method will be faster
    pygame.display.update()
    # to control the frames per second
    clock.tick(15)

# to uninitialize the pygame
pygame.quit()
quit()