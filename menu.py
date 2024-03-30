import pygame
from resources import *
import constants
import menuhandler

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

class Menu:
    def __init__(self, renderer, processor, **kwargs):
        self.renderer = renderer
        self.processor = processor
        self.initialiser = kwargs.get("initialiser", None)
        self.ticker = kwargs.get("ticker", None)

    def draw(self, screen, game):
        self.renderer(screen, game)

    def process(self, event, game):
        self.processor(event, game)

    def initialise(self, game):
        if (self.initialiser != None):
            self.initialiser(game)

    def tick(self, game):
        if (self.ticker != None):
            self.ticker(game)

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