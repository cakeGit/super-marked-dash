import pygame
import menuhandler
import constants

from resources import menuImage

class Menu:
    def __init__(self, renderer, processor):
        self.renderer = renderer
        self.processor = processor

    def draw(self, screen, game):
        self.renderer(screen, game)

    def process(self, event, game):
        self.processor(event, game)

class Button:
    def __init__(self, rect, onclick):
        self.rect = rect
        self.onclick = onclick

def drawDebugButtonColliders(screen, buttonTable):
    if (not constants.RENDER_DEBUG_BUTTON_COLLIDERS):
        return
    for button in buttonTable.values():
        pygame.draw.rect(screen, (255, 0, 0), button.rect, width=1)


def processMenuButtonClicks(event, game, buttons):
    if event.type != pygame.MOUSEBUTTONUP:
        return
    
    mousePos = pygame.mouse.get_pos()
    
    for button in buttons.values():
        if button.rect.collidepoint(mousePos):
            button.onclick(game)

# Simple return button

simpleReturnButtons = {
    "return": Button(pygame.Rect(798, 262, 90, 90), lambda g: menuhandler.back())
}

returnButton = menuImage("return.png")

def drawSimpleReturnButton(screen):
    screen.blit(returnButton, (811, 275))
    drawDebugButtonColliders(screen, simpleReturnButtons)

def processSimpleReturnButton(event, game):
    processMenuButtonClicks(event, game, simpleReturnButtons)

# Title menu

titleBackground = menuImage("titleBackground.png")

def startGame(game):
    game.start()
    menuhandler.back()

titleButtons = {
    "start": Button(pygame.Rect(208, 428, 70, 70), startGame), # Using lambda to prevent circular import
    "settings": Button(pygame.Rect(415, 428, 70, 70), lambda g: menuhandler.navigate("settings")),
}

def drawTitleMenu(screen, game):
    screen.blit(titleBackground, (0, 0))

    drawDebugButtonColliders(screen, titleButtons)

def processTitleMenu(event, game):
    processMenuButtonClicks(event, game, titleButtons)

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

# Game finished menu

gameFinishedBackground = menuImage("gameover.png")

def startGame(game):
    game.start()
    menuhandler.back()

gameFinishedButtons = {
    "return": Button(pygame.Rect(415, 464, 70, 70), lambda g: menuhandler.setMenu("titleMenu")),
}

def drawGameFinishedMenu(screen, game):
    screen.blit(gameFinishedBackground, (0, 0))

    drawDebugButtonColliders(screen, gameFinishedButtons)

def processGameFinishedMenu(event, game):
    processMenuButtonClicks(event, game, gameFinishedButtons)


menus = {
    "titleMenu": Menu(drawTitleMenu, processTitleMenu),
    "settings": Menu(drawSettingsMenu, processSettingsMenu),
    "gameFinished": Menu(drawGameFinishedMenu, processGameFinishedMenu),
}