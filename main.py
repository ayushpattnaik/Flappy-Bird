import random 
import sys
import pygame
from pygame.locals import *


#Global var for game
FPS= 32
SCREENWIDTH= 289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.6
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='/Gallery/Sprites/bird.png'
BACKGROUND='/Gallery/Sprites/bg.png'
PIPE='/Gallery/Sprites/pipe.png'

def welcomeScreen():
    pass

if __name__ == '__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers']=(
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),


    )
    GAME_SPRITES['base']=pygame.image.load('').convert_alpha()
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(PIPE,180),
        pygame.image.load(PIPE).convert_alpha()
    )
    #Game sounds

    GAME_SOUNDS['die']=pygame.mixer.Sound('');
    GAME_SOUNDS['hit']=pygame.mixer.Sound('');
    GAME_SOUNDS['point']=pygame.mixer.Sound('');
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('');
    GAME_SOUNDS['wing']=pygame.mixer.Sound(''); 
    
    GAME_SPRITES['message']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame()


   

    

    



