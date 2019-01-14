import pygame
import math

####
#Every controller is numbered differently
####

# For initializing pygame
pygame.init()
# For initializing the joystick
pygame.joystick.init()

# Checking the number of joystick present
# 0 means no joystick present
print(pygame.joystick.get_count())

# assign the first controller
joystick = pygame.joystick.Joystick(0)

# initialize the first controller for reading
joystick.init()  

# return the number of axes on the controller
numaxes = joystick.get_numaxes()
print("The number of axis are" , numaxes)

#Pygame calls the digital inputs by the term buttons
#The button values are 0 = not pressed and 1 = pressed
numbuttons = joystick.get_numbuttons()
print("The number of buttons are" , numbuttons)

# returns the number of hats
hats = joystick.get_numhats()
print("The number of hats are" , hats)

# returns the number of hats
balls = joystick.get_numballs()
print("The number of balls are" , balls)

JoyName = pygame.joystick.Joystick(0).get_name()
print("Name of the joystick:")
print(JoyName)

def getAxis(number):
    # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
    # so this is used not "if joystick value not zero"
    if(joystick.get_axis(number) < -0.1 or joystick.get_axis(number) > 0.1):
      
      # different ways of increasing the resolution
      # method 1
      #nos = int(round((joystick.get_axis(number)+1)/2.0 * 1023)) 
      
      # method 2
      sign = joystick.get_axis(number)/abs(joystick.get_axis(number))
      nos = sign*math.log(9*abs(joystick.get_axis(number)) + 1)/2.303

      print("Axis value is %s" %nos)
      print("Axis ID is %s" %(number))

def getButton(number):
    # returns 1 or 0 - pressed or not
    if(joystick.get_button(number)):
      # just prints id of button
      print("Button ID is %s" %(number))

def getHat(number):
    if joystick.get_hat(number) != (0,0):
      # returns tuple with values either 1, 0 or -1
      print( "Hat value is %s, %s" %(joystick.get_hat(number)[0],joystick.get_hat(number)[1]))
      print ("Hat ID is %s" %(number))


# For getting the numbering of the keys
while True:
#    for event in pygame.event.get(): 
#        if event.type == pygame.QUIT: 
#                pass

# There are events in the joystick
# these are JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
# we need to continously pump them
    pygame.event.pump()
    for i in range(numaxes):
        getAxis(i)
    for i in range(numbuttons):
        getButton(i)
    for i in range(hats):
        getHat(i)

    

