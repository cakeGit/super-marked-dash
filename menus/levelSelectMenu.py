from resources import *
from menu import *

# Title menu

background = menuImage("levelselect.png")

# Tell the game what level to load then load it
# Note that index is the array index of the level, meaning level 1 is at index 0
def selectLevel(game, index):
    game.currentLevelIndex = index
    game.load()

selectButtons = {
    "level-1": Button(pygame.Rect(140, 300, 70, 70), lambda game: selectLevel(game, 0)),
    "level-2": Button(pygame.Rect(416, 300, 70, 70), lambda game: selectLevel(game, 1)),
    "level-3": Button(pygame.Rect(692, 300, 70, 70), lambda game: selectLevel(game, 2)),
}

def drawSelectMenu(screen, game):
    screen.blit(background, (0, 0))

    drawDebugButtonColliders(screen, selectButtons)

def processSelectMenu(event, game):
    processMenuButtonClicks(event, game, selectButtons)

def getMenu():
    return Menu(drawSelectMenu, processSelectMenu)