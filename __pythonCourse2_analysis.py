# I want to have a look over the way they have strctured the guyidance notes when builing stuff so I can break down future projects into reasonanble steps.

# Now the analysis:
    # build the skeleton - imports, globals, data structure classes (image info), load in prerequisite data (sound, images), identify the core classes (ship, sprite) and add in the innit and draw method, make a frame, flesh out a draw handler with the background
    # add in the core code for the event driving class (spaceship - as stuff happens when the spaceship fires or gets hit)
    # get ship image displayed and make ship move, make an update method, call it and draw method in draw handler
    # draw the ship thrusting, and play the sound
    # add wrapping, and deceleration
    # add in the next core object (the missiles mediate the ship rock interaction so they go in last)
    # make sure you have the draw handler then add in the relevant creation events via making registering starting the timer and writing the timer function - don't forget the update and draw!
    # implement the missile sprite, make it appear in the right place, add in the movement, update and draw methods and call in the right places - in this case add in the key handler
    # flesh out the basic gui
    # make the rock group and a process_sprite_group helper - updates and draws a whole set
    # implement group object collision - then add the behaviour to the game e.g. a rock (group) hitting the ship
    # implement other groups (missiles)  and group-group interactions update and draw (if there is a collisions, updating and draw), then add in the ingame logic (when destroy a rock with a missile gain a point)
    # add in start win loss and restart functionality and gui, resetting 'globals' as needed
    # refactor code
    # think up new features and add them
    # take each change slowly and test as often as possible

    # define single core object (fields and methods), then the events that spawn them, and basic in game behaviours
    # generate, update and draw groups of objects
    # add in the object - group in game behaviours
    # inplement further groups and in game behaviours
    # add in group - group interactions (collision) and in game behaviours / consequences
    # get the start and restart smooth
    # refactor code so it's DRY
    # more testing and tweaking
    # implement cool new ideas
