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
    #every handler in the object also needs self
    #
