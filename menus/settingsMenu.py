from resources import *
from menu import *

# Settings menu

#this is a temp sprite, so add a proper one sometime
settingsBackground = menuImage("settingsBackground.png")

audioIcon = menuImage("audio.png")
musicIcon = menuImage("music.png")
disabledIcon = menuImage("disabled.png")

def startGame(game):
    game.start()
    menuhandler.back()

settingsButtons = {
    "audioToggle": Button(pygame.Rect(154, 96, 252, 413), lambda game: game.toggleAudio()),
    "musicToggle": Button(pygame.Rect(493, 96, 252, 413), lambda game: game.toggleMusic()),
}

def drawSettingsMenu(screen, game):
    screen.blit(settingsBackground, (0, 0))

    screen.blit(audioIcon, (230, 257))
    screen.blit(musicIcon, (569, 257))

    if (not game.audio):
        screen.blit(disabledIcon, (230, 257))
    if (not game.music):
        screen.blit(disabledIcon, (569, 257))

    drawSimpleReturnButton(screen)
    drawDebugButtonColliders(screen, settingsButtons)

def processSettingsMenu(event, game):
    processMenuButtonClicks(event, game, settingsButtons)
    processSimpleReturnButton(event, game)

def getMenu():
    return Menu(drawSettingsMenu, processSettingsMenu)
