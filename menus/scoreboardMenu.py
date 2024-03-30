from resources import *
from menu import *

# Scoreboard menu

scoreboardBackground = menuImage("scoreboard.png")
scrollMaskRect = pygame.Rect((59, 99), (782, 483))
scoreboardLineHeight = 40
scoreboardEntriesHeight = 0
scoreboardFont = pygame.font.Font('./font/CamingoCode-Regular.ttf', scoreboardLineHeight - 10)
scoreboardTitleFont = pygame.font.Font('./font/CamingoCode-Regular.ttf', 50)
scoreboardEntries = []
scroll = 0
scrollSpeed = 50

def drawScoreboardMenu(screen, game):
    screen.blit(scoreboardBackground, (0, 0))
    screen.blit(scoreboardTitleFont.render("Scoreboard: " + game.lastLevelName, True, (0, 0, 0)), (25, 25))

    # Draw the scores (within the scroll mask)
    screen.set_clip(scrollMaskRect)

    yPos = 0
    for scoreboardEntry in scoreboardEntries:
        screen.blit(scoreboardFont.render(scoreboardEntry, True, (0, 0, 0)), (64, 99 + yPos - scroll))
        yPos += scoreboardLineHeight

    # Reset clipping area
    screen.set_clip(None)

    #Draw the scroll bar "dot"
    if (not scoreboardEntriesHeight == 0):
        scrollScale = scroll / scoreboardEntriesHeight #0 to 1 of how far down you are
        pygame.draw.circle(screen, (0, 0, 0), (740, 113 + (456 * scrollScale)), 10)
    
    drawSimpleReturnButton(screen)

def clamp(minValue, x, maxValue):
    return max(minValue, min(x, maxValue))

def processScoreboardMenu(event, game):
    global scroll
    if (event.type == pygame.MOUSEWHEEL):
        scroll = clamp(0, scroll - (event.y * scrollSpeed), scoreboardEntriesHeight)

    processSimpleReturnButton(event, game)

def initScorebeardMenu(game):
    global scoreboardEntries, scoreboardEntriesHeight, scroll
    scroll = 0
    scoreboardEntries = game.lastLevelScoreboard.getStringEntries()
    scoreboardEntriesHeight = max(len(scoreboardEntries) * scoreboardLineHeight - 483,0)
    print("Fetched scoreboard entries")

def getMenu():
    return Menu(drawScoreboardMenu, processScoreboardMenu, initialiser=initScorebeardMenu)