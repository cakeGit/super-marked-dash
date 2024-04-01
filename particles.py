from resources import *
import mathutil

#Store a list of the particles, each as an array with fields:
#[imageID (string), position (int, int), velocity (int, int), gravity (num), remainingLifetime (int)]
#Which i belive is faster than making a class, and these need to be as light as possible
particles = []

# Schema indexes
IMAGE_ID = 0
POSITION = 1
VELOCITY = 2
GRAVITY = 3
REMAINING_LIFETIME = 4

# Holds a dictionary of paths to their respective loaded images, to save repeatedly loading the same thing
images = {}

# Checks images for an already loaded image
# If it doesent exist it loads it from resources.py
# This is a marginally more optimised version than the one in objects.py
# -> Since it skips getting by path and stores by id only (except for loading)
def getParticleImageFromCacheOrLoad(path):
    if not (path in images):
        #Load the image
        images[path] = image(path + ".png")
    return images[path]

# Create a particle with the given data
# imageID (string), position (int, int), velocity (int, int), gravity (int), remainingLifetime (int)
def spawn(imageID, position, velocity, gravity, remainingLifetime):
    # Add in to the particles list
    particles.append([imageID, position, velocity, gravity, remainingLifetime])

# Tick all particles
def tick():
    global particles

    if (len(particles) > 50):
        print("HIGH PARTICLE COUNT! Please take a chill pill to reduce lag!")

    # Whenever a particle is removed, it moves the index of the remaining items backwards, so we need to track it eg:
    # [0, 1, 2, 3]
    #        ^ removed
    # now, the array is
    # [0, 1, 3]
    #        ^ previously 4th element
    # and the element that was in the 4th position, is in the 3rd
    removedParticleCount = 0

    for i in range(len(particles)):
        currentParticle = particles[i - removedParticleCount]

        #Take away 1 tick from the remaining life
        currentParticle[REMAINING_LIFETIME] -= 1

        # If the particle is now out of life
        if currentParticle[REMAINING_LIFETIME] <= 0:
            # Delete it
            del particles[i - removedParticleCount]
            # And increment the removed count
            removedParticleCount += 1
        else: #Otherwise, the particle needs to be simulated

            # Change the velocity by gravity
            currentParticle[VELOCITY] = (
                currentParticle[VELOCITY][0],
                currentParticle[VELOCITY][1] + currentParticle[GRAVITY]
            )

            # Apply the velocity to the position
            currentParticle[POSITION] = mathutil.add(currentParticle[POSITION], currentParticle[VELOCITY])

            # Put the data back in to the particle list
            particles[i - removedParticleCount] = currentParticle

# Draw the particles
def draw(screen):
    
    for particle in particles:
        # Use the schema to access the specified fields of the current particle (see above)
        imageId = particle[IMAGE_ID]
        position = particle[POSITION]

        screen.blit(
            getParticleImageFromCacheOrLoad(imageId), # Get the image for the current particle
            position # And render at the position
            )

# Called at the end of the game to clean up and remove all particles
def clear():
    global particles
    particles = []