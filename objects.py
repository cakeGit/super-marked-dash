from resources import itemImage

# Physical object types, such as store items

# STORE ITEMS

#Cache the images save loading them repeatedly
itemIcons = {}

class StoreItem():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    #If the image is not loaded, load it and save to itemIcons, then draw
    def draw(self, screen):
        if not (self.itemType in itemIcons):
            #Load the image
            itemIcons[self.itemType] = itemImage(self.itemType + ".png")
        screen.blit(itemIcons[self.itemType], self.pos)