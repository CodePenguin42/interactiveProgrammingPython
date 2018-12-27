#python learning 2
#week 5
#mini project - pairs / memory game
#game matching cards 1 -> 8

#Process:
    #define the end states for the game, and the pairs of cards
    #create logic to navigate between those options

#Types of states:
    #logic states - paired, not paired, win, loss
    #design states - face up or down, location
#Game states:
    #in progress - new_game called
    #completed - all cards face up and matched
#Card states:
    #face down, unmatched
    #face up, unmatched
    #face up, matched
#Flags:
    #clicked - if it has been clicked on in the turn (reset click flags, two clicks then increment turn)
#End conditions:
    #when all cards are matched or when you have had enough turns

#Version 2:
    #timer for the game - starts on first click when turn = 0 and click = 1
    #Sadly cannot make it resize in gamE :()

#imports
import simplegui, random

#globals
GRID = 4
CARD_WIDTH = 75
CARD_HEIGHT = 100
BORDER = 10
HEIGHT = (CARD_HEIGHT * GRID) + (BORDER * 5)
WIDTH = (CARD_WIDTH * GRID) + (BORDER * 5)

#Counters and flags
click_counter = 0
card_pos_one = [0,0]
card_pos_two = [0,0]
turn_counter = 0

#Generating random grid
card_list = range(1, (GRID * 2) + 1)
card_list.extend(range(1, (GRID * 2) + 1))
random.shuffle(card_list)
card_grid = [card_list[x:x+GRID] for x in range(0, len(card_list), GRID)]

#Generating card grid
grid_list = []
for i in card_list:
    grid_list.append(0)
card_matrix = [grid_list[x:x+GRID] for x in range(0, len(grid_list), GRID)]

#Generating win grid
win_list = []
for i in card_list:
    win_list.append(2)
win_matrix = [win_list[x:x+GRID] for x in range(0, len(win_list), GRID)]


#helpers
#reset grid input
def new_game():
    global card_list, card_grid, grid_list
    global turn_counter, click_counter, card_matrix

    #Generating random grid
    card_list = range(1, 9)
    card_list.extend(range(1, 9))
    random.shuffle(card_list)
    card_grid = [card_list[x:x+GRID] for x in range(0, len(card_list), GRID)]
    # looking at it this piece of code is redundant as new game is called before you start the draw handler

    #rest all flags and counters
    turn_counter = 0
    label.set_text("Turn = " + str(turn_counter))
    #have a better way of defining this for any grid size
    card_matrix = [grid_list[x:x+GRID] for x in range(0, len(grid_list), GRID)]

#handlers
#turn numbers into combinations of variables
def click(pos):
    global card_matrix, click_counter, card_pos_one, card_pos_two, turn_counter
    card_pos = find_card(pos)

    #if you have clicked a face down card
    #need to exclude borders so that when people click in it something odd doesn't happen
    if card_matrix[card_pos[0]][card_pos[1]] == 0:
        click_counter += 1
        if click_counter == 1:
            card_pos_one[0] = card_pos[0]
            card_pos_one[1] = card_pos[1]
            card_matrix[card_pos_one[0]][card_pos_one[1]] = 1
        elif click_counter == 2:
            card_pos_two[0] = card_pos[0]
            card_pos_two[1] = card_pos[1]
            card_matrix[card_pos_two[0]][card_pos_two[1]] = 1
        elif click_counter == 3:
            click_counter = 0
            turn_counter+= 1
            label.set_text("Turn = " + str(turn_counter))
            if card_grid[card_pos_one[0]][card_pos_one[1]] == card_grid[card_pos_two[0]][card_pos_two[1]]:
                card_matrix[card_pos_one[0]][card_pos_one[1]] = 2
                card_matrix[card_pos_two[0]][card_pos_two[1]] = 2
            else:
                card_matrix[card_pos_one[0]][card_pos_one[1]] = 0
                card_matrix[card_pos_two[0]][card_pos_two[1]] = 0

# finding the i and j coordinates of the card
def find_card(pos):
    card_pos = [0,0]
    card_pos[0] = int(((pos[0] - BORDER)**2)**0.5 // (BORDER + CARD_WIDTH))
    card_pos[1] = int(((pos[1] - BORDER)**2)**0.5 // (BORDER + CARD_HEIGHT))
    return card_pos


#handler - draw handler
def draw(canvas):

    #could probably do something clever like if it isn't a 2 return false, so when it's all 2 or true you do the win screen.
    if card_matrix == win_matrix: #- when do you update the win matrix?
        win_text_width = frame.get_canvas_textwidth("Congratulations, you win!!", 20) * 0.5
        canvas.draw_text("Congratulations, you win!!", [(WIDTH //2 - win_text_width), HEIGHT // 2], 20, "White")
    elif turn_counter >= GRID * 5:
        lose_text_width = frame.get_canvas_textwidth("Out of turns, try again!", 20) * 0.5
        canvas.draw_text("Out of turns, try again!", [(WIDTH //2 - lose_text_width), HEIGHT // 2], 20, "White")
    else:
        for i in range(GRID):
            for j in range(GRID):

                #colour coding cards by state
                card_colour = "Blue"
                text_colour = "White"

                if card_matrix[i][j] == 0:   #Facedown
                    card_colour = "Green"
                    text_colour = "Green"
                else:  #faceup
                    card_colour = "Blue"
                    text_colour = "White"

                #Calculations and drawing cards
                #Move the top left point, and calculate all points relative to that
                top_left = [((i * CARD_WIDTH) + ((i + 1) * BORDER)), ((j * CARD_HEIGHT) + ((j + 1) * BORDER))]
                top_right = [top_left[0] + CARD_WIDTH, top_left[1]]
                bottom_right = [top_left[0] + CARD_WIDTH, top_left[1] + CARD_HEIGHT]
                bottom_left = [top_left[0], top_left[1] + CARD_HEIGHT]

                #Draw cards in a grid with a border
                canvas.draw_polygon([top_left, top_right, bottom_right, bottom_left], 1, "White", card_colour)

                #Draw in top border
                canvas.draw_polygon([[0, (HEIGHT - BORDER)], [(WIDTH - BORDER), (HEIGHT - BORDER)], [(WIDTH - BORDER), HEIGHT], [0, HEIGHT]], 1, "Black", "Black")
                #Draw in side border
                canvas.draw_polygon([[(WIDTH - BORDER), 0], [WIDTH, 0], [WIDTH, HEIGHT], [(WIDTH - BORDER), HEIGHT]], 1, "Black", "Black")

                #Draw in text
                hc_width = frame.get_canvas_textwidth(str(card_grid[i][j]), 20) *0.5
                #Draw text in center of card
                canvas.draw_text(str(card_grid[i][j]), [((i * CARD_WIDTH) + (CARD_WIDTH // 2) + ((i + 1) * BORDER) - hc_width), ((j * CARD_HEIGHT) + (CARD_HEIGHT // 2) + ((j + 1) * BORDER) + 7)], 20, text_colour)


#create and register
frame = simplegui.create_frame("pairs", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.add_button("Reset", new_game)
label = frame.add_label("Turn = " + str(turn_counter))


#start
new_game()
frame.start()


#Scoring matrix
    #draws grid of 16 number cards
    #8 pairs
    #ignores clicks on exposed cards
    #clicking a card turns it over
    #if a pair cards stay untill start of next game, if not they flip back on click of a third card
    #number of turns counter
    #rest button
    #randomly shuffled cards on new game and reset
    #additional - use an image as the 'back' of the card - need to make sure it will load from anywhere

# What I have learned:
#It is all about the relationship between the 'layers' of data
#In this example the layers are [spacial co-ords of cards, i/j reference, state matrix]

#Old and new comparison - n dimension card grid matching
#old code:
# def find_i(pos):
#     global BORDER, CARD_WIDTH
#     if pos[0] >= BORDER and pos[0] <= (BORDER + CARD_WIDTH):
#         card_pos_i = 0
#     elif pos[0] >= (2 * BORDER + CARD_WIDTH) and pos[0] <= 2 * (BORDER + CARD_WIDTH):
#         card_pos_i = 1
#     elif pos[0] >= (3 * BORDER + 2 * CARD_WIDTH) and pos[0] <= 3 * (BORDER + CARD_WIDTH):
#         card_pos_i = 2
#     elif pos[0] >= (4 * BORDER +  3 * CARD_WIDTH) and pos[0] <= 4 * (BORDER + CARD_WIDTH):
#         card_pos_i = 3
#     else:
#         card_pos_i = 10
#     return card_pos_i
#
#New code
#def find_it(pos):
    # for x in range(0, GRID):
    #     if pos[0] >= (((x + 1) * BORDER) + (x * CARD_WIDTH)) and pos[0] <= ((x + 1) * (BORDER + CARD_WIDTH)):
    #         card_pos_i = x
    #         return card_pos_i
    #this doesn't work as iterators can't be made into intergers! so you need to do some eimple maths to get the x and y locations

#
#
#two more random cool pieces of code
##Generating random grid
# card_list = range(1, 9)
# card_list.extend(range(1, 9))
# random.shuffle(card_list)
# card_grid = [card_list[x:x+GRID] for x in range(0, len(card_list), GRID)]
#
# #Generating card grid
# grid_list = []
# for i in card_list:
#     grid_list.append(0)
# card_matrix = [grid_list[x:x+GRID] for x in range(0, len(grid_list), GRID

#Also you cannot redefine the height and width of the canvas after it has opened, you would have to save the data then reload the screen!
#as you are doing pos[0] - border can get negative values so suare then sqrt, or dont take off border

#A really handy set of values for testing
# CLICK [0]
# 10-85 -> i = 0 -> BORDER, BORDER + CARD_WIDTH
# 95-170 -> i = 1 -> 2*BORDER + CARD_WIDTH, 2*(BORDER + CARD_WIDTH)
# 180-255 -> i = 2 -> 3*BORDER + 2*CARD_WIDTH, 3*(BORDER + CARD_WIDTH)
# 265-340 -> i = 3 -> 4*BORDER + 3*CARD_WIDTH, 4(BORDER + CARD_WIDTH)
#
# CLICK [1]
# 10-110 -> j = 0 -> BORDER, BORDER + CARD_HEIGHT
# 120-220 -> j = 1 -> 2*BORDER + CARD_HEIGHT, 2*(BORDER + CARD_HEIGHT)
# 230-330 -> j = 2 -> 3*BORDER + 2*CARD_HEIGHT, 3*(BORDER + CARD_HEIGHT)
# 340-440 -> j = 3 -> 4*BORDER + 3*CARD_HEIGHT, 4(BORDER + CARD_HEIGHT)
