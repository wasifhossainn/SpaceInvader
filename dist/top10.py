from __future__ import division #import __future__
import pygame #import pygame
import random #import random
from os import path #import path
from Score_Module import show_top10 #import score module

## assets folder
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sfx')

###############################
#define window size and fps
WIDTH = 1080
HEIGHT = 500
FPS = 60

#Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################
pygame.init() #initialize pygame
pygame.mixer.init() #For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set screen
pygame.display.set_caption("Top 10 Score") #set name of window
clock = pygame.time.Clock() #For syncing the FPS
###############################

font_name = pygame.font.match_font('arial') #set font

running = True #set running to true
while running: 

    clock.tick(FPS) # will make the loop run at the same speed all the time

    show_top10(screen, 'scores.txt') #call highscore module
    running = False #running is now false and now exit the program

        
pygame.quit() #quit

