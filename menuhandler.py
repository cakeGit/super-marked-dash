import menus

# Easy back button
history = []

def setMenu(menu, game):
    global history
    history = [ menus.menus[menu] ]
    initialiseCurrent(game)

def navigate(menu, game):
    global history
    print("Navigating to: "+ menu)
    history.append(menus.menus[menu])
    initialiseCurrent(game)


def back():
    global history
    history.pop()

# These are safe to call even if you arent looking at a menu

def drawCurrent(screen, game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.draw(screen, game)

def processCurrent(event, game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.process(event, game)

def tickCurrent(game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.tick(game)

def initialiseCurrent(game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.initialise(game)
