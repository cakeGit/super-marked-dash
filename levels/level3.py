from resources import image
from objects import *
from scoreboardDataHandler import ScoreboardDataHandler
import mathutil

# This file holds all the data for the first (and only level)

Floor = image('Floor.png')

itemSpawningGroups = [

]

checkoutAreas = [
    CheckoutArea((0, 478), (305, 135))
]

collideableSprites = [
    CollideableSprite("Checkout", (13, 497)),
    CollideableSprite("Checkout", (144,497)),
]

# Add colliders for level obstacles like pillars, but there isnt any
colliders = [

]

def addSpawningGroupAtPosition(position, offsets):
    positions = []
    for offset in offsets:
        positions.append(mathutil.add(position, offset))
    itemSpawningGroups.append(ItemSpawningGroup(positions))
    

def createShelfComponent(position):
    collideableSprites.append(CollideableSprite("Shelf", position))
    addSpawningGroupAtPosition(position, [
        (6, 5), (36, 5), (66, 5),
        (6, 45), (36, 45), (66, 45)
    ])

def createIslandComponent(position):
    collideableSprites.append(CollideableSprite("Island", position))
    addSpawningGroupAtPosition(position, [
        (3, 11), (3, 37), (3, 63),
        (40, 11), (40, 37), (40, 63),
        (23, 1), (23, 67),
    ])

# Components are used to quickly create the item spawning groups and collideable sprites in one go, saving so much pain...
# Row 1
createShelfComponent((256, 39))
createShelfComponent((353, 39))
createShelfComponent((450, 39))
createShelfComponent((547, 39))

# Row 2
createShelfComponent((256, 154))
createShelfComponent((353, 154))
createShelfComponent((450, 154))

# Row 3
createShelfComponent((159, 269))
createShelfComponent((256, 269))
createShelfComponent((353, 269))

createShelfComponent((547, 269))
createShelfComponent((644, 269))
createShelfComponent((741, 269))

# Row 4
createShelfComponent((62, 384))
createShelfComponent((159, 384))

createShelfComponent((353, 384))
createShelfComponent((450, 384))
createShelfComponent((547, 384))
createShelfComponent((644, 384))
createShelfComponent((741, 384))

# Islands
createIslandComponent((73, 143))
createIslandComponent((703, 46))
createIslandComponent((703, 143))

# Called to draw the background, the level is also responsible for drawing the sprites inside it
def drawBackground(screen):
    screen.blit(Floor, (0, 0))
    for sprite in collideableSprites:
        sprite.draw(screen)

# These functions are used by the game to access the variables above in a standard way

def getLevelItemSpawningGroups():
    return itemSpawningGroups

# Include both types of collider
def getColliders():
    return collideableSprites + colliders

def getCheckoutAreas():
    return checkoutAreas

scoreboardDataHandler = ScoreboardDataHandler("level-3")

def getScoreboardDataHandler():
    return scoreboardDataHandler

def getName():
    return "Level 3"