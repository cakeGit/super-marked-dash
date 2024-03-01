import menus

# Easy back button
history = []

def setMenu(menu):
    global history
    history = [ menus.menus[menu] ]

def navigate(menu):
    global history
    history.append(menus.menus[menu])

def back():
    global history
    history.pop()
# These are safe to call even if a menu is not present

def drawCurrent(screen):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.draw(screen)

def processCurrent(event, game):
    hasActiveMenu = len(history) != 0

    if (hasActiveMenu):
        currentMenu = history[len(history)-1]
        currentMenu.process(event, game)
