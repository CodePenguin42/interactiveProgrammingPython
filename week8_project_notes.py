# Cheat sheet that cuts out the scrolling
    # also a good way of diguring out the template code
    # sorry to anyone reading my code in my notes I use => to mean implies
    # a function can return a number, and can be used as a number
    # it's math.pi, not math.pi() - bad habbit!

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Image information storage class
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

# Sets
rock_group = set([])
missile_group = set ([])
explosion_group = set([])

# General Advice and helpful code:

# Comparison of generating random rocks:
    # Their method:
    rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    rock_avel = random.random() * .2 - .1
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)

# they generate a random number between 0-1 and then do some maths on that?

# Splash (starting screen) code:
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
# the use inequalities to create booleans which then simplify the logic for the if statement

# Thoughts and Questions
    # when do you use object.get_pos and object.pos?
    # two spaces between unrelated code chunks, one space to add spacing within a related code chunk.
    # Do an analysis of how the instruction sheets were created.
    # should add missile ship collisions!
    # don't like thier random, the rocks just head up towards the top left hand corner
    # do a random.choice of a concat of a positive and negative ranges; should avoid getting low speeds and generate random sign
    # reset the ships position and velocity on restart
    # when out of lives should set vel to 0, could also reset angle
    # cant still thrust and twitch so would have to disable the keyhandlers and reenable at the right time
    # moved UI draw_text later in draw handler so it is always on top.
    # hearts for lives
    # hall of fame - scores in order with name
    # make ship class inherit from sprite class
    # make ship a sprite so it can explode!
    # I want to make harts instead of a life counter, make the ship look wrecked as it takes hits, make it explode when you have no lives, and spawn random power ups, and make smaller asteroids appear when you hit a bigger one!!


# Comparison of mine and other dudes code:
# see rice_rocks_example.py
    # They put the process sprite group, group collide, and group group collide alongside the mathematical helper functions
    # in the group collide:
        # they use a boolean flag collided set it to false at the start and then if there is a collsion modify the flag. Then return the flag at the end of the function
        # they create and add a sprite to the explosion group at the same time on one line
        # they use the set method set.remove(thing) which is similar to set.discard(thing) while iterating over the set - which I thought you couldn't do
        # remove will throw and error if you try and remove something that isn't there, discard won't throw an error
        # if you want to remove a random item from a set you can just pop one, as it is an unordered set so removing the last one is random.
    # in group group collide:
        # they use set(group), to create a copy of the group in the same line as the for statement
        # they split out the running og the group collide function into a variable where I leave it on one line.
        # they use remove where I have used discard
    # process sprite group:
        # they draw all the sprites then if the update returns false they remove it in the for loop
    # Ship - draw method:
        # Consolidate the similar draw statements
    # ship.shoot()
        # put the two vector component calculations on different lines for presentation reasons
        # create and add sprite on the same line
    # sprite.update()
        # return the value of the inequality self.age > self.lifespan, rather than using an if else; neat
    # sprite.collide()
        # same as sprite.update()
    # draw(canvas)
        # split out the draw image arguments onto their own lines - I think this looks ugly on a wide screen
        # they increased the rocks velocity based on score in the draw handler not in the rock spawner
        # UI draw statements are below everything but the splash screen
        # they process ship - rock, and missile - rock collisions in the same statment. As you can't have fired at a rock that you hit e.g. if hit a rocck lose a life, else gain a point for every collision of missile and rock
        # Then they put the game over logic, they overwrite the rock set with a blank set rather than deleting each object
    # Rock spawner:
        # while the distance between a rock and the ship is less than 100 move it to the ede of the screen then add it to the group

# General conclusions:
    # they consolidate more stuff onto one line - fewer lines but might be harder to read
    # they create a set to iterate over then modify the origional
    # they use flags and/or intermediate variables to better consolidate changing one thing in a draw function - this I will use to refactor my code
    # vector components on different lines, arguments or components on different lines should be for when you have similarities in the code structures or else to me it looks ugly
    # returning true or false flags based on inequalities rather than if else statements
    # the collisions and sprite processing functions can go above the sprites next to the mathematical helper functions
    # more than one way of processing the same logic that both work
    # instead of emptying each element from a set, replace it with an empty one - faster
    # much neater way of avoiding ship rock collisions - add this concept to refactor
    # they have done less tweaks on what happens between games e.g. stopping the music and the ship from moving, but very nice neat code.

# Magic number dump:
ACC_MULT = 0.1
DEC_MULT = 0.99
TURN_ANGLE_VEL_INC = 0.05
MISSILE_BOOST = 6
ROCK_SPAWN = 1000.0
ROCK_SCORE_RATE = (1 + score / 5.0)
MAX_ROCKS = 12
SPAWN_DISTANCE = 100
ROCK_OFFSET = 150
BG_RATE = 4

# As they are so similar I would like to make the ship clas sinherit from the sprite class as they have many of the same fields, the methods on the other hand are so different that it isn't worth it, you would have to make a whole new set of methods for the ship anyways.

# Post Course Notes:
    # good resource - python.org
    # python 2 vs 3, minor differences
        # 2 more packages, "tried and true" -> what I have learn't with
        # 3 new version, activley developed
    # python 2 or 3 ok on windows, linux comes with it installed, apple is complicated
    # I have learnt event driven programming
    # shell -> console that outputs from the module (where code is), but can take code itself.
    # http://wiki.python.org/moin/UsefulModules#GUI
        # pick a gui like simplegui, or fits your tastes and needs
        # tkinter comes with python already installed and is easy to access, or WxPython
    # http://wiki.python.org/moin/PythonGameLibraries
        # these are better for building games not guis
        # pygame is popular, robust and well supported <- start here
        # pyglet or pyopenGL- if you want OpenGL
    #don't often use global variables as there is limited namespace
        # put stuff in game state Class (lives, in play, use methods only to modify fields, )
        # have one global variable that is an instance of the game state class
        # also good for security - stops stuff being modified by outside force or by accident:
            # e.g. lives is a field of game, create a lose life method, create an instance of game, when the player needs to lose a life use game.lose_life() -> you are not directly modifying the global lives.
    # Good site for reviewing MOOCs
        # https://www.coursetalk.com/providers/coursera/courses/an-introduction-to-interactive-programming-in-python/write-review
        # https://www.class-central.com/review/new/408
# everything is awesome
