#Change this when making level colliders / debugging player movement
RENDER_PLAYER_COLLIDERS = True

#Handles the player drawing and moving

import pygame
import math
from resources import image

#Drawing

playerImage = image("user.png")

def getPlayerCollisionRect(game):
    return pygame.Rect(game.playerX, game.playerY, 28, 22)


def drawPlayer(screen, game):
    screen.blit(playerImage, (game.playerX-18, game.playerY-42))
    if (RENDER_PLAYER_COLLIDERS):
        pygame.draw.rect(screen, (255, 0, 0), getPlayerCollisionRect(game), width=1)
        for collideable in game.currentLevel.getColliders():
            pygame.draw.rect(screen, (0, 0, 255), collideable.getRect(), width=1)


#Logic

movementVelocity = (0, 0)

def add(vector1, vector2):
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])

def mult(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)

def lerp(vector1, vector2, scalar):
    return add(mult(vector1, 1-scalar), mult(vector2, scalar))

#Calculate how much the player should move by
def updatePlayer(game):
    global movementVelocity
    pressedKeys = pygame.key.get_pressed()

    #Python lets you use true or false as equal to 1 or 0
    movementVector = (
        pressedKeys[pygame.K_d] - pressedKeys[pygame.K_a],
        pressedKeys[pygame.K_s] - pressedKeys[pygame.K_w]
    )
    
    #Up = (0, -1)
    #Down = (0, 1)
    #Left = (-1, 0)
    #Right = (1, 0)

    #Pythagorous 
    magnitude = math.sqrt(pow(movementVector[0], 2) + pow(movementVector[1], 2))

    #Check we are moving
    if (magnitude != 0):
        
        #Normalise
        movementVector = mult(movementVector, 1/magnitude)

        movementSpeed = 2.5
        movementVector = mult(movementVector, movementSpeed)

    movementVelocity = lerp(movementVelocity, movementVector, 0.15)

    movePlayer(movementVelocity, game)
    # if userX > 860 or userX < 0 or userY > 550 or userY < 0:  # if the user bumps into the borders then they re-spawn at position (400,400) this could be seen as another obstacle
    #     userX = 400
    #     userY = 400

class CollisionContext():
    def __init__(self, collideable, rect, clip, clipArea):
        self.collideable = collideable
        self.rect = rect
        self.clipArea = clipArea
        self.clip = clip

def resolveCollision(pos, length, colliderPos, colliderLength):
    center = pos + (length/2)
    colliderCenter = colliderPos + (colliderLength/2)

    if (center > colliderCenter):#Player is + from the collider
        return colliderPos + colliderLength
    else:#Player is - from the collider
        return colliderPos - length

#Moves the player and handles the collsions
def movePlayer(velocity, game):
    game.playerX += velocity[0]
    game.playerY += velocity[1]

    # Resolve collisions
    playerRect = getPlayerCollisionRect(game)

    collisions = []
    for collision in game.currentLevel.getColliders():
        rect = collision.getRect()
        if (playerRect.colliderect(rect)):
            clip = playerRect.clip(rect)
            clipArea = clip.width * clip.height
            collisions.append(CollisionContext(collision, rect, clip, clipArea))

    collisions.sort(key=lambda o: -o.clipArea)

    for collision in collisions:
        playerRect = getPlayerCollisionRect(game)
        rect = collision.rect
        
        #Check this collision hasn't been resolved by something else
        if (not playerRect.colliderect(rect)):
            continue

        if (clip.width < clip.height):
            game.playerX = resolveCollision(playerRect.left, playerRect.width, collision.rect.left, collision.rect.width)
        else:
            game.playerY = resolveCollision(playerRect.top, playerRect.height, collision.rect.top, collision.rect.height)
            