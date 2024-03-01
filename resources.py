import pygame

# Definitions for util / game objects - used across files

# Path of an image called str
def imageResource(str):
    return "./images/" + str

# Shorthand
def image(str):
    return pygame.image.load(imageResource(str))

# Subtypes
def itemImage(str):
    return image("items/" + str)

def menuImage(str):
    return image("menu/" + str)
