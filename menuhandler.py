# Menus work around the history list,
# This is by getting whichever menu is most recent in the history
# Then processing clicks and drawing it to the screen
# Which allows you to have a back button that knows where its going
history = []

# Also all of these functions take the game object,
# which means that they can do stuff to it, such as toggling the music

# Clears the history, and navigates to the set menu
def setMenu(menu, game):
    global history
    print("Setting menu to to: "+ menu)
    history = [ menus[menu] ]
    initialiseCurrent(game)

# Navigates to the set menu, keeping the previous one in the history
def navigate(menu, game):
    global history
    print("Navigating to: "+ menu)
    history.append(menus[menu])
    initialiseCurrent(game)

# Remove the last menu from the history, meaning the one before that is displayed
def back():
    global history
    history.pop()
    print("Navigating back")

# Safe (wont cause any error) to call even if you arent looking at a menu
# Draws it to the screen
def drawCurrent(screen, game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.draw(screen, game)

# Safe (wont cause any error) to call even if you arent looking at a menu
# Sends the event to the menu, such as clicks
def processCurrent(event, game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.process(event, game)

# Safe (wont cause any error) to call even if you arent looking at a menu
# Called every update, used for animations
def tickCurrent(game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.tick(game)

# Safe (wont cause any error) to call even if you arent looking at a menu
# Called only by setMeny and navigate,
# Used to clear variables such as for setting up animations
def initialiseCurrent(game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.initialise(game)

import menus.gameFinishedMenu
import menus.levelSelectMenu
import menus.nameInputMenu
import menus.scoreboardMenu
import menus.settingsMenu
import menus.titleMenu

#Store a list of all the menus in ./menus/
menus = {
    "gameFinishedMenu": menus.gameFinishedMenu.getMenu(),
    "levelSelectMenu": menus.levelSelectMenu.getMenu(),
    "nameInputMenu": menus.nameInputMenu.getMenu(),
    "scoreboardMenu": menus.scoreboardMenu.getMenu(),
    "settingsMenu": menus.settingsMenu.getMenu(),
    "titleMenu": menus.titleMenu.getMenu(),
}