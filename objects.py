from resources import image, item, object
import items
import pygame
import constants
import random

# This file has a bunch of object definitions
# These are different data types to represent the physical "things" in the level (excluding the player, cart, and stuff inside it)

# Holds a dictionary of paths to their respective loaded images, to save repeatedly loading the same thing
images: list[pygame.Surface] = {}

# Checks images for an already loaded image
# If it doesent exist it loads it from resources.py
def getImageFromCacheOrLoad(path):
    if not (path in images):
        #Load the image
        images[path] = image(path)
    return images[path]

# The thing on the shelf, generated in game.spawnItems, from the ItemSpawningGroups of the level
class StoreItem():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    # Draw this current item at its current position
    def draw(self, screen):
        screen.blit(getImageFromCacheOrLoad(item(self.itemType + ".png")), self.pos)
    
    # Get a rectangle of the item, the size is based from the image
    def getRect(self):
        imageDimensions = getImageFromCacheOrLoad(item(self.itemType + ".png")).get_size()
        return pygame.Rect(self.pos[0], self.pos[1], imageDimensions[0], imageDimensions[1])

# Pick a random index in the list (the last element is at the position 1 less than the length)
def pickRandomOfList(list):
    return list[random.randint(0, len(list) -1)]

class ItemSpawningGroup():
    # Takes in a list of bunch of positions for each item in the group, eg:
    # ItemSpawningGroup([ (810,68), (830,68),
    #                   (850,68), (870,68) ]),
    def __init__(self, positions: list[tuple]):
        self.positions = positions

    # Generate items for this group, returns a tuple of the name of the item that was generated, how much, and then the items
    def generateRandom(self) -> tuple[str, int, list[StoreItem]]:
        generatedItemType: str = pickRandomOfList(items.itemIds)
        generatedItemCount: int = len(self.positions)
        
        generatedItems: list[StoreItem] = []
        for position in self.positions:
            generatedItems.append(StoreItem(generatedItemType, position))

        return (generatedItemType, generatedItemCount, generatedItems)

# Functionally the same as the StoreItem, but is a different type since the uses are different 
class CollideableSprite():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    # Draw this current item at its current position
    def draw(self, screen):
        screen.blit(getImageFromCacheOrLoad(object(self.itemType + ".png")), self.pos)
    
    # Get a rectangle of the item, the size is based from the image
    def getRect(self):
        imageDimensions = getImageFromCacheOrLoad(object(self.itemType + ".png")).get_size()
        return pygame.Rect(self.pos[0], self.pos[1], imageDimensions[0], imageDimensions[1])

# Can be used as an alternative to the CollideableSprite, if you want to add collisions to something in a level that doesen't have an associated sprite 
class Collider():
    def __init__(self, pos: tuple[int, int], dimensions: tuple[int, int]):
        self.pos = pos
        self.dimensions = dimensions

    # Get a rectangle of the collider, the size is specified above
    def getRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])

# Used to mark an area on the map where the cart is cleared and items are counted as collected
class CheckoutArea():
    def __init__(self, min, max):
        self.rect = pygame.Rect(min[0], min[1], max[0], max[1])

    # Used to show a green outline to check the size is correct while developing
    def draw(self, screen):
        if (constants.RENDER_DEBUG_CHECKOUT_AREA):
            pygame.draw.rect(screen, (0, 255, 0), self.rect, width=5)

    # Checks if the player is within the area, if so, tell the game to collect the items in the cart
    # (the related game method is called sell but really means collect, its just a distinction between this, and collecting them from the shelf)
    def tick(self, game):
        playerPos = (game.playerX, game.playerY)
        if (self.rect.collidepoint(playerPos)):
            game.collectCartContents()
