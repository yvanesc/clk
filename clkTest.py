import pygame
import os
import sys
import time
from time import localtime, strftime
pygame.init()

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((320, 240))
caption = pygame.display.set_caption("Digital Clock") 

screen = pygame.display.get_surface()
#--------------time
#print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
strH2 = strftime("%H", localtime())[1:]
strH2 = strH2 + ".bmp"
#imgH1 = os.path.join("/home/pi/Documents/clkTest/nb/1.bmp")
imgH1 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strH2)
imgH2 = os.path.join("/home/pi/Documents/clock/2.bmp")
imgM1 = os.path.join("/home/pi/Documents/clock/2.bmp")
imgM2 = os.path.join("/home/pi/Documents/clock/1.bmp")
#---------------------------------------------
imgH1 = pygame.image.load(imgH1).convert()
imgH2 = pygame.image.load(imgH2).convert()
imgM1 = pygame.image.load(imgM1).convert()
imgM2 = pygame.image.load(imgM2).convert()
screen.blit(imgH1, (0, 0))
screen.blit(imgH2, (80, 0))
screen.blit(imgM1, (160, 0))
screen.blit(imgM2, (660,0)) #(240, 0))

pygame.display.update()
time.sleep(10)
