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

shoppingListFontHeight = 25
shoppingListFont = pygame.font.Font('./font/CamingoCode-Regular.ttf', shoppingListFontHeight)

# Pick a random index in the list (the last element is at the position 1 less than the length)
def pickRandomOfList(list):
    return list[random.randint(0, len(list) -1)]

class Game():
    def __init__(self):
        # Allow other modules (such as the menus) to access the same scoreboard data instance
        self.scoreboardDataHandler = scoreboardDataHandler

        self.inGame = False
        self.isGameTicking = False

        self.initialiseAll()

        self.audio = True
        self.music = True

    # Set all variables to their defaults between games
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
        self.shoppingListEntries = {}
        self.collectedItems = []

        self.cartContents = []

    # Set all the variables from the current level
    def load(self):
        print("Started game from level")
        self.inGame = True
        self.awaitingNameInput = True
        self.initialiseAll()

        self.currentLevel = levelhandler.allLevels[self.currentLevelIndex]
        self.playerX = 535
        self.playerY = 417
        self.cartPos = (self.playerX, self.playerY)

        self.generateLevelItemsAndShoppingList()
        self.updateShoppingList()
        
        menuhandler.setMenu("nameInputMenu", self)

    # Start the game
    def start(self):
        self.awaitingNameInput = False
        self.isGameTicking = True
        self.levelStartTime = time.time()
        print("Recived Player name: " + self.playerName  + ("(empty so Unkown)" if self.playerName == "" else ""))
        menuhandler.back()

    def tickCartItems(self):
        # Calculate the speed effect of the cart (0-1 and based on how full the cart is) for the player
        self.cartSpeedModifier = (constants.CART_MAX_CAPACITY - len(self.cartContents)) / constants.CART_MAX_CAPACITY

        mousePos = pygame.mouse.get_pos()
        playerPos = (self.playerX, self.playerY)

        distance = calcMagnitude(sub(playerPos, mousePos))

        if distance < 75:
            for item in self.currentLevelItems:
                if len(self.cartContents) < constants.CART_MAX_CAPACITY and item.getRect().collidepoint(mousePos):
                    self.cartContents.append(CollectedItem(item))
                    self.currentLevelItems.remove(item)
    
    # Draw the items that are in the cart, thats it ig
    def drawCartItems(self, screen):
        for collectedItem in self.cartContents:
            collectedItem.draw(screen, self.cartPos)

    # Called when the player is inside the checkout area
    def collectCartContents(self):
        # Get all the items in the cart
        for collectedItem in self.cartContents:

            # Put it in the list for the recipt at the end
            self.collectedItems.append(collectedItem)

            # Tick them off shoping list if they are in it
            collectedType: str = collectedItem.item.itemType
            if collectedType in self.shoppingListEntries:
                self.shoppingListEntries[collectedType] -= 1
                
                if self.shoppingListEntries[collectedType] == 0:
                    del self.shoppingListEntries[collectedType]

        self.cartContents = []
        self.updateShoppingList()
        self.checkGameOver()

    #Check whether the shopping list is empty, and that the player then won
    def checkGameOver(self):
        if len(self.shoppingListEntries.keys()) == 0:
            game.isGameTicking = False
            menuhandler.setMenu("gameFinished", game)
            scoreboardDataHandler.put(game.playerName, math.floor((time.time() - game.levelStartTime) * 100))


    # Return the time passed since the start of the level, in seconds
    def getTimePassed(self):
        currentTime = time.time()
        return currentTime - self.levelStartTime

    # Return a text string for the stopwatch of the time since the start
    def getTimeText(self, ignoreGameTicking):
        if not ignoreGameTicking and not game.isGameTicking:
            return "00.00"
        
        remainingTime = self.getTimePassed()

        return "{:02}.{:02}".format(
            math.floor(remainingTime), # the time in seconds (rounded)
            math.floor((remainingTime %1) * 100) # the ms part of the time
            )
    
    # Accessor to the levels colliders
    def getCurrentLevelColliders(self):
        return self.currentLevel.getColliders()

    def generateLevelItemsAndShoppingList(self):
        # Get a copy of the spawning groups so we can remove stuff from it without worrying about modifying the level itself
        ungeneratedSpawningGroups: list[ItemSpawningGroup] = self.currentLevel.getLevelItemSpawningGroups().copy()

        # How many more items to add to the shopping list
        remainingShoppingListSpace: int = constants.MAX_SHOPPING_LIST_COUNT

        # Once each spawning group has its content generated its removed,
        # and this just loops until everything has been removed,
        # this way you can go randomly through it.

        # ...but ye be warned, while loops be dangerous terriory
        while len(ungeneratedSpawningGroups) != 0:
            spawnGroup: ItemSpawningGroup = pickRandomOfList(ungeneratedSpawningGroups)

            itemType, count, items = spawnGroup.generateRandom()
            
            # Make sure that the number added to the shopping list wont exceed the remaining space on it
            countOfItemsForShoppingList: int = min(count, remainingShoppingListSpace)

            if countOfItemsForShoppingList != 0:
                # Add the amount to the entry, or create the entry
                if itemType in self.shoppingListEntries:
                    self.shoppingListEntries[itemType] += countOfItemsForShoppingList
                else:
                    self.shoppingListEntries[itemType] = countOfItemsForShoppingList

            # Update the remaining space
            remainingShoppingListSpace -= countOfItemsForShoppingList
            
            # Add in all of the items
            self.currentLevelItems += items

            # Remove it from the ungenerated ones
            ungeneratedSpawningGroups.remove(spawnGroup)

    def updateShoppingList(self):
        self.shoppingListText = []

        for k in self.shoppingListEntries:
            self.shoppingListText.append(k + " x" + str(self.shoppingListEntries[k]))

    def drawShoppingList(self, screen):
        height = 100
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((423, 613 -(height + 20)), (423, height + 20)))

        yPos = 613-(height + 20)

        for line in self.shoppingListText:
            screen.blit(shoppingListFont.render(line, True, (0, 0, 0)), (430, yPos))
            yPos += shoppingListFontHeight + 5

    def toggleAudio(self):
        self.audio = not self.audio
        print("Toggled audio: " + str(self.audio))

    def toggleMusic(self):
        self.music = not self.music
        print("Toggled music: " + str(self.music))


game = Game()

menuhandler.setMenu("titleMenu", game)
timerBackground = image("timerbg.png")

running = True
while running:

    #Ticlomg stuff to update the game's components
    menuhandler.tickCurrent(game)

    if (game.inGame and game.isGameTicking):
        #Some things are only ticked when the game is running, and playing
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
        screen.blit(gameFont.render(game.getTimeText(False), False, (0, 0, 0)), (79, 19))

    menuhandler.drawCurrent(screen, game)

    # Event (input) handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        menuhandler.processCurrent(event, game)

    pygame.display.update()

pygame.quit()