import pygame

# Used to get the filepaths for images, so that they can be changed without requiring renaming everything, and for cleaner code

# Path of an image called str
def imageResource(str):
    return "./images/" + str

# Shorthand
def image(str):
    return pygame.image.load(imageResource(str))

# Subtypes
def itemImage(str):
    return image("items/" + str)

def objectImage(str):
    return image("object/" + str)

def menuImage(str):
    return image("menu/" + str)

def item(str):
    return ("items/" + str)

def object(str):
    return ("object/" + str)

def menu(str):
    return ("menu/" + str)