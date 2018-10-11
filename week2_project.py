#python learning 1
#week 2
#Mini project - guess the number



#import statements
import random
import simplegui

#global variables
guess = 0
secret_number = random.randrange(0,100)
number_of_guesses = 7
is_hund = True

#helpers and handlers  - input
def input_guess(text_input):
    """take input and decrement guess"""
    global guess, number_of_guesses
    guess = int(inp.get_text())
    number_of_guesses -= 1

#helpers and handlers - buttons
def reset_hun():
    """play a range 0-100 game"""
    global guess, number_of_guesses, secret_number, is_hund
    number_of_guesses = 7
    guess = 0
    secret_number = random.randrange(0,100)
    is_hund = True

def reset_thou():
    """Play a range 0-1000 game"""
    global guess, number_of_guesses, secret_number, is_hund
    number_of_guesses = 10
    guess = 0
    secret_number = random.randrange(0,1000)
    is_hund = False

#helpers and handlers - draw
def draw(canvas):
    """logic for deciding what to draw based on input"""
    global guess, secret_number, number_of_guesses
    if number_of_guesses == 0:
        canvas.draw_text("Out of guesses", [135, 100], 22, "White")
    elif guess == secret_number:
        canvas.draw_text("You win!", [160, 100], 22, "White")
    else:
        canvas.draw_text("Previous guess: " + str(guess), [20, 30], 22, "White")
        canvas.draw_text(str(number_of_guesses), [370, 30], 22, "White")
        if (number_of_guesses == 7 and is_hund == True) or (is_hund == False and number_of_guesses == 10):
            canvas.draw_text("Enter your guess", [130, 100], 22, "White")
        elif ((is_hund == False and guess < 0) or (is_hund == False and guess > 1000)):
            canvas.draw_text("Please enter a number between 0 and 1000", [12, 100], 22, "White")
        elif ((guess < 0 and is_hund == True) or (guess >= 100 and is_hund == True)):
            canvas.draw_text("Please enter a number between 0 and 99", [25, 100], 22, "White")
        elif guess < secret_number:
            canvas.draw_text("Higher", [170, 100], 22, "White")
        elif guess > secret_number:
            canvas.draw_text("Lower", [175, 100], 22, "White")
        else:
            canvas.draw_text("I have no idea...", [140, 100], 22, "White")

#create frame and register buttons
frame = simplegui.create_frame("guessgame", 400, 200)
inp = frame.add_input("Your guess here:", input_guess, 100)
frame.add_button("Range 0-100", reset_hun, 150)
frame.add_button("Range 0-1000", reset_thou, 150)
frame.set_draw_handler(draw)

#start the frame
frame.start()

# Formatting template
# import simplegui
#
# def draw(canvas):
#     canvas.draw_text("Out of guesses", [135, 100], 22, "White")
#     canvas.draw_text("You win!", [160, 100], 22, "White")
#     canvas.draw_text("42", [20, 30], 22, "White")
#     canvas.draw_text("7", [370, 30], 22, "White")
#     canvas.draw_text("Enter your guess", [130, 100], 22, "White")
#     canvas.draw_text("Please enter a number between 0 and 99", [25, 100], 22, "White")
#     canvas.draw_text("Higher", [170, 100], 22, "White")
#     canvas.draw_text("Lower", [175, 100], 22, "White")
#     canvas.draw_text("I have no idea...", [140, 100], 22, "White")
#     canvas.draw_text("Please enter a number between 0 and 1000", [12, 100], 22, "White")
#
# frame = simplegui.create_frame("format", 400, 200)
# frame.set_draw_handler(draw)
# frame.start()

#What I have learnt:
#Start with the win and loss conditions
#then break down the in play game logic further - including error validation
#whn tackling draw handler start with the screens you want group them by type and separate with logic
#only decrement guesses if there is a valid input - needs two sets of error validation
#if you enter a negative number it still counts as a guess, but an if statement here stops the game...
#can I clear the input field?
#reset the random number when you press the reset button!
