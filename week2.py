#python learning 1
#week 2
#optional exercises 2a Interactive Applications

# 1) global variable = "Hello", global variable = "Goodbye"

message = "Hello"

def print_goodbye():
"""a function to define message the local variable,as goodbye"""
    message = "Goodbye"
    print message

#testing of global and local variables
print message
print_goodbye()
print message

# 2) changing globalvariable with function

def set_goodbye():
"""using key words to change g variable inside function"""
    global message
    message = "Goodbye"
    print message

# Test of the change in variable
print message
set_goodbye()
print message

# 3) Challenge reset, increment, decrement, and print a global variable
#initialise count in global namespace
count = 0

#functions to manipulate the count variable
def reset():
    """a function to reset the value of count to the inital value"""
    global count
    count = 0

def increment():
    """increment the count variable"""
    global count
    count += 1

def decrement():
    """decrement the count variable"""
    global count
    count -= 1

def print_count():
    """print the count variable"""
    global count
    print count

#test of the functions
increment()
print_count()
increment()
print_count()
decrement()
print_count()
reset()
print_count()


# 4) My first frame 100x200, title my first frame

#import statements
import simplegui

#message acting as a title
message = "My first frame!"

#Handler for mouse click that prints title
def click():
    print message

#create the frame and assign callbacks to the event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

#start the frame
frame.start()

# 5) My second frame 200 x 100

#already done the imports
import simplegui

#helper functions and variables
message = "My second frame"

#click handler creation
def click():
    print message

#create the frame and assin callbacks to the event handlers
frame = simplegui.create_frame("My second frame", 200, 100)
frame.add_button("Click me", click)

#start the frame
frame.start()

# optional exercises 2b - Buttons and input fields

# 1) Frame with buttons that print "hello" and "goodbye"
import simplegui

 #Handlers for the buttons
def print_hello():
     print "Hello"

def print_goodbye():
    print "Goodbye"

#create frames and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello, 100)
frame.add_button("Goodbye", print_goodbye, 100)

#start the frame, do not forget this
frame.start()

#test the functions
print_hello()
print_goodbye()

#test the frame by clicking a few buttons

# 2) changing the global variable with buttons

#global variable
colour = "green"

#Handlers for the buttons
def print_colour():
    global colour
    print colour

def set_red():
    global colour
    colour = "red"
    print_colour()

def set_blue():
    global colour
    colour = "blue"
    print_colour()

def set_reset():
    global colour
    colour = "green"
    print_colour()

#create frame and regester buttons
frame = simplegui.create_frame("global colour manipluation", 200, 200)
frame.add_button("Print",print_colour,100)
frame.add_button("Red", set_red, 100)
frame.add_button("Blue", set_blue, 100)
frame.add_button("Reset", set_reset, 100)

#Start the frame
frame.start()

#test the demo functions
print_colour()
set_red()
set_blue()
set_reset()

# 3) make a counter... oooo

#globals
count = 0

#Handlers
def print_count():
    global count
    print count

def reset():
    global count
    count = 0
    print_count()

def increment():
    global count
    count += 1
    print_count()

def decrement():
    global count
    count -= 1
    print_count()

#create frame and register buttons
frame = simplegui.create_frame("global count manipulation", 200, 200)
frame.add_button("Print", print_count, 100)
frame.add_button("Reset", reset, 100)
frame.add_button("Increment", increment, 100)
frame.add_button("Decrement", decrement, 100)

#start the frame
frame.start()

#test the functions
print_count()
increment()
increment()
decrement()
reset()

# 4) Echo input to console

#globals - none

#functions
def get_input(txt):
    print txt

#create frame and register functions
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Echo input (press enter)", get_input, 200)

#start the frame
frame.start()

#test functions
get_input("A spoon full of sugar")

#okay, so functions is what I want to do with the captured text, capturing it is the role of the event handler add_input

# 5) enter a word in frame and get pig latin out
#functions
def pig_latin(word):
    """makes words into pig latin"""
    if (word[0] == "a") or (word[0] == "e") or (word[0] == "i") or (word[0] == "o") or (word[0] == "u"):
        print word + "ay"
    else:
        print word[1 : ] + word[0] + "ay"


#create frame and register stuff
frame = simplegui.create_frame("pig latin frame", 200, 200)
frame.add_input("Type phrase then hit enter", pig_latin, 200)

#start frame
frame.start()

#test funtion
pig_latin("owl")

#so that works, would be better if the input field cleared itself after you hit enter

# 6) add interface to RPSLS

#import
import simplegui
import random

#helper functions:
def name_to_number(name):
    """dictionary lookup to convert name(key) into number(value)"""
    return {
    "rock" : 0,
    "Spock" : 1,
    "paper" : 2,
    "lizard" : 3,
    "scissors" : 4
    }.get(name, "Invalid choice")

def number_to_name(number):
    """dictionary lookup to convert number(key) into name(value)"""
    return {
    0 : "rock",
    1 : "Spock",
    2 : "paper",
    3 : "lizard",
    4 : "scissors"
    }.get(number, "Number out of range")

#Main function
#need some filtering before the frame gets invoved this has to be a separate function
def get_guess(guess):
    if not (guess == "rock" or guess == "paper" or guess == "scissors" or guess == "lizard" or guess == "spock"):
        print "please enter rock, paper, scissors, lizard, spock"
        print
        return
    else:
        rpsls(guess)

def rpsls(player_choice):
    """main function taking player choice, making random choice, and deciding the victor"""
    
    #confirm player choice and generate number
    print "The player has chosen " + player_choice + " no take-backsies!"
    player_number = name_to_number(player_choice)

    #make random computer choice
    computer_number = random.randrange(0,5)
    computer_choice = number_to_name(computer_number)
    print "The computer has chosen " + computer_choice

    #calculating the winner
    value = (player_number - computer_number) % 5

    #declaring the winner
    if value == 1 or value == 2:
        print "The player wins"
    elif value == 3 or value == 4:
        print "The computer wins"
    elif value == 0:
        print "We have a draw"
    else:
        print "time to do some debugging"

    #print blank line to separate games
    print

#create frame and register inputs
frame = simplegui.create_frame("RPSLS interface", 200, 200)
frame.add_input("Your guess", get_guess, 200)

#start frame
frame.start()

#test the function
rpsls("Spock")
rpsls("scissors")
rpsls("paper")
rpsls("rock")
rpsls("lizard")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
