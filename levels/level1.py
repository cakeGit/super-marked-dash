from resources import image
from objects import *

Floor = image('Floor.png')
# Shelf = image("brownshelf2.png")
# Cashier = image("cashier .png")
# Island = image("BrownIsland.png")

#This was getting a bit to long so i put it in this file, also you should maybe make a function to make these
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
    StoreItem("soda", (395,68)),

    StoreItem("onion", (275, 200)),
    StoreItem("onion", (288, 200)),

    StoreItem("onion", (275, 272)),
    StoreItem("onion", (288, 272)),

    StoreItem("onion", (260, 220)),
    StoreItem("onion", (260, 240)),
    StoreItem("onion", (260, 260)),


    StoreItem("onion", (305, 220)),
    StoreItem("onion", (305, 240)),
    StoreItem("onion", (305, 260)),


    StoreItem("orange", (260, 320)),
    StoreItem("orange", (260, 340)),
    StoreItem("orange", (260, 360)),

    StoreItem("orange", (305, 320)),
    StoreItem("orange", (305, 340)),
    StoreItem("orange", (305, 360)),

    StoreItem("orange", (275, 305)),
    StoreItem("orange", (288, 305)),

    StoreItem("orange", (275, 375)),
    StoreItem("orange", (288, 375)),

    StoreItem("strawberry", (490, 220)),
    StoreItem("strawberry", (490, 240)),
    StoreItem("strawberry", (490, 260)),

    StoreItem("strawberry", (450, 220)),
    StoreItem("strawberry", (450, 240)),
    StoreItem("strawberry", (450, 260)),

    StoreItem("strawberry", (465, 200)),
    StoreItem("strawberry", (475, 200)),

    StoreItem("strawberry", (465, 272)),
    StoreItem("strawberry", (475, 272)),

    StoreItem("coconut", (490, 320)),
    StoreItem("coconut", (490, 340)),
    StoreItem("coconut", (490, 360)),

    StoreItem("coconut", (450, 320)),
    StoreItem("coconut", (450, 340)),
    StoreItem("coconut", (450, 360)),

    StoreItem("coconut", (465, 305)),
    StoreItem("coconut", (475, 305)),

    StoreItem("coconut", (465, 375)),
    StoreItem("coconut", (475, 375)),

    StoreItem("instant-noodles", (810,155)),
    StoreItem("instant-noodles", (830,155)),
    StoreItem("instant-noodles", (850,155)),
    StoreItem("instant-noodles", (870,155)),

    StoreItem("instant-noodles", (810,196)),
    StoreItem("instant-noodles", (830,196)),
    StoreItem("instant-noodles", (850,196)),
    StoreItem("instant-noodles", (870,196)),
    
    StoreItem("soy", (710,155)),
    StoreItem("soy", (730,155)),
    StoreItem("soy", (750,155)),
    StoreItem("soy", (770,155)),

    StoreItem("soy", (710,196)),
    StoreItem("soy", (730,196)),
    StoreItem("soy", (750,196)),
    StoreItem("soy", (770,196)),

    StoreItem("pasta", (810,324)),
    StoreItem("pasta", (830,324)),
    StoreItem("pasta", (850,324)),
    StoreItem("pasta", (870,324)),

    StoreItem("pasta", (810,280)),
    StoreItem("pasta", (830,280)),
    StoreItem("pasta", (850,280)),
    StoreItem("pasta", (870,280)),

    StoreItem("tomato", (710, 324)),
    StoreItem("tomato", (730, 324)),
    StoreItem("tomato", (750, 324)),
    StoreItem("tomato", (770, 324)),

    StoreItem("tomato", (710, 280)),
    StoreItem("tomato", (730, 280)),
    StoreItem("tomato", (750, 280)),
    StoreItem("tomato", (770, 280)),

    StoreItem("chocolate", (810, 408)),
    StoreItem("chocolate", (835, 408)),
    StoreItem("chocolate", (860, 408)),

    StoreItem("chocolate", (810, 452)),
    StoreItem("chocolate", (835, 452)),
    StoreItem("chocolate", (860, 452)),

    StoreItem("chocBag", (720, 408)),
    StoreItem("chocBag", (745, 408)),
    StoreItem("chocBag", (770, 408)),

    StoreItem("chocBag", (720, 452)),
    StoreItem("chocBag", (745, 452)),
    StoreItem("chocBag", (770, 452)),
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

# Add colliders for level obstacles like pillars
colliders = [

]

def createItemSetForGame():
    newItems = []
    for item in items:
        newItems.append(item.clone())
    return newItems

def getColliders():
    return collideableSprites + colliders

def getCheckoutAreas():
    return checkoutAreas

# Time in seconds that the player will have while ingame
def getLevelTime():
    return 60

def drawBackground(screen):
    screen.blit(Floor, (0, 0))
    for sprite in collideableSprites:
        sprite.draw(screen)