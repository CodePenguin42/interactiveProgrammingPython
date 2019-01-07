# # python learning - 2
# week 8

# Groups of Sprites - Sets
    # set - a collection of objects (data) and their properties, unique and ordered so faster to use
    # name1 = set([thing1, thing2, thing3])
    # print thing in set -> boolean
    # name2 = set([thing1, thing1, thing2, thing3]) -> set([thing1, thing2, thing3]) == name1
    # set methods name.add(), name.remove()
    # cannot remove something if it is not in the set
    # if thing1 in name1:
        # name1.remove(thing1)

    # removing stuff from one set and adding it to another:
    # instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
    # print instructors
    #
    # def get_rid_of(inst_set, starting_letter):
    #     remove_set = set([])
    #     for inst in inst_set:
    #         if inst[0] == starting_letter:
    #             remove_set.add(inst)
    #     inst_set.difference_update(remove_set)
    #
    # get_rid_of(instructors, 'W')
    # print instructors
    # do not modify the set that you are iterating over, create a set of things that you want to remove then use difference update to remove them

    # need to be able to iterate through sets to draw objects in the game, and to decide if there has been a collision, then score points
        # Assume there are no asteroid - asteroid collisions....

    # need to iterate through a set of asteroids and see if distance from the centers (missile, asteroid) is <= sum of radi, if it is then add the asteroid to the remove set and difference update.
        # essentially the same logic for the rock and ship collision, just lose a life, if out of lives end the game

# Groups of Sprites - Collisions for Sprites
    # assume a spherical chicken in a vacuume.
    # ability to detect a collision with a Sprite goes inside the sprite class - as that is where the location of the sprite data is
        # this is a rock and anything, and a missile and anything collision.
        # A ship is not a sprite as it is not going to need the functionality of being a set
    # remember make a general sprite collision method then use rock.collide(ship) (iterating over rocks) to detect a collision
    # group_collide(rocks, ship) -> True if there is a collision; is easier
        # the group_collide function is the wrapper for the iteration only works for an object colliding with a set
    # Alternative iteration method for removing:
        # for s in list(myset):
            # myset.remove(s)
        #This works as you are creating a duplicate list of the set and removing stuff from the duplicate
    # Set to set collisions:
        # for s in set1:
            # for e in set2:
                # group_collide(....)
                # return the number of collisions, count the number of True's from group_collide(....)
        # I think that should reduce the set-set collision down into essentially multiple object set collisions
        # many - many mapping -> many(one - many) mappings

# Practice examples using the bubble shooter game
# Basic infrastructure for Bubble Shooter

import simplegui, random, math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True


# firing sound
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# class defintion for Bubbles
class Bubble:

    def __init__(self, sound = None):
        self.pos = list(FIRING_POSITION)
        self.vel = [0, 0]
        self.color = random.choice(COLOR_LIST)
        self.sound = sound

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] <= BUBBLE_RADIUS or self.pos[0] >= WIDTH - BUBBLE_RADIUS:
            self.vel[0] = - self.vel[0]

    def fire_bubble(self, vel):
        self.vel = vel
        if self.sound:
            self.sound.play()


    def is_stuck(self, bubble_group):
        #return true if bubble is touching the top wall
        if self.pos[1] <= BUBBLE_RADIUS:
            return True
        for b in bubble_group:
            if self.collide(b):
                return True
                # couldn't this be written as return self.collide(b) - as collide returns a boolean.
        return False
    # This is acting like a less rigid elif statement, each statement is evaluated in turn until a value is returned.

    def collide(self, bubble):
        if dist(self.pos, bubble.pos) <= 2 * BUBBLE_RADIUS:
            return True
        return False
        # They have used much shorter syntax: return dist(self.pos, bubble.pos) <= 2 * BUBBLE_RADIUS

    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, "White", self.color)


# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck
    if simplegui.KEY_MAP["space"] == key:
        bubble_stuck = False
        vel = angle_to_vector(firing_angle)
        a_bubble.fire_bubble([4 * vel[0], -4 * vel[1]])
    elif simplegui.KEY_MAP["left"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC

def keyup(key):
    global firing_angle_vel
    if simplegui.KEY_MAP["left"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC

# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck

    # update firing angle
    firing_angle += firing_angle_vel

    #draw firing line
    orient = angle_to_vector(firing_angle)
    upper_endpoint = [FIRING_POSITION[0] + FIRING_LINE_LENGTH * orient[0],
                      FIRING_POSITION[1] - FIRING_LINE_LENGTH * orient[1]]
    canvas.draw_line(FIRING_POSITION, upper_endpoint, 4, "White")

    # update a_bubble and check for sticking
    a_bubble.update()

    #
    if a_bubble.is_stuck(stuck_bubbles):
        bubble_stuck = True
        stuck_bubbles.add(a_bubble)
        a_bubble = Bubble(firing_sound)
        firing_angle = math.pi / 2


    # draw a bubble and stuck bubbles
    a_bubble.draw(canvas)
    for b in stuck_bubbles:
        b.draw(canvas)

# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
a_bubble = Bubble(firing_sound)
stuck_bubbles = set([])
frame.start()

# This is cool but:
    # Sometimes the bubbles overlap slightly - this is a rounding issue with the 'where the ball will be' issue
    # also it doesn't do next nearest neighbour distances
    # could make this waay cooler, but that is a pet project for when I need to look over python again

# Part B - Sprite Animation
    # Makes stuff look cooler
    # Digital version of persistence of vision or a analogue film

# demo of animation using asteroid sprite sheet

import simplegui

# load 64 frame sprite sheer for asteroid - image source is opengameart, artist is warspawn
ROCK_CENTER = [64, 64]
ROCK_SIZE = [128, 128]
ROCK_DIM = 64
rock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# global time for animation
time = 0
# time without using a timer
# when doing asteroids game will have to use age and lifespan to control animation of sprite class

# draw handler
def draw(canvas):
    global time
    current_rock_index = (time % ROCK_DIM) // 1 # the //1 converts the fraction to an index
    # using time as a for loop iterator
    current_rock_center = [ROCK_CENTER[0] +  current_rock_index * ROCK_SIZE[0], ROCK_CENTER[1]]
    canvas.draw_image(rock_image, current_rock_center, ROCK_SIZE, ROCK_CENTER, ROCK_SIZE)
    time += 0.2 # the larger this number the faster the rock spins, the draws per frame if >1 skips images, if <1 slows the animation
    # 0.2 is 12 frames a second

# create frame and size frame based on 128x128 pixel sprite
frame = simplegui.create_frame("Asteroid sprite", ROCK_SIZE[0], ROCK_SIZE[1])

# set draw handler and canvas background using custom HTML color
frame.set_draw_handler(draw)
frame.set_canvas_background("Blue")

# start animation
frame.start()

# Another Example 2D tiled image L-R, Top-Bottom
# animation of explosion using 2D sprite sheet

import simplegui

# load 81 frame sprite sheer for explosion - image generated by phaedy explosion generator, source is hasgraphics.com
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]
EXPLOSION_DIM = [9, 9] # dimensions of sprite tile 9 images by 9 images
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# create timer that iterates current_sprite_center through sprite
time = 0

# define draw handler
def draw(canvas):
    global time
    explosion_index = [time % EXPLOSION_DIM[0], (time // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1]] # relates the time to the index of the image you want to display
    canvas.draw_image(explosion_image,
                    [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0],
                     EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]],
                     EXPLOSION_SIZE, EXPLOSION_CENTER, EXPLOSION_SIZE)
    time += 1


# create frame and size frame based on 100x100 pixel sprite
f = simplegui.create_frame("Asteroid sprite", EXPLOSION_SIZE[0], EXPLOSION_SIZE[1])

# set draw handler and canvas background using custom HTML color
f.set_draw_handler(draw)
f.set_canvas_background("Blue")

# start animation
f.start()

# Programming Tips - Sets
# python version 2.6 which is used in codeskulptor does not support {} as a set - clashing with the common mathematical notation
# set intersection / mutation
    # s.intersection(t) - returns the common elements of s and t
    # s.intersection_update(t) - returns nothing, and modifies s to contain only the common elements
        # similar to database manipulations
    # read through the documentation for info on the Union / Intersection / Difference / Symmetris difference methods and their respective methods with mutations
    # the aqrguments can be anything not just a set, but a list or a string etc
