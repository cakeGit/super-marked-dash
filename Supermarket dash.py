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
# Grape1 = pygame.image.load("grapes.png")
# WMelon = pygame.image.load("watermelon.png")
# Pep = pygame.image.load("Pepper.png")
# Carrot = pygame.image.load("carrots.png")
# Corn = pygame.image.load("Corn.png")
# SweetP = pygame.image.load("sweet-potato.png")
# Bread = pygame.image.load("bread.png")
# Butter = pygame.image.load("butter.png")
# Eggs = pygame.image.load ("egg.png")
# Milk = pygame.image.load ("milk.png")
# Syrup = pygame.image.load ("maple-syrup.png")
# Soda = pygame.image.load ("soda.png")
# Mango = pygame.image.load("mango.png")
# Onion = pygame.image.load("onion.png")
background = (255,255,0) 

userX_vel = 10
userY = 535   #player will not be moving on the X axis when they start
userX = 417   ##player will not be moving on the Y axis when they start



def movement():
    global userY, userX #F python

    pressedKeys = pygame.key.get_pressed()

    #Python lets you use true or false as equal to 1 or 0
    movementVector = (
        pressedKeys[pygame.K_d] - pressedKeys[pygame.K_a],
        pressedKeys[pygame.K_s] - pressedKeys[pygame.K_w]
    )
    #Up = (0, -1)
    #Down = (0, 1)
    #Left = (-1, 0)
    #Right = (1, 0)

    #normalise 🤓

    #Pythagorous
    magnitude = math.sqrt(pow(movementVector[0], 2) + pow(movementVector[1], 2))
    #Scale the vector

    if (magnitude != 0):
        movementVector = (movementVector[0]/magnitude, movementVector[1]/magnitude)

        movementSpeed = 5
        movementVector = (movementVector[0]*movementSpeed, movementVector[1]*movementSpeed)

        #Apply
        userX += movementVector[0]
        userY += movementVector[1]

#Store thhe images
itemIcons = {}

class StoreItem():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    #If the image is not loaded, load it and save to itemIcons, then draw
    def draw(self, screen):
        if not (self.itemType in itemIcons):
            #Load the image
            itemIcons[self.itemType] = pygame.image.load("items/" + self.itemType + ".png")
        screen.blit(itemIcons[self.itemType], self.pos)

#Remvove an item from here if you pick it up
items = [
    StoreItem("grapes", (810,27)),
    StoreItem("grapes", (830,27)),
    StoreItem("grapes", (850,27)),
    StoreItem("grapes", (870,27)),

    StoreItem("watermelon", (810,68)),
    StoreItem("watermelon", (830,68)),
    StoreItem("watermelon", (850,68)),
    StoreItem("watermelon", (870,68)),

    StoreItem("Pepper", (710,27)),
    StoreItem("Pepper", (730,27)),
    StoreItem("Pepper", (750,27)),
    StoreItem("Pepper", (770,27)),

    StoreItem("carrots", (710,68)),
    StoreItem("carrots", (730,68)),
    StoreItem("carrots", (750,68)),
    StoreItem("carrots", (770,68)),

    StoreItem("Corn", (615,27)),
    StoreItem("Corn", (635,27)),
    StoreItem("Corn", (655,27)),
    StoreItem("Corn", (675,27)),

    StoreItem("sweet-potato", (615,68)),
    StoreItem("sweet-potato", (635,68)),
    StoreItem("sweet-potato", (655,68)),
    StoreItem("sweet-potato", (675,68)),

    StoreItem("bread", (520,27)),
    StoreItem("bread", (540,27)),
    StoreItem("bread", (560,27)),
    StoreItem("bread", (580,27)),

    StoreItem("butter", (520,68)),
    StoreItem("butter", (540,68)),
    StoreItem("butter", (560,68)),
    StoreItem("butter", (580,68)),

    StoreItem("milk", (427,27)),
    StoreItem("milk", (447,27)),
    StoreItem("milk", (467,27)),
    StoreItem("milk", (487,27)),

    StoreItem("egg", (440,68)),
    StoreItem("egg", (480,68)),

    StoreItem("maple-syrup", (330,27)),
    StoreItem("maple-syrup", (350,27)),
    StoreItem("maple-syrup", (370,27)),
    StoreItem("maple-syrup", (390,27)),

    StoreItem("soda", (335,68)),
    StoreItem("soda", (355,68)),
    StoreItem("soda", (375,68)),
    StoreItem("soda", (395,68))
]

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

    for item in items:
        item.draw(screen)

    screen.blit(Player, (userX, userY))

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
 
# class character():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


#     #def draw

running = True
gameStarted = False

Background = pygame.image.load('menu background.png')
screen.blit(Background, (0,0))

def current_milli_time():
    return round(time.time() * 1000)

laggingNotifCooldown = 0
timeFactor = 1
while running:
    startTime = current_milli_time()
    #screen. fill((0, 0, 0))
    Pos = pygame.mouse.get_pos()

    #Game render loop
    if (gameStarted):
        draw()

    movement()

    for event in pygame.event.get():
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

    #calculate how long to sleep
    currentTime = current_milli_time()
    deltaTime = currentTime - startTime
    remainingFrameTime = 25 - deltaTime
    if (remainingFrameTime < 0):
        if laggingNotifCooldown == 0:
            laggingNotifCooldown = 50 #Dont scream every tick, it only makes it worse
            print("Game is lagging! (remaining frame time = " + str(remainingFrameTime) + ", total time = " + str(deltaTime) + ")")
        else:
            laggingNotifCooldown -= 1
    else:
        time.sleep(remainingFrameTime / 1000) #Convert to seconds
pygame.quit()
sys.exit()


    
