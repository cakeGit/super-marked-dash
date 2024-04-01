import pygame
import scoreboardDataHandler
from pygame.locals import *
import particles

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
# Using a different font to gamefont since the font heights may be diffent
shoppingListFont = pygame.font.SysFont('Comic Sans MS', shoppingListFontHeight)

# Pick a random index in the list (the last element is at the position 1 less than the length)
def pickRandomOfList(list):
    return list[random.randint(0, len(list) -1)]

class Game():
    def __init__(self):
        # Allow other modules (such as the menus) to access the same scoreboard data instance
        self.inGame = False
        self.isGameTicking = False

        self.initialiseAll()

        self.audio = True
        self.music = True

    # Set all variables to their defaults between games
    def initialiseAll(self):
        self.awaitingNameInput = False
        self.remainingLevelTime = 0
        self.totalScore = 0
        self.currentLevel = {}
        self.currentLevelItems = []

        self.playerX = 0
        self.playerY = 0
        self.cartPos = (0, 0)
        self.cartRemainingPercent = 1
        self.playerName = ""
        self.levelStartTime = 0
        self.shoppingListDisplay = []
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

        self.lastLevelScoreboard = self.currentLevel.getScoreboardDataHandler()
        self.lastLevelName = self.currentLevel.getName()
        
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
        self.cartRemainingPercent = (constants.CART_MAX_CAPACITY - len(self.cartContents)) / constants.CART_MAX_CAPACITY

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
        # If we have won
        if len(self.shoppingListEntries.keys()) == 0:
            # Stop ticking the game
            game.isGameTicking = False
            # Clear all particles
            particles.clear()
            # Go to the game over menu
            menuhandler.setMenu("gameFinishedMenu", game)
            # Save our score
            self.lastLevelScoreboard.put(game.playerName, math.floor((time.time() - game.levelStartTime) * 100))


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
        # Simplified to just grab a random set of items, instead of whole groups to get a more varied shopping list
        
        # Get a copy of the spawning groups so we can remove stuff from it without worrying about modifying the level itself
        spawningGroups = self.currentLevel.getLevelItemSpawningGroups().copy()

        # Loop through all spawning groups in the level and generate the items
        for spawningGroup in spawningGroups:
            self.currentLevelItems += spawningGroup.generateRandom()
        
        # Randomise the order (since items is currently in order of spawning)
        # Also do this on a seperate list since the order of currentLevelItems results in items rendering differently
        # which results in it being random and not as neat
        randomisedItemList = self.currentLevelItems.copy()
        random.shuffle(randomisedItemList)

        # Grab the first (MAX_SHOPPING_LIST_COUNT) number of items or the whole list if it is not big enough
        shoppingListItems = self.currentLevelItems[0 : min(len(self.currentLevelItems), constants.MAX_SHOPPING_LIST_COUNT) -1]

        for shoppingListItem in shoppingListItems:
            # store the item type as a local variable to save writing the full name
            itemType = shoppingListItem.itemType

            # Add a number to an entry to track how much of this entry is on the list
            if not itemType in self.shoppingListEntries:
                self.shoppingListEntries[itemType] = 0

            self.shoppingListEntries[itemType] += 1

    def updateShoppingList(self):
        # Clear all entries since they will be remade
        self.shoppingListDisplay = []

        # Itterate all the items to be collected
        for k in self.shoppingListEntries:
            #Put the current item ID (used to generate an icon), then the text to be displayed after, packaged as an array
            self.shoppingListDisplay.append([ k, (k + " x" + str(self.shoppingListEntries[k])) ])

    def drawShoppingList(self, screen):
        # How tall the list should be, it covers alot of the level so dont make it too high
        height = 100
        # Draw the white "paper" background
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((423, 613 -(height + 20)), (423, height + 20)))

        # calculate the position of the first line
        yPos = 613 -(height + 20)

        for entry in self.shoppingListDisplay:

            # If we have gone over the screen height
            if (yPos > 613):
                break # Skip rendering the rest to save on lag

            # Draw the item icon to help the player find it
            screen.blit(
                pygame.transform.scale(
                    getImageFromCacheOrLoad(item(entry[0] + ".png")), # Get the image for the current entry
                    (20, 20) #Set the size since the icon needs to be a little smaller
                    ),
                (430, yPos +10))

            # Render the text - Defined by main.py#updateShoppingList
            screen.blit(shoppingListFont.render(entry[1], True, (0, 0, 0)), (450, yPos))
            # Move to the next line
            yPos += shoppingListFontHeight + 5

    # Called by the settings menu to change audio / music enabled
    def toggleAudio(self):
        self.audio = not self.audio
        print("Toggled audio: " + str(self.audio))

    # Called by the settings menu to change audio / music enabled
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
        playerhandler.updatePlayer(game, particles)
        game.tickCartItems()
        particles.tick()
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
        particles.draw(screen)

    menuhandler.drawCurrent(screen, game)

    # Event (input) handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        menuhandler.processCurrent(event, game)

    pygame.display.update()

pygame.quit()