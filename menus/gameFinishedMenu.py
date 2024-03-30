from resources import *
from menu import *
import random

# Game finished menu

gameFinishedBackground = menuImage("gameover.png")
gameFinishedPrinterMask = menuImage("gameover-printermask.png")

def startGame(game):
    game.start()
    menuhandler.back()

gameFinishedButtons = {
    "scoreboard": Button(pygame.Rect(691, 327, 70, 70), lambda game: menuhandler.navigate("scoreboardMenu", game)),
    "return": Button(pygame.Rect(691, 504, 70, 70), lambda game: menuhandler.setMenu("titleMenu", game)),
}

reciptHeight = 0

def buildReciptText(game):
    itemReciptEntries = []

    total = 0
    for collectedItem in game.collectedItems:
        total += collectedItem.getScore()
        itemReciptEntries.append(
            collectedItem.item.itemType.upper() + " : " + str(collectedItem.getScore() /10) + "0"
        )

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
        "TIME : " + game.getTimeText(True),
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
    global reciptHeight, reciptText, reciptVelocity
    reciptHeight = 0
    reciptText = buildReciptText(game)
    reciptVelocity = 0.1

reciptVelocity = 0.1
reciptVelocityTicks = 0
def tickGameFinishedMenu(game):
    global reciptHeight, reciptVelocity, reciptVelocityTicks

    reciptVelocityTicks += 1
    if(reciptVelocityTicks == 20):
        reciptVelocityTicks = 0
        reciptVelocity = 0.75 + (random.random() / 4)

    reciptHeight += 20 * reciptVelocity
    reciptHeight = min(reciptHeight, (fontheight + 5) * (len(reciptText) + 1))

def getMenu():
    return Menu(drawGameFinishedMenu, processGameFinishedMenu, initialiser=initGameFinishedMenu, ticker=tickGameFinishedMenu)