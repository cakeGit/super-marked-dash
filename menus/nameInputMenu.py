from resources import *
from menu import *
import re

# Name badge input menu

backgroundOverlay = menuImage("backgroundoverlay.png")
nameBadgeInput = menuImage("namebadgeinput.png")
nameBadgeInputSubmitButton = menuImage("namebadgeinputsubmit.png")

playerNameInputFont = pygame.font.Font('./font/KaushanScript-Regular.ttf', 60)
playerNameInput = ""

incomeLerpAnimationLength = 20
incomeLerpAnimationTicks = 0

def submitNameBadgeInputMenu(game):
    game.playerName = playerNameInput
    game.start()
    
nameBadgeInputButtons = {
    "submit": Button(pygame.Rect(400, 428, 100, 100), submitNameBadgeInputMenu),
}

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

def getMenu():
    return Menu(drawNameBadgeInputMenu, processNameBadgeInputMenu, initialiser=initNameBadgeInputMenu, ticker=tickNameBadgeInputMenu)

