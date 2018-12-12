#python learning 2
#week 6 - OOP

#Notes from lectures
#Object is a collection of rules or properties that can be called upon or manipulates
#This segregation of code makes objects interchangable, and programmes incredibly flexible with minimum effort
#it is also a very different style of thinking and feels like a whole other language
#E.g. when making black jack:
    #Physical things that I need to represent [card, hand, cards]
    #card = number, suit, image
    #hand = collection of cards & hit, score total
    #deck = collection of cards & shuffle, deal a card
#the types or classes you define above are a mix of types and values of data and their behaviour, so hand and deck are kinda different
#primary objective of OODesign is to make code as reusable as possible
#e.g. cards don't have value inherently, e.g. an Ace in poker is different to an ace in 21
#In the videos they talk about putting the calcs in the hand class, but shouldn't they be abstracted from that into a game class so you can put the rules of the game in the game class and separate the concept of a hand of cards.
#abstraction is key, it is the process of separating how a class behaves from how you interact with it

#Notes from OOP&Classes video
#https://www.youtube.com/watch?reload=9&v=xzjHT6CVcAA
#A class is a list of instructions, properties, and functions that define an object
#The object however does not exist untill an instance of the class is created
#each instance of an object is unique, a string method can describe this, and is called whenever you print the object
#A variable in a class is called an attribute
#A function in a class is called a method
#There is a cool example of this - the infinite tie generator....

#imports
import simplegui

#images
joe = simplegui.load_image("http://farm9.staticflickr.com/8560/8876956295_fa57030cf4_o.png")
img_sz = (171, 370)
img_ctr = (img_sz[0]//2, img_sz[1]//2)
#Load up images, specifying the size and center.

#globals
COLORS = ["Blue", "Red", "Yellow", "Green", "Maroon", "Aqua", "Fuchsia", "Lime", "Teal", "Olive", "Silver", "Purple"]
color_key = 0
ties = []
#defining global:
    #the list of colours to be iterated through
    #using a key which can be incremented
    #an empty list for all the instances of ties to be created

#classes
class Tie:
    def __init__(self):
        self.height = 150
        self.width = 30
        self.color = "White"
        self.location = (50, 200)
        #What you need to make a tie, dimension, colour, and location
        #why oh why is only self referenced, because you aren't changing anything about it upon creation, each one "spawns" in the same place and the same colour

    def __str__(self):
        return "I am a " + self.color + " tie."
        #A string to communicatethe content of the class

    def draw(self, canvas):
        #I didn't know you could define x and y like this, kinda neat
        x, y = self.location[0], self.location[1]
        #center of the rectangle that defines the tie
        w, h = self.width, self.height
        #dimensions of the rectangle that defines the tie
        A = (x - w/4, y - h/2)
        B = (x + w/4, y - h/2)
        C = (x + w/8, y - 3*(h/8))
        D = (x - w/8, y-3*(h/8))
        E = (x - w/2, y + h/4)
        F = (x, y + h/2)
        G = (x + w/2, y + h/4)
        #These are the coordinates of a tie, relative to rectagle that encompasses it
        canvas.draw_polygon([A,B,C,D], 1, "Black", self.color)
        canvas.draw_polygon([C,D,E,F,G], 1, "Black", self.color)
        #draw the two polygons that define the tie

    def change_color(self, color):
        self.color = color
        #update the colour of the tie object

    def drag(self, pos):
        self.location = pos
        #update the location of the tie object

# event handlers
def drag(pos):
    ties[-1].drag(pos)
    #select the last tie create it and drag it

def new_tie():
    ties.append(Tie())
    #create a new tie

def new_color():
    global color_key
    #access the global colour key to change the colour of the last tie created
    color_key += 1
    color_key %= 12
    #the mod wraps the iterator to the length of the list
    ties[-1].change_color(COLORS[color_key])
    #reference the index of the colour list

#draw handler
def draw(canvas):
    canvas.draw_image(joe, img_ctr, img_sz, (250, 215), img_sz)
    #draw the picture of the silly man

    for tie in ties:
        tie.draw(canvas)
        #draw every tie that has been made

#create frame, labels, and buttons
frame = simplegui.create_frame("Scott's Revenge", 400, 400)
frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)
frame.add_button("Make New Tie", new_tie, 100)
frame.add_button("Change Color", new_color, 100)
frmae.add_label("")
frame.add_label("Drag a tie onto Joe")
frame.add_label("")
frame.add_label("Or a hundred!!")
#use blank labels as line spacers

# start
frame.start()

#Interesting principals
    #drawing an image relative to a box then resizing that box, or moving it's center, then redrawing everthing relative to that
    #every handler in the object also needs self, not just tbe usual

# Practice exercises Part 1
# 1) Make an empty class called Tile
class Tile:
    pass

# 2)  Create two instances of Tile
tile_one = Tile()
tile_two = Tile()

# 3) create two numbered tiles
class Tile:
    def __init__(self, num):
        self.number = num

tile_one = Tile(3)
tile_two = Tile(4)

# 4) create a get number method (AKA a getter method)
class Tile:

    def __init__(self, num):
        self.number = num
    #changing the name inside the class to number, rather than the varible num

    def get_number(self):
        return self.number
    #I think num is not an argument here as it isn't changing but it is defined in the global scope

tile_one = Tile(3)
tile_two = Tile(4)
#creating two instances of tile.

print tile_one.get_number()
print tile_two.get_number()
#object.method(), need the paren

# 5) Add exposed and hidden class
class Tile:

    #initialse the class
    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

    #create interesting methods so it can do stuff
    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self, exposed):
        self.exposed = True

    def hide_tile(self, exposed):
        self.exposed = False

#All the data relating to the tile is now grouped together in one place, rather than separate like in the memory game where things are grouped relative to position and there is a whole new variable for each state.

# 6) Add a __str__ method to give a status update
class Tile:

    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self, exposed):
        self.expose = True

    def hide_tile(self, exposed):
        self.exposed = False

#Test it!
tile_one = Tile(3, True)
print tile_one

#prints...
Number is 3, exposed is True

# 7) Add in the draw function
    #facedown = green polygon
    #faceup = text at tile location
    #add location of tile class and implement draw method inside draw function as yoou need to pass it canvas
    #use bottom left hand corner as origin point for each tile

# imports
import simplegui

# globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# imports, globals, handlers, create, register, all exist outside the Tile class

class Tile:

    def __init__(self, num, exp, pos):
        self.number = num
        self.exposed = exp
        self.position = pos

    def __str__(self):
        return "Number is %s, exposed is %s." % (self.number, self.exposed)
        # I like this method, less messing with " and +

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self, exposed):
        self.expose = True

    def hide_tile(self, exposed):
        self.exposed = False

    def draw_tile(self, canvas):
        pos = self.position
        # redefining this inside the draw function
        if self.exposed:
            text_position = [pos[0] + 0.2 * TILE_WIDTH, pos[1] - 0.3 * TILE_HEIGHT]
            #Modify the position of the text using a multiplier so the text position scales with the dimensions of the tile
            canvas.draw_text(str(self.number), text_position, TILE_WIDTH, "White")
        else:
            tile_corners = (pos, [pos[0], pos[1] - TILE_HEIGHT], [pos[0] + TILE_WIDTH, pos[1] - TILE_HEIGHT], [pos[0] + TILE_WIDTH, pos[1]])
            # starting from bottom left, clockwise
            canvas.draw_polygon(tile_corners, 1, "Green", "Green")

# design one tile using the variables of the class and globals, not thinking about it as part of a whole design of tiles, that comes later and outside the class, or perhaps in a class of it's own.

# draw handler
def draw(canvas):
    tile_one.draw_tile(canvas)
    tile_two.draw_tile(canvas)
    # These are needed to be created manually, could make a button to add more
    # Also the code to draw tiles appears before the code to make them. Kinda odd - will figure it out eventually

# create frame, add extras
frame = simplegui.create_frame("Pairs", 2 * TILE_WIDTH, TILE_HEIGHT)
# The '2' here will need to be dynamically updates as you add in more tiles
frame.set_draw_handler(draw)
# This calls the draw function that in return uses the draw_tile method

# create two tiles
tile_one = Tile(3, True, [0, TILE_HEIGHT])
tile_two = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])
# the positions of the tile is entered manually, need a better way of doing this, again this lives outside the class


# Start
frame.start()

# Notes:
    # they are using the bottom left corner as it is the same reference frame as draw_text, also they defined things anti-clockwise
    # sing it with me "imports, globals, class, draw handler, create frame, create objects, start"
    # this is a different style of thinking, focusing on one specific part of the game rather than interpolating the structure of the variables from the structure of the game. More flexible and easier to build up iterations of.
    # pos is reserved for the location of the click, use loc for refering to the spacial coords of the card

# 8) Changing state
    # put the logic of the game in a method so it isn't clogging up a click or draw handler.

# imports
import simplegui

# globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# class
class Tile:

    # initialise the class and assign attributes
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # define a human friendly descriptive string
    def __str__(self):
        return "Number is %s, exposed is %s" % (self.number, self.exposed)

    # get the tile number
    def get_number(self):
        return self.number

    # return state of a tile
    def is_exposed(self):
        return self.exposed

    # flip a tile up
    def expose_tile(self):
        self.exposed = True

    # flip a tile down
    def hide_tile(self):
        self.exposed = False

    # determind if tile has been clicked
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return inside_hor and inside_vert
        # so inside_hor and inside_vert will return True or False - without having to use and in an if
        # this is much neater and easier to read, and mathematically intuitive

    # draw a tile based on state
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0], loc[1] - TILE_HEIGHT], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0] + TILE_WIDTH, loc[1]])
            canvas.draw_polygon(tile_corners, 1, "Green", "Green")

# handlers
def draw(canvas):
    tile_one.draw_tile(canvas)
    tile_two.draw_tile(canvas)

def click(pos):
    if tile_one.is_selected(pos):
        tile_one.hide_tile()
    if tile_two.is_selected(pos):
        tile_two.expose_tile()

# create frame and register
frame = simplegui.create_frame("Pairs", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# create tiles
tile_one = Tile(3, True, [0, TILE_HEIGHT])
tile_two = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

# start frame
frame.start()

# Notes
    # so hide and expose only take self as arguments, you only need to include arguments that are coming in from outside the class e.g. where you have clicked, or if a button changes something
    # this is a kind of boring program, it only had two tiles and you can only change the states once to improve it you would have to:
        # generate and randomly shuffle a deck of tiles
        # toggle the hidden exposed states
        # lay cards out in a grid and draw them - probably using two for iterators and a deck object
        # have win and loss conditions
            # would the logic for this still be in the draw handler or in the game class
            # you can see where the bottom up structure of django comes from

# More practice exercises
# build a character / avatar that has specified visual characterstics and two gold stashes
# methods needed : find gold, bury gold, encounter fairy

# class
class Avatar:

    def __init__(self, name, hair, initial_gold):
        self.name = name
        self.hair_colour = hair
        self.gold_in_bag = initial_gold
        self.burried_gold = 0.0

    def __str__(self):
        return "%s has shining %s hair, a bag of %s gold, and a hidden stash of %s gold pieces." % (self.name, self.hair_colour, self.gold_in_bag, self.burried_gold)

    def find_gold(self, amount):
        self.gold_in_bag += amount

    def bury_gold(self, amount):
        self.gold_in_bag -= amount
        self.burried_gold += amount

    def sprinkled_with_fairy_dust(self, multiplier):
        self.gold_in_bag *= multiplier

# Test
Alice = Avatar("Alice", "blonde", 10)
# the name and hair colour have to be strings here or else the object will not be created.
Alice.bury_gold(5)
print Alice
Alice.find_gold(6)
print Alice
Alice.sprinkled_with_fairy_dust(2)
print Alice

# Notes
    # is put in a game like way but could equally be used for finance, be it a bank account or for a business
    # origionally the multiplier was fixed, but I made it variable for more interesting encounters.
    # could add in some random events so characters have to spend gold, and win/loose conditions when they run out of gold

# Notes on week 6b - Tiled Images, visualising objects and aliases, tips and tricks
    # draw a 4x13 deck layout, need to have a draw handler for a card and the deck
    # use card center as that is one of the requirement for the draw handler
    # if you want to use an image from drop box get the share link then replace the www with dl
    # When using your own images the first time the ncode is run the image is cached, will need to clear image cache to check that all is working well for all people who use the code
    # aliasing - when you rename an object both the names will access the same object
    # if you want to create a new object with the same parameters you have to use name = class(etc)
    # you can create an alias for the list of parameters and use it to create and update multiple objects simulataneously
    # typing the same list by hand into an object constructor will generate a seemingly identical object, that is independent of the list.
    # if you change one part of the list the shared state either directly or referencing the specific part of the object changes the list, and all the objects it connects to.
    # if you want to use one variable shared state to define multiple independent states use the list function.
        # e.g. list(shared_state) => unliked objects but just using shared_state in init will keep them linked
        # this is because list creates a local copy of the shared_state
    # implicitly the init method always returns the object being created
    # first letter of a class name is capitalised
    # for loops - know how many time it will loop and cannot change the data you are looping through
    # bring on the while loop:
def countdown(n):
    i = n
    while i >= 0:
        print i
        i -= 1
countdown(5) -> 5 4 3 2 1 0

    # the equivalent for loop looks like this (remember you are counting backwards!)
def countdown(n):
    for i in range(n, -1, -1):
        print i

    # for has to build a long list then print it out - problematic for large numbers
    # infinite series will kill your browser, codeskulptor should have a 5s cut out

# Practise Exercises Part 2
# Create a person class giving name and birthday

class Person:

    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year

    def __str__(self):
        return "My name is %s %s and I was bornm in %s" % (self.first_name, self.last_name, self.birth_year)

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def age(self, current_year):
        return current_year - self.birth_year
        # you don't have to get the year at this point - not well supported in codeskulptor

# 2) return average age of a list of person

def average_age(person_list, current_year):
    total = 0
    for p in person_list:
        total += p.age(current_year)
    return total / float(len(person_list))

# 3) create the class Student which contains the class person
    # you don't seem to formally import one class into the other, just use the lowercase name

class Student:

    def __init__(self, person, password):
        self.person = person
        self.password = password
        self.projects = []

    def get_name(self):
        return self.person.full_name()

    def check_password(self, password):
        return student.password == password

    def get_project(self):
        return self.projects()

    def add_project(self, project):
        return self.projects.append(project)

# 4) Search for students and add their project
    # only use student objects to manipulate student attributes

def assign(student_list, student_name, student_password, project):
    for s in student_list:
        if s.get_name() == student_name and s.check_password(student_password):
            if s.get_projects().count(project) == 0:
                s.add_project(project)
# count is an inbuilt python method that returns the number of times that an item appears in a list - really handy
# note to self look up more of these very useful python methods

# 5) Start making a game of pairs
    # build tile class
    # generate list of duplicate numbers and shuffle
    # draw a straight line of tiles (boring, improve later), all initially hidden
#sing it with me "imports, globals, helper functions, class, draw handler, create frame, create objects, start"

# 6) turn over tiles with mouseclick

# 7) add in the rest of the game level logic in the mouse click handler

# imports
import simplegui, random

# Globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# Helpers - new game
    # also used to initialise variable / dynamic globals
def new_game():
    global my_tiles, state, turns

    # generate a list from 1 - distinct tiles and shuffle
    tile_list = range(1, DISTINCT_TILES + 1) * 2
    # previously used the extend method, but you can just multiply lists to create and append a duplicate
    random.shuffle(tile_list)
    my_tiles = [Tile(tile_list[t], False, [TILE_WIDTH * t, TILE_HEIGHT]) for t in range(DISTINCT_TILES * 2)]
    # cannot start a list with for, for lists it "do this" for i in thing - list comprehension
    # [for t in tile_list: Tile(tile_list[t], False, [TILE_WIDTH * t, TILE_HEIGHT])]
    # thing is not my_tiles it has to be the numbers 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 other wise t is the numbers 1,2,3,4,5,6,7,8. which when passed to the draw handler stacks cards in the wrong locations

    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))

# Class - Tile
class Tile:

    # initialise attributes
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # print the status of the object
    def __str__(self):
        return "The number is %s, is exposed is %s, and its location is %s" % (self.number, self.exposed, self.location)

    # get the value on the tile
    def get_number(self):
        return self.number

    # return the state of the tile
    def is_exposed(self):
        return self.exposed

    # flip tile face up
    def expose_tile(self):
        self.exposed = True

    # flip tile face down
    def hide_tile(self):
        self.exposed = False

    # draw method for draw handler for each tile
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "White", "Green")

    # has a tile been clicked on?
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert

# the draw handler
def draw(canvas):
    for t in my_tiles:
        t.draw_tile(canvas)

# handlers - mouseclick
def click(pos):
    global state, turns, first_tile, second_tile
    # need first and second tiles as globals as they are accesses by the if in the else (game logic)

    for t in my_tiles:
        if t.is_selected(pos) and not t.is_exposed():
            clicked_tile = t
            clicked_tile.expose_tile()
            # these have to be two separate lines cant expose tile and change it's name
            print type(clicked_tile)
    # iterate over all the tiles and test if the position of the click lies within the boundaries of that card - ok for short lists not long ones
    # if that tile has been clicked and isn't already exposed, expose the tile and create a local variable clicked tile and save which tile has been clicked

    # game logic
        # state 0 before the click
        # state 1 after first click
        # state 2 after second click (match or hide), update turns

    if state == 0:
        state = 1
        first_tile = clicked_tile
    elif state == 1:
        state = 2
        second_tile = clicked_tile
        turns += 1
        label.set_text("Turns = " + str(turns))
    else:
        if first_tile.get_number() != second_tile.get_number():
            first_tile.hide_tile()
            second_tile.hide_tile()
        state = 1
        # assuming you have clicked on another card a third time, this turns over a card and triggers the matching logic
        first_tile = clicked_tile
        # esentially you go through state 0 once at the start of the game then loop between state 1 and 2.




# create frame and control objects
frame = simplegui.create_frame("Pairs", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
frame.set_mouseclick_handler(click)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# start the frame
new_game()
frame.start()

# Notes /  Learnt / Advantages and differences with previous method
    # much neater way of determining wether a tile has been clicked on
    # globals, new game, class, other handlers, create, start
    # remember it is set_mouseclick_handler, not add_mouseclick_handler!!
    # stylistic differences:
        # I like the way this code loops through the last two states only creates smoother gameplay
        # iterate over tiles to find the one that has been clicked rather than going from a click location to a tile
        # they separated out the conditions for flipping over a card I combined them as I don't like leaving blank spaces where I keep expecting code
        # used is_selected rather than calculating the position of the card and returning the index - easier to adjust to the 2D grid
    # no fancy win or lose conditions
    # also they origionlly used a redd border - very not cool











# 8) make the 2D version

# imports
import simplegui, random

# Globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
GRID = 4
DISTINCT_TILES = GRID *2
WIDTH = TILE_WIDTH * GRID
HEIGHT = TILE_HEIGHT * GRID

# Helpers - new game
def new_game():
    global my_tiles, state, turns

    tile_list = range(1, DISTINCT_TILES + 1) * 2
    random.shuffle(tile_list)
    tile_grid = [tile_list[x:x+GRID] for x in range(0, len(tile_list), GRID)]
    my_tiles = [Tile(tile_grid[i][j], False, [TILE_WIDTH * i, TILE_HEIGHT * (j + 1)]) for i in range(GRID) for j in range(GRID)]
    # this generates the correct location and outputs a list of objects, not a nested list
    #which makes it the same format of data as in the previous version

    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))

# Class - Tile
class Tile:

    # initialise attributes
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # print the status of the object
    def __str__(self):
        return "The number is %s, is exposed is %s, and its location is %s" % (self.number, self.exposed, self.location)

    # get the value on the tile
    def get_number(self):
        return self.number

    # return the state of the tile
    def is_exposed(self):
        return self.exposed

    # flip tile face up
    def expose_tile(self):
        self.exposed = True

    # flip tile face down
    def hide_tile(self):
        self.exposed = False

    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert
        #this actually works in 2D not just one as it looks at everything relative to loc, which is defined in the 2D grid separate to the game logic

    # draw method for draw handler for each tile
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "White", "Green")


# the draw handler
def draw(canvas):
    for i in range(GRID ** 2):
        my_tiles[i].draw_tile(canvas)

# handlers - mouseclick
def click(pos):
    global state, turns, first_tile, second_tile

    # this is done in separate steps to keep it robust
    for tile in my_tiles:
        if tile.is_selected(pos):
            clicked_tile = tile

    if clicked_tile.is_exposed():
        return

    clicked_tile.expose_tile()

    if state == 0:
        state = 1
        first_tile = clicked_tile
    elif state == 1:
        state = 2
        second_tile = clicked_tile
        turns += 1
        label.set_text("Turns = " + str(turns))
    else:
        if first_tile.get_number() != second_tile.get_number():
            first_tile.hide_tile()
            second_tile.hide_tile()
        state = 1
        first_tile = clicked_tile


# create frame and control objects
frame = simplegui.create_frame("Pairs", WIDTH, HEIGHT)
frame.add_button("Restart", new_game)
frame.set_mouseclick_handler(click)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# start the frame
new_game()
frame.start()

# to make the 1D game 2D, just change the way the loc variable is created pass it to the Tile class.
# THE GAME LOGIC REMAINS UNCHANGED
# when bored add a pretty border to the game!
