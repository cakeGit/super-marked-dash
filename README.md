theres some random changes so dont just copy paste if you dont have any changes just download my way cooler file

# 1) why movement wasnt workign
python is weird, so functions cant access variables outside unless you use<br/>
`global userX, userY`
# 2) making movement better and work
1st thing is that it isnt normalised (🤓)<br/>
which is fancy math word for that you can move 20% faster on diagonals cause of trig idk<br/>
so, to fix this, you make a movement a vector, then do math shit<br/>
(i also changed movement to be per tick and decoupled from events so that you dont have to spam w)<br/>
```
    pressedKeys = pygame.key.get_pressed()

    #Python lets you use true or false as equal to 1 or 0
    movementVector = (
        pressedKeys[pygame.K_d] - pressedKeys[pygame.K_a],
        pressedKeys[pygame.K_s] - pressedKeys[pygame.K_w]
    )

    #normalise 🤓

    #Pythagorous
    magnitude = math.sqrt(pow(movementVector[0], 2) + pow(movementVector[1], 2))
    #Scale the vector

    if (magnitude != 0):
        movementVector = (movementVector[0]/magnitude, movementVector[1]/magnitude)

        #Apply
        userX += movementVector[0]
        userY += movementVector[1]
```

also you need to call draw every frame in case something changed, the main loop (the while True thing) kept getting changed so probably copy it in
# 3) fixing movement speed
since the main loop runs whenever it feels like it, its important to add a sleep timer, so that it will run at maximum 30fps (ill do 35 cause its a nicer number)<br/>
1/35 = 0.025s per frame<br/>
<br/>
tag on this beautiful hunk of code
```
    startTime = current_milli_time()

    ...game processing here...

    #calculate how long to sleep
    currentTime = current_milli_time()
    deltaTime = currentTime - startTime
    remainingFrameTime = 25 - deltaTime
    if (remainingFrameTime < 0):
        if laggingNotifCooldown == 0:
            laggingNotifCooldown = 50 #Dont scream every tick, it only makes it worse
            print("Game is lagging! (remaining frame time = " + str(remainingFrameTime) + ", total time = " + str(deltaTime) + ")")
        else:
            laggingNotifCooldown -= 1
    else:
        time.sleep(remainingFrameTime / 1000) #Convert to seconds
```

now, the player will move at a set rate
# 4) please god why the images this made me sob dw im a sweat at coding its not really that bad i just wanted to change a few other things related too cause the code is 90% drawing atp and iits not very good
1stly all the item rendering is moved to a list
```
def draw():
    screen.blit(Floor, (0, 0))
    screen.blit(Shelf, (803,27))
    screen.blit(Shelf, (708,27))
    screen.blit(Shelf, (613,27))
    screen.blit(Shelf, (518,27))
    screen.blit(Shelf, (423,27))
    screen.blit(Shelf, (328,27))
    screen.blit(Cashier, (0,200))
    screen.blit(Cashier, (0,300))
    screen.blit(Island, (260,308))
    screen.blit(Island, (260,210))
    screen.blit(Island, (450,210))
    screen.blit(Island, (450,308))
    screen.blit(RShelf, (824,210))
    screen.blit(RShelf, (824,307))
    screen.blit(RShelf, (824,404))

    for item in items:
        item.draw(screen)

    screen.blit(Player, (userX, userY))
```
this list is defined before as 
```
items = [
    StoreItem("grapes", (810,27)),
    StoreItem("grapes", (830,27)),
    StoreItem("grapes", (850,27)),
    StoreItem("grapes", (870,27)),

    StoreItem("watermelon", (810,68)),
    StoreItem("watermelon", (830,68)),
    StoreItem("watermelon", (850,68)),
    StoreItem("watermelon", (870,68)),

    StoreItem("Pepper", (710,27)),
    StoreItem("Pepper", (730,27)),
    StoreItem("Pepper", (750,27)),
    StoreItem("Pepper", (770,27)),

    StoreItem("carrots", (710,68)),
    StoreItem("carrots", (730,68)),
    StoreItem("carrots", (750,68)),
    StoreItem("carrots", (770,68)),

    StoreItem("Corn", (615,27)),
    StoreItem("Corn", (635,27)),
    StoreItem("Corn", (655,27)),
    StoreItem("Corn", (675,27)),

    StoreItem("sweet-potato", (615,68)),
    StoreItem("sweet-potato", (635,68)),
    StoreItem("sweet-potato", (655,68)),
    StoreItem("sweet-potato", (675,68)),

    StoreItem("bread", (520,27)),
    StoreItem("bread", (540,27)),
    StoreItem("bread", (560,27)),
    StoreItem("bread", (580,27)),

    StoreItem("butter", (520,68)),
    StoreItem("butter", (540,68)),
    StoreItem("butter", (560,68)),
    StoreItem("butter", (580,68)),

    StoreItem("milk", (427,27)),
    StoreItem("milk", (447,27)),
    StoreItem("milk", (467,27)),
    StoreItem("milk", (487,27)),

    StoreItem("egg", (440,68)),
    StoreItem("egg", (480,68)),

    StoreItem("maple-syrup", (330,27)),
    StoreItem("maple-syrup", (350,27)),
    StoreItem("maple-syrup", (370,27)),
    StoreItem("maple-syrup", (390,27)),

    StoreItem("soda", (335,68)),
    StoreItem("soda", (355,68)),
    StoreItem("soda", (375,68)),
    StoreItem("soda", (395,68))
]
```
and the StoreItem object is:
```
#Store the images
itemIcons = {}

class StoreItem():
    def __init__(self, itemType, pos):
        self.itemType = itemType
        self.pos = pos

    #If the image is not loaded, load it and save to itemIcons, then draw
    def draw(self, screen):
        if not (self.itemType in itemIcons):
            #Load the image
            itemIcons[self.itemType] = pygame.image.load("items/" + self.itemType + ".png")
        screen.blit(itemIcons[self.itemType], self.pos)
```
And now, when the character is in range of an item, you can code it simply check for all items in range<br/>
then, remove it from `items` and add it to an inventory (make this a dictionary of the item type to the count in the inventory)<br/>
<br/>
# also please split your project into multiple modules so the files dont get too big
[https://www.w3schools.com/python/python_modules.asp](https://www.w3schools.com/python/python_modules.asp)

### thats it your safe from my clutches now
