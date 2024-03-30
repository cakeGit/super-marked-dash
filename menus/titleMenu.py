from resources import *
from menu import *

# Title menu

titleBackground = menuImage("titleBackground.png")

titleButtons = {
    "start": Button(pygame.Rect(208, 428, 70, 70), lambda game: menuhandler.navigate("levelSelectMenu", game)),
    "settings": Button(pygame.Rect(415, 428, 70, 70), lambda game: menuhandler.navigate("settingsMenu", game)),
    # "scoreboard": Button(pygame.Rect(622, 428, 70, 70), lambda game: menuhandler.navigate("scoreboard", game)),
}

def drawTitleMenu(screen, game):
    screen.blit(titleBackground, (0, 0))

    drawDebugButtonColliders(screen, titleButtons)

def processTitleMenu(event, game):
    processMenuButtonClicks(event, game, titleButtons)

def getMenu():
    return Menu(drawTitleMenu, processTitleMenu)