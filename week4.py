#python learning 1
#week 4
#optional exercises 4a Practice for lists

# 1) Creating and printing from a list
primes = [2, 3, 5, 7, 11, 13]
print primes[1]
print primes[3]
print primes[-1]

# 2) list manipulation
a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0
print a
print b

#both a and b are altered by the reassisngment of b[0] as there is a link created between a and b by the statement b = a
#so how would you create a second list then reassign the first value

# 3) more list manipulation
a = [5, 3, 1, -1, -3, 5]
b = list(a)
b[0] = 0
print a
print b
#The list function creates a separate non related list b that is identical to a

# 4) vectors and lists
def add_vector(v, w):
    a = v[0] + w[0]
    b = v[1] + w[1]
    new_vector = [a , b]
    return new_vector

#test examples
first_vector = [1, 2]
second_vector = [2, 3]
print add_vector(first_vector, second_vector)

# 5) Challenge: two indepedent timers
# Mystery bug

# This program should implement two independent timers
# each having their own start and stop buttons.
# Find and correct the error in the code below.

import simplegui

# Initialize two counters.
counter1 = [0, 0]
counter2 = list(counter1)

#this is the problem, didn't us a list function to create a separate copy of counter 1 for counter two.

# Define event handlers.
def start1():
    timer1.start()

def stop1():
    timer1.stop()

def start2():
    timer2.start()

def stop2():
    timer2.stop()

def tick1():
    global counter
    if counter1[1] == 9:
        counter1[0] += 1
        counter1[1] = 0
    else:
        counter1[1] += 1

def tick2():
    global counter
    if counter2[1] == 9:
        counter2[0] += 1
        counter2[1] = 0
    else:
        counter2[1] += 1


# Define draw handler.
def draw(canvas):
    canvas.draw_text("Timer 1:     " + str(counter1[0] % 10) + "." + str(counter1[1]), [50, 100], 24, "White")
    canvas.draw_text("Timer 2:     " + str(counter2[0] % 10) + "." + str(counter2[1]), [50, 200], 24, "White")

# Register event handlers.
frame = simplegui.create_frame("Mystery bug", 300, 300)
frame.add_button("Start timer1", start1, 200)
frame.add_button("Stop timer1", stop1, 200)
frame.add_button("Start timer2", start2, 200)
frame.add_button("Stop timer2", stop2, 200)
frame.set_draw_handler(draw)

timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)


# Start frame.
frame.start()

# optional exercises 4 Practice for key events

# 1) debugging a program that uses key events

#imports
import simplegui

#globals
message = "Welcome!"

#helpers and handlers - keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"

#helpers and handlers - draw
def draw(canvas):
    canvas.draw_text(message, [50, 112], 48, "Red")

#create and assign
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

#start
frame.start()

#Need the key_map to translate the up down etc to something simplgui understands
#need to register the key event handler

# 2) changing ball size

#imports
import simplegui

#globals
HEIGHT = 400
WIDTH = 400
radius = 10
STEP = 20
ball_position = [WIDTH / 2, HEIGHT / 2]

#helpers and handlers - key
def keydown(key):
    global radius, step
    if key == simplegui.KEY_MAP["up"]:
        radius += STEP
    elif key == simplegui.KEY_MAP["down"]:
        radius -= STEP

#helpers and handlers - draw
def draw(canvas):
    canvas.draw_circle(ball_position, radius, 1, "White", "White")

#create and register
frame = simplegui.create_frame("big balls", 400, 400)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

#start
frame.start()

# 3) spaced out space bar

#imports
import simplegui

#globals
message = "Space bar up"

#helpers and handlers - keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar down"

#helpers and handlers - keyup
def keyup(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar up"

#helpers and handlers - draw
def draw(canvas):
    canvas.draw_text(message, [100, 200], 22, "White")

#create and register
frame = simplegui.create_frame("space", 400, 400)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#start
frame.start()

# 4) inflating ball

#imports
import simplegui

#globals
HEIGHT = 400
WIDTH = 400
STEP = 5
BALL_GROWTH_INC = 0.2
ball_growth = 0
radius = 20
ball_position = [WIDTH / 2, HEIGHT / 2]

#helpers and handlers - keydown
def keydown(key):
    global ball_growth, BALL_GROWTH_INC
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = BALL_GROWTH_INC
    elif key == simplegui.KEY_MAP["down"]:
        ball_growth = -1.0 * BALL_GROWTH_INC

#helpers and handlers - keyup
def keyup(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        ball_growth = 0

#helpers and handlers - draw
def draw(canvas):
    global ball_position, radius, ball_growth
    radius += ball_growth
    canvas.draw_circle(ball_position, radius, 1, "White", "White")

#create and register
frame = simplegui.create_frame("more balls", 400, 400)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


#start
frame.start()

#logic for change that occurs with every screen refresh happens in draw handler
#add in the shrinking stuff - put in the same event handler just extend the if statements. Only one keydown and one keyup per frame?
