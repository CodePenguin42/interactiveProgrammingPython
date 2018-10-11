#python learning 1
#week 3
#optional exercises 3a Drawing

# 1) Printing "it works" on cavas

#imports
import simplegui

#globals
#none

#helper functions / handlers
def draw(canvas):
    canvas.draw_text("It works", [120,120], 48, "Red")

#create frame
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)

#start frame
frame.start()

# 2) print "This is easy" on canvas

#imports
import simplegui

#globals
#none

#helpers and handlers
def draw(canvas):
    canvas.draw_text("This is easy",[150, 150], 42, "White")

#create frame, register handlers
frame = simplegui.create_frame("This is easy", 500, 300)
frame.set_draw_handler(draw)

#start frame
frame.start()

#good guess with the size of the frame, text, and position.

# 3) "X" marks the spot in the upper left hand corner

#imports
import simplegui

#globals
#none

#helpers and handlers
def draw(canvas):
    canvas.draw_text("X", [50,50], 48, "White")

#create and register
frame = simplegui.create_frame("X marks the spot", 96, 96)
frame.set_draw_handler(draw)

#start frame
frame.start()

#should be able to build a template for this kind of work with an example of each type of element to aid memory

# 4) convert seconds to minutes and seconds with string splicing, output to console

#string generation
def format_time(number):
"""generating the string, called in validation function"""
    #calcualte minutes
    minutes = number // 60
    #calculate seconds
    seconds = number % 60
    return str(minutes) + " minutes and " + str(seconds) + " seconds."

def check_number(number):
"""error validation"""
    if number < 0 or number >= 3600:
        print "Your number is out of range"
    else:
        return format_time(number)

#test of the function
print check_number(187)
print check_number(-187)
print check_number(0)
print check_number(360)
print check_number(36666)

# 5) circle of various radii
#abandonded - do the simple version without error validation and come back to this later...
#try putting the error validation in the event handlersfor the clicks as that is when the radi changes

#imports
import simplegui

# globals
radi = 670

#helpers and handlers
#error validation
def validate_radi():
    global radi
    if radi < 1:
        error_message_small()
    elif radi > 600:
        error_message_big()
    else:
        draw_circle(radi)

#error message
def error_message_small(canvas):
    canvas.draw_text("Too small", [300, 300], 48, "White")

def error_message_big(canvas):
    canvas.draw_text("Too big!", [300, 300], 48, "White")

#draw circle
def draw_circle(canvas):
    canvas.draw_circle([300,300], radi, 2, "White")

#increase button
def click_bigger():
    global radi
    radi += 1
    return radi

#decrease button
def click_smaller():
    global radi
    radi -= 1
    return radi

#create and register
frame = simplegui.create_frame("variable circle", 600, 600)
frame.set_draw_handler(draw_circle)
frame.set_draw_handler(error_message_big)
frame.set_draw_handler(error_message_small)
frame.add_button("Bigger", click_bigger)
frame.add_button("Smaller", click_smaller)

#start
frame.start()


# 5) The simple verson

#imports
import simplegui

#globals
HEIGHT = 600
WIDTH = 600
RADIUS_INCREMENT = 2
ball_radius = 20

#draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH//2, HEIGHT//2], ball_radius, 2, "White", "White")

#button event handlers
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT
#add error validation here


def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT
#further error validation here

#create and assign
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("increase radius", increase_radius)
frame.add_button("decrease radius", decrease_radius)

#start frame
frame.start()



#optional exercises 3b Drawing
#A timer updates a global on a regular basis, keep minimal

# 1) Simple timer

#import - simplegui module required
import simplegui

#globals - the initial counter etc
counter = 0

#event handlers - what happens at each tick
def tick():
    global counter
    print counter
    counter += 1

#create timer - delay in ms, and event called
timer = simplegui.create_timer(1000, tick)

#start timer - start the timer
timer.start()


# 2) Start, stop, reset timer that prints to console

#3 buttons
#1 output

#imports
import simplegui

#globals
counter = 0

#helper - timer function
def tick():
    global counter
    draw()
    counter += 1

#helper - buttons
def start():
    timer.start()

def reset():
    global counter
    counter = 0
    draw()

def stop():
    timer.stop()


#create frame and timer, register buttons
timer = simplegui.create_timer(1000, tick)
frame = simplegui.create_frame("timer", 200, 400)
frame.add_button("Start", start)
frame.add_button("Reset", reset)
frame.add_button("Stop", stop)

#start the frame and timer
frame.start()

#I want to print this to the frame, what they want is just to print to console, which is boring
# the more interesting version is...

#imports
import simplegui

#globals
counter = 0

#helper - draw to canvas
def draw(canvas):
    canvas.draw_text(str(counter), [100, 200], 48, "White")

#helper - timer function
def tick():
    global counter
    frame.set_draw_handler(draw)
    #need draw handler when "calling" draw
    counter += 1

#helper - buttons
def start():
    timer.start()

def reset():
    global counter
    counter = 0

def stop():
    timer.stop()


#create frame and timer, register buttons
timer = simplegui.create_timer(1000, tick)
frame = simplegui.create_frame("timer", 200, 400)
frame.add_button("Start", start)
frame.add_button("Reset", reset)
frame.add_button("Stop", stop)

#start the frame and timer
frame.start()


# 3) toggle canvas background colour with timer

#imports
import simplegui

#globals
bkg_colour = "Red"

#helpers
def change_bkg():
    global bkg_colour
    if bkg_colour == "Red":
        bkg_colour = "Blue"
    else:
        bkg_colour = "Red"
    frame.set_canvas_background(bkg_colour)

#create and register
timer = simplegui.create_timer(3000, change_bkg)
frame = simplegui.create_frame("strobe", 200, 200,)
frame.set_canvas_background(bkg_colour)
#need the above line or else it starts out as black

#start
frame.start()
timer.start()

# 4) Expand circle 1px every 100ms
# add in some code that stops it when it gets too big and goes off canvas

#imports
import simplegui

#globals
radius = 0
WIDTH = 200
HEIGHT = 200

#helpers and handlers - draw circle
def draw(canvas):
    canvas.draw_circle([WIDTH//2, HEIGHT//2], radius, 2, "White")
#helpers and handlers - timer
def tick():
    global radius
    global WIDTH
    if radius <= WIDTH//2():
        frame.set_draw_handler(draw)
        radius += 1


#create and register
frame = simplegui.create_frame("pop", WIDTH, HEIGHT)
timer = simplegui.create_timer(100, tick)

#start
frame.start()
timer.start()


# 5) Reaction timer, print to console?! Nah I want to pint to canvas
#move the print to a different section as it isn't printing as I want it

#imports
import simplegui

#globals
ticks = 0
first_click = True

#helpers and handlers - timer
def tick():
    global ticks
    ticks += 1

#helpers and handlers - draw message
def draw(canvas):
    canvas.draw_text("Your reaction speed is " + str(ticks / 100.0) + " seconds", [10, 100], 28, "White")

#helpers and handlers - button
def click():
    global ticks, first_click
    if first_click:
        first_click = False
        ticks = 0
        timer.start()
    else:
        first_click = True
        timer.stop()
        frame.set_draw_handler(draw)
        ticks = 0

#create and register
frame = simplegui.create_frame("reaction", 400, 200)
timer = simplegui.create_timer(10, tick)
frame.add_button("Click me", click, 200)

#start
frame.start()
