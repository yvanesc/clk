import pygame
import os
import sys
import time
from time import localtime, strftime
pygame.init()
#loop
done = False
while done == False:

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
    
    #imgH1 = os.path.join("/home/pi/Documents/clkTest/nb/1.bmp")
    imgH1 = os.path.join("/nb/"+ strH1)
    imgH2 = os.path.join("./clk/nb/"+ strH2)
    imgM1 = os.path.join("./clk/nb/"+ strM1)
    #imgM2 = os.path.join("/home/pi/Documents/clkTest/nb/"+ strM2)
    imgM2 = os.path.join("./clk/nb/"+ strM2)
    #------------reverse order & rotate for screen ---------------------------------
    imgH1p = pygame.transform.rotate(pygame.image.load(imgM2).convert(),180)
    imgH2p = pygame.transform.rotate(pygame.image.load(imgM1).convert(),180)
    #pygame.image.load(imgH2).convert()
    imgM1p = pygame.transform.rotate(pygame.image.load(imgH2).convert(),180)
    imgM2p = pygame.transform.rotate(pygame.image.load(imgH1).convert(),180)
    
    screen.blit(imgH1p, (0, 0))
    screen.blit(imgH2p, (80, 0))
    screen.blit(imgM1p, (160, 0))
    screen.blit(imgM2p, (240, 0))

    pygame.display.update()
    time.sleep(10)
