import serial

#Required to use delay functions
import time
import pygame

# com port number and the baud rate
arduinoData = serial.Serial('com17' , 9600)

# hold the program for two seconds to establish the communication
time.sleep(2)

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init() 

# The following line will read anything coming from Arduino and 
# will print it on the shell window
print(arduinoData.readline())

while True:
    pygame.event.pump()
    
    numberA = joystick.get_button(0)
    numberB = joystick.get_button(1)
    numberX = joystick.get_button(2)
    numberY = joystick.get_button(3)
    analog = joystick.get_axis(0)
    analog = int(round((analog+1)/2.0 * 1023))
    
    s= str(numberA) + '\t' + str(numberB) + '\t' + str(numberX) + '\t' + str(numberY) + '\t' + str(analog) +'\n'
    arduinoData.write(s.encode())

        