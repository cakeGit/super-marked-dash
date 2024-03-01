# Holds the data for each level - im guessing you wanted this since one level might get a bit dry and you mentioned it

class Level:
    def __init__(self, initialItems, spawnpoint, renderer):
        self.initialItems = initialItems
        self.spawnpoint = spawnpoint
        self.renderer = renderer

import levels.level1

allLevels = [
    levels.level1
]