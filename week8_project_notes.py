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
