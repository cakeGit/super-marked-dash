import pygame
import scoreboardDataHandler
from pygame.locals import *

# initiating pygame
pygame.init()
pygame.font.init()

gameFont = pygame.font.SysFont('Comic Sans MS', 30)

import levelhandler
import menuhandler
import playerhandler
import random
import time
from mathutil import *
from resources import *
from objects import *

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

fontheight = 25
reciptFont = pygame.font.Font('./font/CamingoCode-Regular.ttf', fontheight)
class Game():
    def __init__(self):
        # Allow other modules (such as the menus) to access the same scoreboard data instance
        self.scoreboardDataHandler = scoreboardDataHandler

        self.inGame = False
        self.isGameTicking = False

        self.initialiseAll()

    def initialiseAll(self):
        self.awaitingNameInput = False
        self.remainingLevelTime = 0
        self.currentLevelIndex = 0
        self.totalScore = 0
        self.currentLevel = {}
        self.currentLevelItems = []

        self.playerX = 0
        self.playerY = 0
        self.cartPos = (0, 0)
        self.cartSpeedModifier = 1
        self.playerName = ""
        self.levelStartTime = 0
        self.shoppingListText = []
        self.shoppingList = []

        self.collectedItems = []

        self.cartContents = []

        self.audio = True
        self.music = True

    def load(self):
        print("Started game")
        self.inGame = True
        self.awaitingNameInput = True
        self.initialiseAll()

        self.currentLevel = levelhandler.allLevels[self.currentLevelIndex]
        self.currentLevelItems = self.currentLevel.createItemSetForGame()
        self.currentLevelTime = self.currentLevel.getLevelTime()
        self.shoppingList = self.currentLevelItems
        self.playerX = 535
        self.playerY = 417
        self.cartPos = (self.playerX, self.playerY)
        self.updateShoppingList()
        menuhandler.setMenu("nameInputMenu", self)

    def start(self):
        self.awaitingNameInput = False
        self.isGameTicking = True
        self.levelStartTime = time.time()
        print("Player name: " + self.playerName)
        menuhandler.back()

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
            self.collectedItems.append(collectedItem)
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
    
    def calculateTotalScore(self):
        self.totalScore = 0

        for collectedItem in game.collectedItems:
            self.totalScore += collectedItem.getScore()

    def updateShoppingList(self):
        self.shoppingListText = []

        shoppingListEntries = {}

        for i in self.shoppingList:
            name = i.itemType
            if name not in shoppingListEntries:
                shoppingListEntries[name] = 0
            else:
                shoppingListEntries[name] += 1

        for k in shoppingListEntries:
            self.shoppingListText.append(k + " x" + str(shoppingListEntries[k]))

    def drawShoppingList(self, screen):

        height = 100
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((423, 613 -(height + 20)), (423, height + 20)))

        yPos = 613-(height + 20)

        for line in self.shoppingListText:
            screen.blit(reciptFont.render(line, True, (0, 0, 0)), (430, yPos))
            yPos += fontheight + 5

    

game = Game()

menuhandler.setMenu("titleMenu", game)
timerBackground = image("timerbg.png")

running = True
while running:
    menuhandler.tickCurrent(game)

    if (game.inGame and game.isGameTicking):
        if(game.getRemainingTime() < 0):
            game.isGameTicking = False
            game.calculateTotalScore()
            menuhandler.setMenu("gameFinished", game)
            scoreboardDataHandler.put(game.playerName, game.totalScore)

        playerhandler.updatePlayer(game)
        game.tickCartItems()
        for checkoutArea in game.currentLevel.getCheckoutAreas():
            checkoutArea.tick(game)

    #Game render loop
    if (game.inGame):
        draw()
        game.drawCartItems(screen)
        game.drawShoppingList(screen)
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