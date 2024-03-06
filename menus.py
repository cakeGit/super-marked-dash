import pygame
import menuhandler
import constants
import random
import re

from resources import menuImage

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

titleButtons = {
    "start": Button(pygame.Rect(208, 428, 70, 70), lambda game: game.load()), # Using lambda to prevent circular import
    "settings": Button(pygame.Rect(415, 428, 70, 70), lambda game: menuhandler.navigate("settings", game)),
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
gameFinishedPrinterMask = menuImage("gameover-printermask.png")

def startGame(game):
    game.start()
    menuhandler.back()

gameFinishedButtons = {
    "scoreboard": Button(pygame.Rect(691, 327, 70, 70), lambda game: menuhandler.setMenu("titleMenu", game)),
    "return": Button(pygame.Rect(691, 504, 70, 70), lambda game: menuhandler.setMenu("titleMenu", game)),
}

reciptHeight = 0

def buildReciptText(game):
    itemReciptEntries = []
    total = 0
    
    for collectedItem in game.collectedItems:
        itemReciptEntries.append(
            collectedItem.item.itemType.upper() + " : " + str(collectedItem.getScore() /10) + "0"
        )
        total += collectedItem.getScore()

    if (itemReciptEntries == []):
        itemReciptEntries = [ "*NONE*" ]

    return [
        "= SUPER-MART™ =",
        "RECIPT OF PURCHASE",
        "",
        "----------------------------",
    ] + itemReciptEntries + [
        "",
        "TOTAL : " + str(total /10) + "0",
        "----------------------------",
        "",
        "Thanks for shoping at",
        "SUPER-MART™"
    ]

fontheight = 25
reciptFont = pygame.font.Font('./font/CamingoCode-Regular.ttf', fontheight)
reciptText = []

def drawGameFinishedMenu(screen, game):
    screen.blit(gameFinishedBackground, (0, 0))

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((72, 590 - reciptHeight), (403, reciptHeight)))

    yPos = 595 - reciptHeight
    for line in reciptText:
        screen.blit(reciptFont.render(line, True, (0, 0, 0)), (79, yPos))
        yPos += fontheight + 5

    screen.blit(gameFinishedPrinterMask, (0, 0))

    drawDebugButtonColliders(screen, gameFinishedButtons)

def processGameFinishedMenu(event, game):
    processMenuButtonClicks(event, game, gameFinishedButtons)

def initGameFinishedMenu(game):
    global reciptHeight, reciptText
    reciptHeight = 0
    reciptText = buildReciptText(game)

reciptVelocity = random.random()
reciptVelocityTicks = 0
def tickGameFinishedMenu(game):
    global reciptHeight, reciptVelocity, reciptVelocityTicks

    reciptVelocityTicks += 1
    if(reciptVelocityTicks == 20):
        reciptVelocityTicks = 0
        reciptVelocity = pow(random.random()*2, 2)

    reciptHeight += 20 * reciptVelocity
    reciptHeight = min(reciptHeight, (fontheight + 5) * (len(reciptText) + 1))

# Name badge input menu

backgroundOverlay = menuImage("backgroundoverlay.png")
nameBadgeInput = menuImage("namebadgeinput.png")
nameBadgeInputSubmitButton = menuImage("namebadgeinputsubmit.png")

playerNameInputFont = pygame.font.Font('./font/KaushanScript-Regular.ttf', 60)
playerNameInput = ""

incomeLerpAnimationLength = 20
incomeLerpAnimationTicks = 0

def animationInterpolate(i, length):
    i = max(min(i / length, 1), 0)
    return pow(i, 2)

def getSlideInY(direction):
    return direction * (1-animationInterpolate(incomeLerpAnimationTicks,  incomeLerpAnimationLength)) * 613

def drawNameBadgeInputMenu(screen, game):
    screen.blit(backgroundOverlay, (0, 0))

    screen.blit(nameBadgeInput, (0, getSlideInY(-1)))
    screen.blit(nameBadgeInputSubmitButton, (0, getSlideInY(1)))

    if (incomeLerpAnimationTicks != incomeLerpAnimationLength):
        return
    
    screen.blit(playerNameInputFont.render(playerNameInput, True, (0, 0, 0)), (239, 300))
    if (playerNameInput == ""):
        screen.blit(playerNameInputFont.render("NAME HERE", True, (100, 100, 100)), (239, 300))

    drawDebugButtonColliders(screen, nameBadgeInputButtons)

def processNameBadgeInputMenu(event, game):
    if (incomeLerpAnimationTicks != incomeLerpAnimationLength):
        return

    global playerNameInput
    processMenuButtonClicks(event, game, nameBadgeInputButtons)

    if event.type != pygame.KEYDOWN:
        return
    
    keyPressed = event.unicode

    if re.search("[a-zA-Z]", keyPressed) != None:
        playerNameInput += keyPressed
    elif keyPressed == '\x08':
        playerNameInput = playerNameInput[0:-1]

def tickNameBadgeInputMenu(game):
    global incomeLerpAnimationTicks
    incomeLerpAnimationTicks += 1
    incomeLerpAnimationTicks = min(incomeLerpAnimationTicks, incomeLerpAnimationLength)

def initNameBadgeInputMenu(game):
    global incomeLerpAnimationTicks
    incomeLerpAnimationTicks = 0

def submitNameBadgeInputMenu(game):
    game.playerName = playerNameInput
    game.start()

nameBadgeInputButtons = {
    "submit": Button(pygame.Rect(400, 428, 100, 100), submitNameBadgeInputMenu),
}

menus = {
    "titleMenu": Menu(drawTitleMenu, processTitleMenu),
    "settings": Menu(drawSettingsMenu, processSettingsMenu),
    "nameInputMenu": Menu(drawNameBadgeInputMenu, processNameBadgeInputMenu, initialiser=initNameBadgeInputMenu, ticker=tickNameBadgeInputMenu),
    "gameFinished": Menu(drawGameFinishedMenu, processGameFinishedMenu, initialiser=initGameFinishedMenu, ticker=tickGameFinishedMenu),
}