from resources import image, item, object
import pygame
import constants

# Physical object types, such as store items, or the shelves that can be collided with

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
    
    def getRect(self):
        imageDimensions = safeGetImage(item(self.itemType + ".png")).get_size()
        return pygame.Rect(self.pos[0], self.pos[1], imageDimensions[0], imageDimensions[1])
    
    def clone(self):
        return StoreItem(self.itemType, self.pos)


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

class Collider():
    def __init__(self, pos, dimensions):
        self.pos = pos
        self.dimensions = dimensions

    def getRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])
    
class CheckoutArea():
    def __init__(self, min, max):
        self.rect = pygame.Rect(min[0], min[1], max[0], max[1])

    def draw(self, screen):
        if (constants.RENDER_DEBUG_CHECKOUT_AREA):
            pygame.draw.rect(screen, (0, 255, 0), self.rect, width=5)

    def tick(self, game):
        playerPos = (game.playerX, game.playerY)
        if (self.rect.collidepoint(playerPos)):
            game.sellCartContents()
