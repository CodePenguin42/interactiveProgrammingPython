# python learning - 2
# week 7

# Acceleration and Friction:
    # implement control scheme of asteriods this week
    # not controlling velocity of ship, you contol acceleration
    # there will be friction in this game - easier to control and caps maxs vel
    # ship class has fields
        # self.angle -> giving the orientation
        # self.angle_vel -> angualar velocity
    # self.angle += self.angle_vel - key handler / person controls self.angle vel
    # self.angle is used as the last argument for the space ships draw method
    # update position -> position += velocity
    # update velocity -> velocity += position
    # When doing this in python would have to do it component at time.
    # This means the ship needs more fields:
        # self.pos -> ships poition
        # self.vel -> ships velocity
        # self.angle -> see above
        # self.thrust -> boolean, is the ship accelerating?
    #  So you update the position of the ship image if ther is thrust:
    # if self.thrust:
        # self.vel[0] += forward[0] * const
        # self.vel[1] += forward[1] * const
    # where forward is the forward thrust e.g. directional acceleration
    # because the acceleration is directional need the x and y components
        # forward = [math.cos(self.angle), math.sin(self.angle)]
    # Notice how you can define the vector in a single line
    # now the position can be updates:
        # self.pos[0 or 1] += self.vel[0 or 1]
    # and now for something completley different - friction
    # friction is just a small negative acceleration
    # vel += thrust + friction, where friction = -c * velocity
    # where c is a coefficient that allows you to tweak how much friction there is but (1 - c), should be close to 1
        # self.vel[0] *= (1-c) - this is short hand for both the velocity change from thrust and the impact of friction

# Spaceship Class:
    # will be handling multiple images so create an image information class - not just representing an element but a repeated code concept
        # self.center, self.size, self.radius, self.lifespan, self.animates
        # and get_methods for all the attributes
        # where radius is teh radius of the circle that completly encloses the image (scaling, collisions)
        # lifespan -> missiles, asteriods
        # animates -> explosoins
    # ship class will also need information on image:
        # self.image, self.image_center, self.image_size, self.radius
        # each of these (except image) will be defined by the ship info class e.g. self.image_center = info.get_center()
        # create a tiled image for the ships different ship state e.g. picture of ship without thrusters next to the ship with
        # need an update method, for position, vel, angle -> not relatiung to the keys the person presses
        # need to describe all the ships behaviour in the ship method. e.g. thrusters on / off, launches missle, changes angualr velocity

# Sound
    # malking da cool sounds!
    # play paus and rewind, can change vol, and play multiple sounds
    # times and sunds are associated with codeskulptor not the frame will have to hit codeskulptors reset button (right of left buttons)
    # using .ogg files as work in firefox and chrome, but not safari; sounds slowdown firefox
    # music = "like to music", music.play (starts the music)

# no practice questions this week :'(

# Sprites - 2D image or animation
    # build a sprite class structure
    # they have evolved into logical entities to organise and represent images
    # sprite sheet - collection of sprites on a single sheet
    # different from a tiled image as not necessarily regularly spaced
    # colours in codeskulptor can be represented either as predefined strings or "rgba(255, 0, 0, 0.5)"
    # where 1 is opaque and 0 is transparent - generally make image background transparent
    # can build images in Photoshop, save as PNG most commonly used
    # Example sprite class
        # class Sprite():
            # def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
            #     self.pos = [pos[0], pos[1]]
            #     self.vel = [vel[0], vel[1]]
            #     self.angle = ang
            #     self.angle_vel = angle_vel
            #     self.image = image
            #     self.imgae_center = info.get_center()
            #     self.image_size = info.get_size()
            #     self.radius = info.get_radius()
            #     self.lifespan = info.get_lifespan()
            #     self.animated = info.get_animated()
            #     self.age = 0
            #     if sound:
            #         sound.rewind()
            #         sound.play()
            #
            # def draw(self, canvas):
            #     canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
            #     canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_szie, self.angle)
            #
            # def update(self):
            #     self.angle += self.angle_vel
            #     self.pos[o] += self.vel[0]
            #     self.pos[1] += self.vel[1]
            #
            # def draw(canvas):
            #     a_rock.draw(canvas)
            #     a_rock.update()
            #
            # frame = simplegui.create_frame("sprite demo", 800, 800)
            #
            # a_rock = Sprite([400, 300], [0.3, 0.4], 0, 0.1, asteroid_image, asteroid_info)
            #
            # frame.set_draw_handler(draw)
            #
            # frame.start()
            #
    # basically if you are going to be reusing the same code or code structure turn it into a class

# Programming tips:
        # debuggling when using sounds:
        # no error message if sound does not load e.g. wrong file name or format, or volume set too low
        # Coding style - Mostly dictionaries
            # could totally redo the pong game with classes - get it right once, fix it once
            # this avoids repeated code and loads of globals
            # use dictionaries like a switch statement to map a thing to an action e.g. key to movement
                # one to one mapping of a known list of inputs to a known set of outputs
                # e.g.
                # inputs = {"up": paddle2_slower,
                            # "down" : paddle2_faster,
                            # "w" : paddl1_slower,
                            # "s": paddle1_faster}
                # def keydown(key):
                    # for i in inputs:
                        # if key == simplegui.KEY_MAP[i]:
                            # inputs[i]() - the () are not a typo
        # you can improve the efficiency of moving the paddles in a given direction provided you set up the padle_vel correctly
            # inputs = {"up": [1, -2],
                        # "down" : [1, 2],
                        # "w" : [0, -2],
                        # "s": [0, 2]}
            # def keydown(key):
                # for i in inputs:
                    # if key == simplegui.KEY_MAP[i]:
                        # paddle_vel[inputs[i][0]] += inputs[i][1]
        # if you find yourself writing long conditionals with similar looking statements you can probably make a dictionary out of it
        # try and reduce the number of globals by using the relationships behind them e.g.:
            # card_pos[0] = card_center[0] + i * card_size[0]
            # card_pos[0] = (0.5 + i) * card_size[0]
            # can define card_pos as a [some maths, more maths]
            # equally frame size[height, width], can replace the heigth and width variables
        # limit the number of magic constants - numbers that appear in the code that you have had to calculate based on something else
        # break down big long expressions into smaller named snippets of cade

# Practice Exercises for Sprites and Sounds

# Make bubble launcher:

# imports
import simplegui, math, random

# global constants
FRAME_SIZE = [800, 600]
FIRING_POSITION = [FRAME_SIZE[0] // 2, FRAME_SIZE[1]]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOUR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
# these are angular velocities so arent vectors
bubble_stuck = True

# firing sound
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")

# helpers - transporations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]
    # breaks angle into corresponding x y vectors

def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
    #pythag - distance between two points, probably distance between two bubbles for later.

# Class- Bubbles
class Bubble:

    def __init__(self, sound = None):
        self.pos = list(FIRING_POSITION) #this uses list() as you are making a copy of the global
        self.vel = [0, 0]
        self.colour = random.choice(COLOUR_LIST)
        self.sound = sound

    def __str__(self):
        return "This is a %s colour ball, at position %s, with velocity %s" % (self.colour, self.position, self.colour)

    def update(self):
        if not bubble_stuck:
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]

            #bouncing off the left and right walls
            if self.pos[0] <= BUBBLE_RADIUS or self.pos[0] > (FRAME_SIZE[0] - BUBBLE_RADIUS):
                self.vel[0] *= -1


    def fire_bubble(self, vel):
        self.vel = vel
        if self.sound:
            self.sound.play()
        # this sets the balls velocity to something that isn't zero and is specified later
        # if the sound exists play it - this stops it throwing an error if problem with sound

    def is_stuck(self):
        pass

    def collide(self, bubble):
        pass

    def draw(self, canvas):
        # draw the bubble
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, self.colour, self.colour)

# helpers - keyhandlers for firing angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck
    if simplegui.KEY_MAP["space"] == key:
        bubble_stuck = False
        vel = angle_to_vector(firing_angle)
        a_bubble.fire_bubble([vel[0] * 4, vel[1] * -4]) #-4 as going upwards with a speed mult of 4
    elif simplegui.KEY_MAP["left"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC


def keyup(key):
    global firing_angle_vel, a_bubble, bubble_stuck
    if simplegui.KEY_MAP["left"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC

# need to stop line from going 360 degrees
# setting the key up opposite to the key down stops the line from spinning at constant rate which increases on every keypress
#need to consider key conflicts e.g. mashing both keys at the same time, releasing a key on restart.

# handlers - draw everything
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck

    #update firing angle
    firing_angle += firing_angle_vel

    #recalculate line angle and redraw the line
    line = [FIRING_POSITION[0] + angle_to_vector(firing_angle)[0] * FIRING_LINE_LENGTH,
            FIRING_POSITION[1] - angle_to_vector(firing_angle)[1] * FIRING_LINE_LENGTH]
    canvas.draw_line(FIRING_POSITION, line, 2, "White")

    #update and draw bubble
    a_bubble.update()
    a_bubble.draw(canvas)

# create and register
frame = simplegui.create_frame("Bubble Shooter", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

#create and start
a_bubble = Bubble(firing_sound)
frame.start()
