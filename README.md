# 1) why movement wasnt workign
python is weird, so functions cant access variables outside unless
`global userX, userY`
# 2) making movement better and work
1st thing is that it isnt normalised (🤓)
which is fancy math word for that you can move 20% faster on diagonals cause of trig idk
so, to fix this, you make a movement a vector, then do math shit
(i also changed movement to be per tick and decoupled from events so that you dont have to spam w)
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
since the main loop runs whenever it feels like it, its important to add a sleep timer, so that it will run at maximum 30fps (ill do 35 cause its a nicer number)
1/35 = 0.025s per frame

tag on this beautiful hunk of code
```
    startTime = current_milli_time()

    ...game processing here...

    #calculate how long to sleep
    currentTime = current_milli_time()
    deltaTime = currentTime - lastTime

    lastTime = currentTime
    remainingFrameTime = 25 - deltaTime
    if (remainingFrameTime < 0):
        if laggingNotifCooldown == 0:
            laggingNotifCooldown = 50 #Dont scream every tick, it only makes it worse
            #Ive uncommented, python is slow it always lags
            #print("Game is lagging! (remaining frame time = " + str(remainingFrameTime) + ", total time = " + str(deltaTime) + ")")
        else:
            laggingNotifCooldown -= 1
    else:
        time.sleep(remainingFrameTime / 1000) #Convert to seconds
```

now, the player will move at a set rate
# 4) please god why the images this made me sob dw im a sweat at coding its not really that bad i just wanted to change a few other things related too cause the code is 90% drawing atp and iits not very good
