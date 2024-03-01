import pygame
import menuhandler

from resources import menuImage

class Menu:
    def __init__(self, renderer, processor):
        self.renderer = renderer
        self.processor = processor

    def draw(self, screen):
        self.renderer(screen)

    def process(self, event, game):
        self.processor(event, game)

#Change this wwhen making buttons so you can see them - disable when you finished
RENDER_DEBUG_BUTTON_COLLIDERS = True

class Button:
    def __init__(self, rect, onclick):
        self.rect = rect
        self.onclick = onclick

def drawDebugColliders(screen, buttonTable):
    for button in buttonTable.values():
        pygame.draw.rect(screen, (255, 0, 0), button.rect, width=1)


def processMenuButtonClicks(event, game, buttons):
    if event.type != pygame.MOUSEBUTTONUP:
        return
    mousePos = pygame.mouse.get_pos()
    
    for button in buttons:
        if button.rect.collidepoint(mousePos):
            button.onclick(game)

# Title menu

titleBackground = menuImage("titleBackground.png")

def startGame(game):
    game.start()
    menuhandler.back()

titleButtons = {
    "start": Button(pygame.Rect(208, 428, 70, 70), startGame) # Using lambda to prevent circular import
}

def drawTitleMenu(screen):
    screen.blit(titleBackground, (0, 0))

    drawDebugColliders(screen, titleButtons)

def processTitleMenu(event, game):
    processMenuButtonClicks(event, game, titleButtons.values())

menus = {
    "titleMenu": Menu(drawTitleMenu, processTitleMenu)
}