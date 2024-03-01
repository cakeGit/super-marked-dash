import pygame
from pygame.locals import *

import levelhandler
import menuhandler
import playerhandler
from resources import image

# initiating pygame
pygame.init()

# creating display (x axis, y axis/ width, height)
screen = pygame.display.set_mode((900,613))

# image loading
Player = image("user.png")

background = (255,255,0)
rect = Player.get_rect()

def draw():
    game.currentLevel.drawBackground(screen)

    for item in game.currentLevelItems:
        item.draw(screen)

    playerhandler.drawPlayer(screen, game)

class Game():
    def __init__(self):
        self.inGame = False
        self.currentLevelIndex = 0
        self.currentLevel = {}
        self.currentLevelItems = []

        self.playerX = 535
        self.playerY = 417

        self.audio = True
        self.music = True

    def start(self):
        print("Started game")
        self.inGame = True
        self.currentLevel = levelhandler.allLevels[self.currentLevelIndex]
        self.currentLevelItems = self.currentLevel.createItemSetForGame()

    def toggleAudio(self):
        self.audio = not self.audio
        print("Toggled audio: " + str(self.audio))
    def toggleMusic(self):
        self.music = not self.music
        print("Toggled music: " + str(self.music))

game = Game()

menuhandler.setMenu("titleMenu")

running = True
while running:
    menuhandler.drawCurrent(screen, game)

    #Game render loop
    if (game.inGame):
        draw()
        playerhandler.updatePlayer(game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        menuhandler.processCurrent(event, game)

        # #draw the health bar -  put ths into
        # health_bar.hp = 50 # makes the health bar to 50%
        # ##health_bar.draw(screen)
    pygame.display.update()
pygame.quit()