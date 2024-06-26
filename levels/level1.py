from resources import image
from objects import *
from scoreboardDataHandler import ScoreboardDataHandler

# This file holds all the data for the first (and only level)

Floor = image('Floor.png')

itemSpawningGroups = [
    ItemSpawningGroup([(810,27), (830,27),
                      (850,27), (870,27)]),
    ItemSpawningGroup([(810,68), (830,68),
                      (850,68), (870,68)]),

    ItemSpawningGroup([(710,27), (730,27),
                      (750,27), (770,27)]),
    ItemSpawningGroup([(710,68), (730,68),
                      (750,68), (770,68)]),

    ItemSpawningGroup([(615,27), (635,27),
                      (655,27), (675,27)]),
    ItemSpawningGroup([(615,68), (635,68),
                      (655,68), (675,68)]),

    ItemSpawningGroup([(520,27), (540,27),
                      (560,27), (580,27)]),
    ItemSpawningGroup([(520,68), (540,68),
                      (560,68), (580,68)]),

    ItemSpawningGroup([(427,27), (447,27),
                      (467,27), (487,27)]),
    ItemSpawningGroup([(427,68), (447,68),
                      (467,68), (487,68)]),

    ItemSpawningGroup([(330,27), (350,27),
                      (370,27), (390,27)]),
    ItemSpawningGroup([(330,68), (350,68),
                      (370,68), (390,68)]),

    ItemSpawningGroup([(275, 200), (288, 200),
                      (275, 272), (288, 272),
                      (260, 220), (260, 240), (260, 260),
                      (305, 220), (305, 240), (305, 260)]),

    ItemSpawningGroup([(260, 320), (260, 340),
                      (260, 360), (305, 320),
                      (305, 340), (305, 360), (275, 305),
                      (288, 305), (275, 375), (288, 375)]),

    ItemSpawningGroup([(490, 220), (490, 240),
                      (490, 260), (450, 220),
                      (450, 240), (450, 260), (465, 200),
                      (475, 200), (465, 272), (475, 272)]),

    ItemSpawningGroup([(490, 320), (490, 340),
                      (490, 360), (450, 320),
                      (450, 340), (450, 360), (465, 305),
                      (475, 305), (465, 375), (475, 375)]),

    ItemSpawningGroup([(810,155), (830,155),
                      (850,155), (870,155),
                      (810,196), (830,196),
                      (850,196), (870,196)]),
    
    ItemSpawningGroup([(710,155), (730,155),
                      (750,155), (770,155),
                      (710,196), (730,196),
                      (750,196), (770,196)]),

    ItemSpawningGroup([(810,324), (830,324),
                      (850,324), (870,324),
                      (810,280), (830,280),
                      (850,280), (870,280)]),

    ItemSpawningGroup([(710, 324), (730, 324),
                      (750, 324), (770, 324),
                      (710, 280), (730, 280),
                      (750, 280), (770, 280)]),

    ItemSpawningGroup([(810, 408), (835, 408),
                      (860, 408), (810, 452),
                      (835, 452), (860, 452)]),

    ItemSpawningGroup([(720, 408), (745, 408),
                      (770, 408), (720, 452),
                      (745, 452), (770, 452)]),
]

checkoutAreas = [
    CheckoutArea((0, 150), (150, 350))
]

collideableSprites = [
    CollideableSprite("Shelf", (803,27)),
    CollideableSprite("Shelf", (708,27)),
    CollideableSprite("Shelf", (613,27)),
    CollideableSprite("Shelf", (518,27)),
    CollideableSprite("Shelf", (423,27)),
    CollideableSprite("Shelf", (328,27)),

    CollideableSprite("Checkout", (0,200)),
    CollideableSprite("Checkout", (0,300)),
    
    CollideableSprite("Island", (260,308)),
    CollideableSprite("Island", (260,210)),
    CollideableSprite("Island", (450,210)),
    CollideableSprite("Island", (450,308)),

    CollideableSprite("Shelf", (803,155)),
    CollideableSprite("Shelf", (708,155)),
    CollideableSprite("Shelf", (803,283)),
    CollideableSprite("Shelf", (708,283)),
    CollideableSprite("Shelf", (803,408)),
    CollideableSprite("Shelf", (708,408)),
]

# Add colliders for level obstacles like pillars, but there isnt any
colliders = [

]

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

scoreboardDataHandler = ScoreboardDataHandler("level-1")

def getScoreboardDataHandler():
    return scoreboardDataHandler

def getName():
    return "Level 1"