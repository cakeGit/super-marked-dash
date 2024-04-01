#Handles the player drawing and moving

import pygame
from mathutil import *
from resources import image
import constants
import random

#Drawing

playerImage = image("user.png")
cartImage = image("cart.png")

CART_MAX_SLOWDOWN = 0.5

def getPlayerCollisionRect(game):
    return pygame.Rect(game.playerX, game.playerY, 28, 22)

def drawPlayer(screen, game):
    screen.blit(playerImage, (game.playerX - 18, game.playerY - 42))

    playerPos = (game.playerX, game.playerY)
    cartDistance = calcMagnitude(sub(game.cartPos, playerPos))
    if (cartDistance > 50):
        game.cartPos = linearInterpolateVector(game.cartPos, (game.playerX, game.playerY), 0.1)

        cartDifference = sub(game.cartPos, playerPos)
        cartDistance = calcMagnitude(cartDifference)
        if (cartDistance < 50):
            game.cartPos = add(playerPos, multiply(cartDifference, 50 / cartDistance))

    screen.blit(cartImage, (game.cartPos[0] -18, game.cartPos[1] -42))

    if (constants.RENDER_DEBUG_PLAYER_COLLIDERS):
        pygame.draw.rect(screen, (255, 0, 0), getPlayerCollisionRect(game), width=1)
        for collideable in game.getCurrentLevelColliders():
            pygame.draw.rect(screen, (0, 0, 255), collideable.getRect(), width=1)


#Logic

movementVelocity = (0, 0)
sweatParticleSpawn = 0

#Calculate how much the player should move by & make sweat particles depending on how full the cart is
def updatePlayer(game, particles):
    # Particle handling
    global sweatParticleSpawn
    sweatParticleSpawn += 1 * (game.cartRemainingPercent < 0.5) * (1-game.cartRemainingPercent)

    #Check if we have met the threshold to spawn in a new particle
    if (sweatParticleSpawn >= 20):
        # give it a random ish velocity such that it moves up and in either direction
        velocity = (
            (random.random() - 0.5) * 3,
            -(1 + random.random()),
            )

        # Spawn in the particle
        particles.spawn(
            "sweat",
            (
                game.playerX + (random.random() * 28),
                game.playerY + (random.random() * 5) - 42
            ),  
            velocity, .2, 40)
        sweatParticleSpawn = 0

    # Movement handling
    global movementVelocity, lastMovementDirection
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
    magnitude = calcMagnitude(movementVector)

    #Check we are moving
    if (magnitude != 0):
        
        #Normalise
        movementVector = multiply(movementVector, 1/magnitude)

        baseMovementSpeed = 5
        movementSpeed = linearInterpolateScalar(baseMovementSpeed, baseMovementSpeed * game.cartRemainingPercent, CART_MAX_SLOWDOWN)

        movementVector = multiply(movementVector, movementSpeed)

    movementVelocity = linearInterpolateVector(movementVelocity, movementVector, 0.15)

    movePlayer(movementVelocity, game)
    
    # Resolve collisions, and resolve again if there might be more
    while (resolveCollisions(game)):
        pass

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
    game.playerX = min(max(0, game.playerX + velocity[0]), 900 - 28)
    game.playerY = min(max(0, game.playerY + velocity[1]), 613 - 22)


def resolveCollisions(game):
    # Resolve collisions
    playerRect = getPlayerCollisionRect(game)

    collisions = []
    for collision in game.getCurrentLevelColliders():
        rect = collision.getRect()
        if (playerRect.colliderect(rect)):
            clip = playerRect.clip(rect)
            clipArea = clip.width * clip.height
            collisions.append(CollisionContext(collision, rect, clip, clipArea))

    collisions.sort(key=lambda o: -o.clipArea)

    hasResolvedCollision = False
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
        hasResolvedCollision = True
    return hasResolvedCollision
            