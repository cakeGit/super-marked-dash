import pygame
from pygame.locals import*
import sys
import time
import random
import math
import os

# initiating pygame
pygame.init()

# creating display (x axis, y axis/ width, height)
screen = pygame.display.set_mode((900,613))
Floor = pygame.image.load('Floor.png')
Shelf = pygame.image.load("brownshelf2.png")
Cashier = pygame.image.load("cashier .png")
Island = pygame.image.load("BrownIsland.png")
RShelf = pygame.image.load("RotatedShelf.png")
Player = pygame.image.load("user.png")
Grape1 = pygame.image.load("grapes.png")
WMelon = pygame.image.load("watermelon.png")
Pep = pygame.image.load("Pepper.png")
Carrot = pygame.image.load("carrots.png")
Corn = pygame.image.load("Corn.png")
SweetP = pygame.image.load("sweet-potato.png")
Bread = pygame.image.load("bread.png")
Butter = pygame.image.load("butter.png")
Eggs = pygame.image.load ("egg.png")
Milk = pygame.image.load ("milk.png")
Syrup = pygame.image.load ("maple-syrup.png")
Soda = pygame.image.load ("soda.png")
Mango = pygame.image.load("mango.png")
Onion = pygame.image.load("onion.png")
background = (255,255,0) 

userX_vel = 10
userY = 535   #player will not be moving on the X axis when they start
userX = 417   ##player will not be moving on the Y axis when they start



def movement(event):
    global userY, userX #F python
        
    #if keys[pygame.K_LEFT]:   # if the key a is pressed, user should move to the left by one block
   #     print("work")
    #    userX -= userX_vel           
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_w:   # if the key w is pressed, user should more forward by one block
                print("w is prresed")
                userY = userY + 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:   # when the button is released we want the action to stop
                userY = 0
        
        if event.key == pygame.K_s:   # if the key s is pressed, user should move back one block
                userY = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:   # when the button is released we want the action to stop
                   userY = 0
        
        if event.key == pygame.K_d:   # if the key d is pressed, user should move to the right one block
            userX = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:   # when the button is released we want the action to stop
                userX = ACTIVEEVENT
    
    
def draw():
    screen.blit(Floor, (0, 0))
    screen.blit(Shelf, (803,27))
    screen.blit(Shelf, (708,27))
    screen.blit(Shelf, (613,27))
    screen.blit(Shelf, (518,27))
    screen.blit(Shelf, (423,27))
    screen.blit(Shelf, (328,27))
    screen.blit(Cashier, (0,200))
    screen.blit(Cashier, (0,300))
    screen.blit(Island, (260,308))
    screen.blit(Island, (260,210))
    screen.blit(Island, (450,210))
    screen.blit(Island, (450,308))
    screen.blit(RShelf, (824,210))
    screen.blit(RShelf, (824,307))
    screen.blit(RShelf, (824,404))    
    screen.blit(Player, (userX, userY))
    #screen blitting the grapes
    screen.blit(Grape1, (810,27))
    screen.blit(Grape1, (830,27))
    screen.blit(Grape1, (850,27))
    screen.blit(Grape1, (870,27))
    #screen blitting the melon
    screen.blit(WMelon, (810,68))
    screen.blit(WMelon, (830,68))
    screen.blit(WMelon, (850,68))
    screen.blit(WMelon, (870,68))
    #screen blitting the pepper 
    screen.blit(Pep, (710,27))
    screen.blit(Pep, (730,27))
    screen.blit(Pep, (750,27))
    screen.blit(Pep, (770,27))
    #screen blitting carrots 
    screen.blit(Carrot, (710,68))
    screen.blit(Carrot, (730,68))
    screen.blit(Carrot, (750,68))
    screen.blit(Carrot, (770,68))
    #screen blit corn
    screen.blit(Corn, (615,27))
    screen.blit(Corn, (635,27))
    screen.blit(Corn, (655,27))
    screen.blit(Corn, (675,27))
    #screen blit sweet potato
    screen.blit(SweetP, (615,68))
    screen.blit(SweetP, (635,68))
    screen.blit(SweetP, (655,68))
    screen.blit(SweetP, (675,68))

    #screen blit bread
    screen.blit(Bread, (520,27))
    screen.blit(Bread, (540,27))
    screen.blit(Bread, (560,27))
    screen.blit(Bread, (580,27))
    #screen blit butter
    screen.blit(Butter, (520,68))
    screen.blit(Butter, (540,68))
    screen.blit(Butter, (560,68))
    screen.blit(Butter, (580,68))

    #screen blit milk
    screen.blit(Milk, (427,27))
    screen.blit(Milk, (447,27))
    screen.blit(Milk, (467,27))
    screen.blit(Milk, (487,27))
    #screen blit egg
    screen.blit(Eggs, (440,68))
    screen.blit(Eggs, (480,68))

    #screen blit syrup
    screen.blit(Syrup, (330,27))
    screen.blit(Syrup, (350,27))
    screen.blit(Syrup, (370,27))
    screen.blit(Syrup, (390,27))
    #screen blit soda
    screen.blit(Soda, (335,68))
    screen.blit(Soda, (355,68))
    screen.blit(Soda, (375,68))
    screen.blit(Soda, (395,68))

    #screen blit onion
    #screen.blit(Onion, (,))
   # screen.blit(Onion, (,))

    #screen blit mango
    #screen.blit(Mango, (,))
   # screen.blit(Mango, (,))





    
    
    #if event.type == pygame.KEYDOWN:
       #if event.key == pygamne.K_ENTER:
            #screen.blit(background, (700,400), pygame.Rect(700, 400, 100, 100))
        
    
   

   
            ##if start_button == pygame.MOUSEBUTTONDOWN:
                ##if event.type == pygame.MOUSEBUTTONDOWN:
                    ##btn=pygame.mouse
                    ##screen. fill((0, 0, 0))

            #pygame.display.set_caption("start")
            #while running:
                #Start_mouse_pos = pygame.mouse.get_pos()
                #sc
    
    #screen. fill((0, 0, 0))
#Level1.Start()

#def settings():
    


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = image = pygame. transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def checkForInput(self, Pos):
        if Pos[0] in range(self.rect.left, self.rect.right) and Pos[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False                                        

    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        action = False
        
        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action
#Def Img
start_img = pygame.image.load('start.png')
settings_img = pygame.image.load('settings.png')
HighScore_img = pygame.image.load('HighScore.png')
Controls = pygame.image.load ("controls screen.png")
ControllerB = pygame.image.load ("ControllerButton.png")
SoundOn = pygame.image.load ("AudioOn.png")
SoundOff = pygame.image.load("AudioOff.png")
Back = pygame.image.load("return.png")

# create button instances
start_button = Button(212, 425, start_img, 0.8)
settings_button = Button(401, 425, settings_img, 0.8)
HighScore_button = Button(612, 425, HighScore_img, 0.8)
Controller_button = Button(200,310, ControllerB, 1)

    

def Settings():
    screen.fill((255, 255, 255))
    screen.blit(ControllerB, (210, 350))
    screen.blit(SoundOn, (440, 365))


    

    

#def HScore():

# This is my while loop for the menu screen

# i am going to replace this with the love hearts health icon
class HealthBar():
    def __init__(self, x, y, w, h, max_hp): # this is x, y coordinates, the width and the height of the rectangle and the max health points
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp # starts at full health
        self.max_hp = max_hp

    def draw(self,surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        #2 rectangles ontop of each other to create the health bar
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar (700,150,200,40,100) 
 
class character():
    def _init_(self, x, y):
        self.x = x
        self.y = y


    #def draw


        
running = True
gameStarted = True

Background = pygame.image.load('menu background.png')
screen.blit(Background, (0,0))
while running:
   
    #screen. fill((0, 0, 0))
    Pos = pygame.mouse.get_pos()

    #Game render loop
    if (gameStarted):
        draw()

    
    for event in pygame.event.get():
        movement(event)
        if event.type == pygame.QUIT:# red X makes the game Quit
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                ##btn=pygame.mouse

                if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                    gameStarted = True
                   ####### THIS IS TEMPORARY UNTIL I HAVE LEVELS 
                if settings_button.rect.collidepoint(pygame.mouse.get_pos()):
                    Settings()
                    ####### THIS IS TEMPORARY UNTIL I HAVE LEVELS 
                if HighScore_button.rect.collidepoint(pygame.mouse.get_pos()):
                    screen. fill((255, 255, 0))
                    ####### THIS IS TEMPORARY UNTIL I HAVE LEVELS 

        #draw the health bar -  put ths into
        health_bar.hp = 50 # makes the health bar to 50%
        ##health_bar.draw(screen)
        
        #telling the screen  to change if a change is detected
    pygame.display.update()
pygame.quit()
sys.exit()


    
