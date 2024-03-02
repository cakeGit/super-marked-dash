import pygame
from pygame.locals import *

import levelhandler
import menuhandler
import playerhandler
import random
import time
from mathutil import *
from resources import *
from objects import *

# initiating pygame
pygame.init()

pygame.font.init()
gameFont = pygame.font.SysFont('Comic Sans MS', 30)

# creating display (x axis, y axis/ width, height)
screen = pygame.display.set_mode((900,613))

def draw():
    game.currentLevel.drawBackground(screen)

    for item in game.currentLevelItems:
        item.draw(screen)

    playerhandler.drawPlayer(screen, game)

ANIMATION_TIME = 50
class CollectedItem():
    def __init__(self, item):
        self.collectedPos = item.pos
        self.item = item
        self.pos = item.pos
        self.remainingAnimationTicks = ANIMATION_TIME
        self.incartOffset = (random.random() * 40 -20, random.random() * 10 -5)
    
    def draw(self, screen, cartPos):
        cartPos = add(cartPos, self.incartOffset)
        if (self.remainingAnimationTicks > 0):
            self.remainingAnimationTicks-=1
            drawnPos = linearInterpolateVector(cartPos, self.collectedPos, self.remainingAnimationTicks / ANIMATION_TIME)
        else: drawnPos = cartPos
        self.item.pos = add(drawnPos, (0, -40))
        self.item.draw(screen)

    def getScore(self):
        return 15

CART_MAX_CAPACITY = 10

class Game():
    def __init__(self):
        self.inGame = False
        self.isTicking = False

        self.initialiseAll()

    def initialiseAll(self):
        self.remainingLevelTime = 0
        self.currentLevelIndex = 0
        self.currentLevel = {}
        self.currentLevelItems = []

        self.playerX = 0
        self.playerY = 0
        self.cartPos = (0, 0)
        self.cartSpeedModifier = 1

        self.score = 0

        self.cartContents = []

        self.audio = True
        self.music = True

    def start(self):
        print("Started game")
        self.inGame = True
        self.isTicking = True
        self.initialiseAll()

        self.currentLevel = levelhandler.allLevels[self.currentLevelIndex]
        self.currentLevelItems = self.currentLevel.createItemSetForGame()
        self.currentLevelTime = self.currentLevel.getLevelTime()
        self.levelStartTime = time.time()
        self.playerX = 535
        self.playerY = 417
        self.cartPos = (self.playerX, self.playerY)

    def toggleAudio(self):
        self.audio = not self.audio
        print("Toggled audio: " + str(self.audio))

    def toggleMusic(self):
        self.music = not self.music
        print("Toggled music: " + str(self.music))

    def tickCartItems(self):
        self.cartSpeedModifier = (CART_MAX_CAPACITY - len(self.cartContents)) / CART_MAX_CAPACITY

        mousePos = pygame.mouse.get_pos()
        playerPos = (self.playerX, self.playerY)

        distance = calcMagnitude(sub(playerPos, mousePos))

        if distance < 75:
            for item in self.currentLevelItems:
                if len(self.cartContents) < CART_MAX_CAPACITY and item.getRect().collidepoint(mousePos):
                    self.cartContents.append(CollectedItem(item))
                    self.currentLevelItems.remove(item)
    
    def drawCartItems(self, screen):
        for collectedItem in self.cartContents:
            collectedItem.draw(screen, self.cartPos)

    def sellCartContents(self):
        for collectedItem in self.cartContents:
            self.score += collectedItem.getScore()
        self.cartContents = []

    def getRemainingTime(self):
        currentTime = time.time()
        return (self.levelStartTime + self.currentLevelTime) - currentTime

    def getRemainingTimeText(self):
        remainingTime = self.getRemainingTime()
        if (remainingTime < 0):
            return "00.00"
        return "{:02}.{:02}".format(math.floor(remainingTime), math.floor((remainingTime %1) * 100))
    
    def getCurrentLevelColliders(self):
        return self.currentLevel.getColliders()
    

game = Game()

menuhandler.setMenu("titleMenu")
timerBackground = image("timerbg.png")

running = True
while running:
    if (game.inGame and game.isTicking):
        if(game.getRemainingTime() < 0):
            game.isTicking = False
            menuhandler.setMenu("gameFinished")

        playerhandler.updatePlayer(game)
        game.tickCartItems()
        for checkoutArea in game.currentLevel.getCheckoutAreas():
            checkoutArea.tick(game)

    #Game render loop
    if (game.inGame):
        draw()
        game.drawCartItems(screen)
        for checkoutArea in game.currentLevel.getCheckoutAreas():
            checkoutArea.draw(screen)
        screen.blit(timerBackground, (0, 0))
        screen.blit(gameFont.render(game.getRemainingTimeText(), False, (0, 0, 0)), (79, 19))

    menuhandler.drawCurrent(screen, game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        menuhandler.processCurrent(event, game)

        # #draw the health bar -  put ths into
        # health_bar.hp = 50 # makes the health bar to 50%
        # ##health_bar.draw(screen)
    pygame.display.update()
pygame.quit()