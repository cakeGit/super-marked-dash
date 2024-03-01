from resources import image, item, object
import pygame

# Physical object types, such as store items, or the shelves that can be collided with

# STORE ITEMS

#Cache the images save loading them repeatedly
images = {}

def safeGetImage(path):
    if not (path in images):
        #Load the image
        images[path] = image(path)
    return images[path]

class StoreItem():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    #If the image is not loaded, load it and save to itemIcons, then draw
    def draw(self, screen):
        screen.blit(safeGetImage(item(self.itemType + ".png")), self.pos)

class CollideableSprite():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    #If the image is not loaded, load it and save to itemIcons, then draw
    def draw(self, screen):
        screen.blit(safeGetImage(object(self.itemType + ".png")), self.pos)
    
    def getRect(self):
        imageDimensions = safeGetImage(object(self.itemType + ".png")).get_size()
        return pygame.Rect(self.pos[0], self.pos[1], imageDimensions[0], imageDimensions[1])
