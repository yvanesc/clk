import pygame
import os
import sys

pygame.init()

screen = pygame.display.set_mode((320, 240))
caption = pygame.display.set_caption("Digital Clock") 

screen = pygame.display.get_surface()

imgH1 = os.path.join("/home/pi/Documents/clock/1.bmp")
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
screen.blit(imgM2, (240, 0))

pygame.display.update()
