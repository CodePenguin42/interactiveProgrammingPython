# Python Course 2
# Week 8 Mini project - finishing the Asteroids game

# template given - learning to work from someone else code. - might re tweak it
# Key features:
    # splash screen provided (start screen) - need to manipulate to generate the end game message lives = 0, restart button
    # asteroids spawn 1 per second max 12
    # sound track starts on game start
    # when asteroid hit missile sound and asteroid explosion - add explosion last
    # thrusting produces sound
    # Lives and score counter
    # missiles has a lifespan - not a numerical cap
    # no asteroid asteroid collision
# object group collisions (missile rocks[group-group], ship rocks) - collision in the sprite class as is common to both collisions
# use True to represent when you need to eecute another function e.g. to determine missile lifespan, True is the flag that lets you know the missile should die

# implementation of Spaceship - program template for RiceRocks
import simplegui
import math
import random


# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False


# Magic number dump:
# multiplier for ship acceleration
ACC_MULT = 0.1
# Smaller number faster the deceleration
DEC_MULT = 0.99
# Larger number the faster the ship turns
TURN_ANGLE_VEL_INC = 0.05
# Larger the number the faster the missiles move
MISSILE_BOOST = 6
# Lifespan of missile - if increse missile speed (via boost) should decrease lifespan or else is easy to cheat!
MISSILE_LIFE = 50
# Time between rock spawns
ROCK_SPAWN = 1000.0
# Is multiplied by score to increase rock score with speed
ROCK_SCORE_RATE = (1 + score / 5.0)
# Maximum number of rocks on the screen
MAX_ROCKS = 12
# Minimum distance away from center of ship the rock must be
SPAWN_DISTANCE = 100
# How far rock is moved in x and y direction if it is too close to ship
ROCK_OFFSET = 150
# Background scroll rate
BG_RATE = 4


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

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, MISSILE_LIFE)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
#soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# group collide helper function
def group_collide(group, other_object):
    # if there is a collision remove the object from the group
    is_collision = False
    for object in group.copy():
        if object.collide(other_object):
            explosion_group.add(Sprite(object.pos, [0,0], 0, 0, explosion_image, explosion_info, explosion_sound))
            group.discard(object)
            is_collision = True
    return is_collision


# helper for group group collisions
def group_group_collide(g1, g2):
    collisions = 0
    for i in g1.copy():
        if group_collide(g2, i):
            collisions += 1
            g1.discard(i)
    return collisions


# helper function to manage and draw sprites:
def process_sprite_group(group, canvas):
    for sprite in group.copy():
        if sprite.update():
            group.discard(sprite)
        sprite.draw(canvas)


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

    def draw(self,canvas):
        draw_center = list(self.image_center)
        if self.thrust:
            draw_center[0] = self.image_center[0] + self.image_size[0]
        canvas.draw_image(self.image, draw_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * ACC_MULT
            self.vel[1] += acc[1] * ACC_MULT
        self.vel[0] *= DEC_MULT
        self.vel[1] *= DEC_MULT

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()

    def increment_angle_vel(self):
        self.angle_vel += TURN_ANGLE_VEL_INC

    def decrement_angle_vel(self):
        self.angle_vel -= TURN_ANGLE_VEL_INC

    def shoot(self):

        # Make a missile
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + MISSILE_BOOST * forward[0], self.vel[1] + MISSILE_BOOST * forward[1]]
        # add missile to the missile set
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))


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

    def draw(self, canvas):
        draw_center = list(self.image_center)
        if self.animated:
            draw_center[0] = self.image_center[0]  + (self.age * self.image_size[0])
        canvas.draw_image(self.image, draw_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        # update lifespan, True => remove
        self.age += 1
        return self.age >= self.lifespan

    def collide(self, other_object):
        #return true if collision
        return dist(self.pos, other_object.pos) <= (self.radius + other_object.radius)


# key handlers to control ship
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()

def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)


# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, time
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        timer.start()
        lives = 3
        score = 0
        soundtrack.rewind()
        soundtrack.play()
        my_ship.pos = [WIDTH//2, HEIGHT//2]
        my_ship.vel = [0,0]
        my_ship.angle = - math.pi * 0.5


# Draw handler
def draw(canvas):
    global time, started, lives, score, rock_group

    # animiate background
    time += 1
    wtime = (time / BG_RATE) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # update and draw ship
    my_ship.draw(canvas)
    my_ship.update()

    # update and draw Sprites (missiles and rocks)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")

    # determine if a missile has hit a rock, update score
    score += group_group_collide(rock_group, missile_group)

    # determine if the ship has been hit, if so decrement lives
    if lives > 0:
        if group_collide(rock_group, my_ship):
            lives -= 1
    else:
        started = False
        soundtrack.pause()
        timer.stop()
        my_ship.vel = [0,0]
        my_ship.angle_vel = 0
        rock_group = set([])

    # draw start screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())


# timer handler that spawns a rock
def rock_spawner():
    # generate a new rock if have less than 12 rocks:
    if len(rock_group) < MAX_ROCKS:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        # if rock is too close to the ship, generate new position
        if dist(rock_pos, my_ship.pos) < SPAWN_DISTANCE:
            rock_pos = [my_ship.pos[0] + ROCK_OFFSET,
                        my_ship.pos[1] + ROCK_OFFSET]
        else:
            rock_vel = [(random.choice(range(2, 8) + range(-8, -2)) /10.0) * ROCK_SCORE_RATE, (random.choice(range(2, 8) + range(-8, -2)) /10.0) * ROCK_SCORE_RATE]

            rock_avel = random.random() * .2 - .1

            # add it to the rock group
            rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info))


# initialize
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
# initialize ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], - math.pi * 0.5, ship_image, ship_info)
# Sets
rock_group = set([])
missile_group = set([])
explosion_group = set([])


# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(ROCK_SPAWN, rock_spawner)

# get things rolling
frame.start()
