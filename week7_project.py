# Python Learning 2
# Week 7
# Project - build the base of 'Rice Rocks', AKA asteroids

# Notes:
    # controls - forward -> thrust, left -> anticllockwise, right -> clockwise, space -> fire missile
    # gameplay - destroy asteroids with missiles
    # week goals - moving spaceship, randomly spawing asteroid, single missile fired
    # audio - oog format -> works in chrome (fastest for dev)
    # given template to work from, and audio, and sprites
    # need to be able to accelerate in a different direction to the one you are currently moving in
    # There is friction in this version of space


# Let's get started

#globals
import simplegui, math, random

#UI globals
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
fire = False

#ship globals
TURN_ANGLE_VEL_INC = 0.02

# Class for loading and describing images
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

    def __str__(self):
        return "image center %s, image size %s, circle radius %d, lifespan %s, animated %s" % (self.center, self.size, self.radius, self.lifespan, self.animated)

    #methods for passing descriptors externally
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
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functios - transformations
# resolving angle to cartesian components
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

# distance between two points
def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

# Ship class
# a special instance of the sprite class, can't you use a parent class and make this a daughter class that inherits from it and has other attributes and methods -> check this out for v2.

class Ship:

    def __init__(self, pos, vel, angle, image, info, sound = None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def __str__(self):
        return "Spaceship position %s, velocity %s, thrust is %s at %s. Image location %s; center %s, size %s, radius %s" % (self.pos, self.vel, self.thrust, self.angle, self.angle_vel, self.image, self.image_center, self.image_size, self.radius)

    # Draw method - starting with circle worry about drawing graphis in later
    def draw(self, canvas):

        # update ship angle - this needs to be updated in the draw handler so a press and hold moves the ship, hence the self.angle_vel intermediary
        self.angle += self.angle_vel

        # components of angle
        vector = angle_to_vector(self.angle)

        # change image and position based on thrust
        if self.thrust:
            self.image_center = [135, 45]
            self.vel[0] += vector[0] * 0.5 # tweak this constant
            self.vel[1] += vector[1] * 0.5
        else:
            self.image_center = [45, 45]
            self.vel[0] *= (1 - 0.05) # tweak this deceleration constan
            self.vel[1] *= (1 - 0.05)

        # change the ships position based in it's speed & wrap to screen
        self.pos[0] += self.vel[0]
        self.pos[0] %= WIDTH
        self.pos[1] += self.vel[1]
        self.pos[1] %= HEIGHT

        # draw the ship
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)


    # Keyhandler methods - AKA ship control methods
    def thrusters(self):
        #accelerate ship in the direction it is pointing
        if not self.thrust:
            self.thrust = True
            ship_thrust_sound.play()
            #move the ship
        elif self.thrust:
            self.thrust = False
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            #slow the ship

    # Keydown methods:
    def ship_left(self):
        #spin ship anticlockwise
        self.angle_vel -= TURN_ANGLE_VEL_INC

    def ship_right(self):
        # spin ship clockwise
        self.angle_vel += TURN_ANGLE_VEL_INC

    # this lives in the ship class because the ship has the behaviour of shooting missiles, also makes the code easier as the missile moves relative to the ship
    def shoot(self):
        global fire, a_missile
        # update missile spawn position
        miss_vector = angle_to_vector(self.angle)
        miss_pos = [self.pos[0] + miss_vector[0] * self.radius, self.pos[1] + miss_vector[1] * self.radius]

        # update missile speed
        miss_vel = [miss_vector[0] * 5, miss_vector[1] * 5]

        # play missile sound
        a_missile = Sprite(miss_pos, miss_vel, 0, 0, missile_image, missile_info, missile_sound)

        fire = True


    # Keyup methods:
    def stop_left(self):
        #ship stops turning anticlockwise
        self.angle_vel += TURN_ANGLE_VEL_INC

    def stop_right(self):
        #ship stops turning clockwise
        self.angle_vel -= TURN_ANGLE_VEL_INC


# Sprite class
# generic sprite class for the asteroids and rockets, and any other in game objects you want to add
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.image_radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def __str__(self):
        return "Created at %s, with vel %s, image radius %d, lifespan %d, animated %s" % (self.pos, self.vel, self.image_radius, self.lifespan, self.animated)

    # sprite update and draw handler
    # starting with demo circle
    def draw(self, canvas):

        #update angle
        self.angle += self.angle_vel

        #update position
        self.pos[0] += self.vel[0]
        self.pos[0] %= WIDTH
        self.pos[1] += self.vel[1]
        self.pos[1] %= HEIGHT

            # these update methods are the same be it sprite or ship, could abstract?

        # draws the sprite
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

            # The purpose of this is to capture the draw behaviour of the moving sprites, not to include the random movement of the rocks, that is dealt with when you spawn the rock e.g. in the timer?




# Canvas draw handler
# draw sprites, and background -> this has a cool timer thing to it
def draw(canvas):
    global time

    # animate background
    time += 1 # -> one tick per draw
    wtime = (time / 4) % WIDTH # slows the movement down, then represents time in relation to the width of the scrren -> distance per tick
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw lives and score
    canvas.draw_text("Score: " + str(score), [100, 20], 20, "White")
    canvas.draw_text("Lives: " + str(lives), [100, 60], 20, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if fire:
        a_missile.draw(canvas)
        # the objects are created then when the frame starts the draw handler is called, it just looks like you are drawing objects before you create them

# timer handler that spawns a rock once a second
def rock_spawner():
    global a_rock
    # random rock position
    rock_pos = [random.choice(range(0, WIDTH)), random.choice(range(0, HEIGHT))]

    # random rock velocity
    rand_angle = (random.choice(range(0, 630, 20)) / 100.0)
    rand_vel = angle_to_vector(rand_angle)
    rand_int1 = random.choice(range(0, 5))
    rock_vel = [rand_vel[0] * rand_int1, rand_vel[1] * rand_int1]

    # random spin velocity
    rock_spin = (random.choice(range(-80, 80, 5)) / 1000.0)

    #spawn a random rock
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_spin, asteroid_image, asteroid_info)

# initialise frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# create ship and sprite objects
#def __init__(self, pos, vel, angle, image, info, sound = None)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], (1.5 * math.pi), ship_image, ship_info, ship_thrust_sound)
# def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.02, asteroid_image, asteroid_info)



# Keyhandlers - they might go here they might not
# input dictionary for keydown:
down_inputs = {"up" : my_ship.thrusters,
                "left" : my_ship.ship_left,
                "right" : my_ship.ship_right,
                "space" : my_ship.shoot
                }

# input dictionary for keyup:
up_inputs = {"up" : my_ship.thrusters,
                "left" : my_ship.stop_left,
                "right" : my_ship.stop_right
            }


# Keydown event handler
# note how you are searching a defined list for a match to the given input
def key_down(key):
    for i in down_inputs:
        if key == simplegui.KEY_MAP[i]:
            down_inputs[i]()
# look up the key in the dictionary then perform the function you find there
# codeskulproe doesn't like it when you put the my_ship. in the for loop, e.g. my_ship.up_inputs[i]() - check

# Keyup eventhandler
def key_up(key):
    for j in up_inputs:
        if key == simplegui.KEY_MAP[j]:
            up_inputs[j]()

#There is a much neater way of handling the left and right arrow keys, and could tidy up the dictionary but that is for the next iteration.


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(1000.0, rock_spawner)

# Start
timer.start()
frame.start()

# Nip to shops then create variables for the vrious magic numbers like the ship turning and the missile speed.
