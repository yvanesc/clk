import pygame
import os
import sys
import time
from time import localtime, strftime
pygame.init()

#while 

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((320, 240))
caption = pygame.display.set_caption("Digital Clock") 

screen = pygame.display.get_surface()
#--------------time
#print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
strH1 = strftime("%H", localtime())[:1]+ ".bmp"
strH2 = strftime("%H", localtime())[1:]+ ".bmp"
strM1 = strftime("%M", localtime())[:1]+ ".bmp"
strM2 = strftime("%M", localtime())[1:]+ ".bmp"
print(strM2)
#imgH1 = os.path.join("/home/pi/Documents/clkTest/nb/1.bmp")
imgH1 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strH1)
imgH2 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strH2)
imgM1 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strM1)
imgM2 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strM2)
#---------------------------------------------
imgH1 = pygame.image.load(imgH1).convert()
imgH2 = pygame.image.load(imgH2).convert()
imgM1 = pygame.image.load(imgM1).convert()
imgM2 = pygame.image.load(imgM2).convert()
screen.blit(imgH1, (0, 0))
screen.blit(imgH2, (80, 0))
screen.blit(imgM1, (160, 0))
screen.blit(imgM2, (240, 0))

pygame.display.update()
time.sleep(10)
