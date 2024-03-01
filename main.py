import pygame
from pygame.locals import*
import sys
import math

import levelhandler
import menus
import menuhandler
from resources import image

# initiating pygame
pygame.init()

# creating display (x axis, y axis/ width, height)
screen = pygame.display.set_mode((900,613))

# image loading
Player = image("user.png")

background = (255,255,0)
rect = Player.get_rect()

userY = 535
userX = 417

movementVelocity = (0, 0)

def add(vector1, vector2):
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])

def mult(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)

def lerp(vector1, vector2, scalar):
    return add(mult(vector1, 1-scalar), mult(vector2, scalar))

def movement():
    global userY, userX, movementVelocity # global to use inside as well as out 

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

    #Pythagorous 
    magnitude = math.sqrt(pow(movementVector[0], 2) + pow(movementVector[1], 2))

    #Check we are moving
    if (magnitude != 0):
        
        #Normalise
        movementVector = mult(movementVector, 1/magnitude)

        movementSpeed = 2.5
        movementVector = mult(movementVector, movementSpeed)

        movementVelocity = lerp(movementVelocity, movementVector, 0.15)

        #Apply
        userX += movementVelocity[0]
        userY += movementVelocity[1]

    # if userX > 860 or userX < 0 or userY > 550 or userY < 0:  # if the user bumps into the borders then they re-spawn at position (400,400) this could be seen as another obstacle
    #     userX = 400
    #     userY = 400


def draw():
    game.currentLevel.drawBackground(screen)

    for item in game.currentLevelItems:
        item.draw(screen)

    screen.blit(Player, (userX, userY))

#Def Img
# start_img = image('start.png')
# settings_img = image('settings.png')
# HighScore_img = image('HighScore.png')
# Controls = image("controls screen.png")
# ControllerB = image("ControllerButton.png")
# SoundOn = image ("AudioOn.png")
# SoundOff = image("AudioOff.png")
# Back = image("return.png")

# create button instances
# start_button = Button(212, 425, start_img, 0.8)
# settings_button = Button(401, 425, settings_img, 0.8)
# HighScore_button = Button(612, 425, HighScore_img, 0.8)
# Controller_button = Button(200,310, ControllerB, 1)

# def Settings():
#     screen.fill((255, 255, 255))
#     screen.blit(ControllerB, (210, 350))
#     screen.blit(SoundOn, (440, 365))

#def HScore():

# This is my while loop for the menu screen

# i am going to replace this with the love hearts health icon
# class HealthBar():
#     def __init__(self, x, y, w, h, max_hp): # this is x, y coordinates, the width and the height of the rectangle and the max health points
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.hp = max_hp # starts at full health
#         self.max_hp = max_hp

#     def draw(self,surface):
#         #calculate health ratio
#         ratio = self.hp / self.max_hp
#         #2 rectangles ontop of each other to create the health bar
#         pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
#         pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

# health_bar = HealthBar (700,150,200,40,100)

# def loadLevel():
#     global currentLevelItems
#     currentLevelItems = currentLevel.createItemSetForGame()

running = True

class Game():
    def __init__(self):
        self.inGame = False
        self.currentLevelIndex = 0
        self.currentLevel = {}
        self.currentLevelItems = []

    def start(self):
        print("started game")
        self.inGame = True
        self.currentLevel = levelhandler.allLevels[self.currentLevelIndex]
        self.currentLevelItems = self.currentLevel.createItemSetForGame()


game = Game()

menuhandler.setMenu("titleMenu")

while running:
    menuhandler.drawCurrent(screen)

    #Game render loop
    if (game.inGame):
        draw()
    
    movement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menuhandler.processCurrent(event, game)

        # #draw the health bar -  put ths into
        # health_bar.hp = 50 # makes the health bar to 50%
        # ##health_bar.draw(screen)
    pygame.display.update()
pygame.quit()