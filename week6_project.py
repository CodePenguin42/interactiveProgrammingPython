#python learning 2
#week 6 - OOP

# Week 6 project, building a simple version of blackjack


# Tips for building the thing!:
    # ace is either one or 11, the dealer wins ties
    # you would never count two aces and the dealer must count the ace as 11 unless they go bust
        # hand_value = sum(cards_in_hand, where ace = 1)
        # if no aces:
            #return hand_value
        # else: (one or more aces)
            # if hand_value + 10 <= 21:
                # return hand_value + 10
            # else return hand_value

    # After the player stands provided they aren't bust, need to determine when the dealer goes bust - WHILE LOOP:
    # map out the potential outcomes with pen and paper, then translate this into logic, then pseudocode, then code
    # map out the object structure - then check against the given template.

# My Notes on how to build it;
# Objects:
    # Card (face up or down, value, tuple index, ref for image, draw function) {get value, face up, draw a card, expose or hide}
    # Deck (list of cards) {shuffle, if deck != draw deck}
    # Hand [player or dealer] (list of cards, sum, status (bust, stand)) {sum, is bust, hit (appends a new card to a list) that list generates the location of each card}
    # [Game function in the stand mouseclick hander]
        # new game - shuffles deck, deals initial cards using hit method
        # main phase - on hit calculate player hand, and determine if player is bust - decrement score
                   # - on stand dealers turn, score appropriateley

# Three important things to figure out:
    # Objects, attributes, and methods
    # draw methods (board and game pieces)
    # game logic in click events
    # ensure code is readable, robust, DRY, and well commented.

#sing it with me "imports, globals, (helper functions), class, draw handler, create frame, create objects, start"
# Ok, so first thing I have noticed is that they are handling cards in a different way to me, for the first iteration of the game I will do it their way, next time I will give my way a go.
# for the record my way is to make a deck / list of cards given as a list of (value,suit) tuples.
# this can then be randomly shuffled, a counter will keep an eye on how many cards are draw and act as an index for referencing the next card.
# having this pair means the value of the card also gives the location
# will have to treat the ace and face cards separatley - which is actually a pain in the butt
# they split out the cards rank, value, and suit differently, meaning the game logic only has to handle the ace being awkward.
# their way seems simpleer... drat... it aint called the learning curve for nothing...

# imports
import random, simplegui


# globals - canvas
HEIGHT = 600
WIDTH = 600

# globals card sprite
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")
# cards are designed from the center to make the drawing clearer

# global variables
in_play = Flase
outcome = ""
score = 0

# globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
# this allows you to separate the rank (number on the face) from the (in game) value
# Using a dictionary to create rank value pairs
# Why is 10 a T, single character only?


#Classes - Card
class Card:
    """Descriptions of the rank and image of the card, and how to draw it"""

    # Initialise the object
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.rank = rank
            self.suit = suit
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
        # This ensures that you are only going to try and use real cards, I wonder if it stops people from drawing the same card twice later on...

    # Define the string
    def __str__(self):
        return self.suit + self.rank
        # Not in the way suit and rank are defined as strings

    # Return the suit of the given card
    def get_suit(self):
        return self.suit

    # Return the face value of the card e.g. King, Ace, 3 etc
    def get_rank(self):
        return self.rank

    # display card image at a given (but currently unknown) position - which is why pos is an argument
    def draw(self, canvas, pos):
        # cards are defined from their center point as that is needed for drawing an image
        card_loc =  (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                     CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # firstly the code is ligned up neatly one under the other - nicer presentation and easier for error checking
        # index method returns the index of the specifics caqrds rank or suit in their respective list - this is how they navigate the 2D drawing
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        # image location, portion location, portion size, draw location, draw size
        # draw location is defined from the top left hand corner as adding pos and center

# Classes - Hand
class Hand:
    """The actions and logic the player uses, defined as a group of cards"""

    # Initialise the class, no arguments as it is just a wrapper
    def __init__(self):
        self.hand = []

    # Describe the hand
    def __str__(self):
        if len(self.hand) > 0:
            my_hand = " ".join([(c.rank + c.suit) for c in self.hand])
            # remember [ expression for item in list if conditional ] square brackets around the whole thing!!
            return my_hand
        else:
            return "I have no cards in my hand"
        # human readable list of cards

    # Adds a card object to a hand - not just dealing a card, need both pull and push, this is pull
    def add_card(self, card):
        self.hand.append(card)

    # sum the value of the hand
    def get_value(self):
        pass

    # draw the hand on the canvas - pos here refers to the position of the hand (row of cards) on the canvas
    def draw(self, canvas, pos):
        pass

# Class - deck
class Deck:
    """a list of all the cards, which you can shuffle and remove cards from"""

    # Initialise the deck - no arguments as it is just a wrapper
    def __init__(self):
        self.deck = [Card(i,j) for i in SUITS for j in RANKS]
        #random.shuffle(self.deck)

    # print out the decks contents
    def __str__(self):
        if len(self.deck) > 0:
            my_deck = " ".join([str(self.deck[i]) for i in range(len(self.deck))])
            # this works as, each deck element is a card object and the string of a card object returns the suit/rank string, at least I think...
            return my_deck
        else:
            return "Your deck is empty"

    # Deal a card, the push to the pull
    def deal_card(self):
        return self.deck.pop(0)
        #removes the first element from the list

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)


#helper and handler function - new game
def restart():
    global outcome, in_play, score
    global new_deck, player, dealer

    #reset flags and statuses
    in_play = True
    score = 0
    outcome = ""

    #Create a new deck and shuffle it
    new_deck = Deck()
    new_deck.shuffle()

    #create a player and add cards to their hand
    player = Hand()
    player.add_card(new_deck.deal_card())
    player.add_card(new_deck.deal_card())
    print "Players hand"
    print player

    #create a dealer and add cards to their hand
    dealer = Hand()
    dealer.add_card(new_deck.deal_card())
    dealer.add_card(new_deck.deal_card())
    print "Dealers hand"
    print dealer

    #draw board


#Handler - Hit
def hit(click):
    pass
    # if not bust deal another card, calculate the hand value



# Handler - Stand
def stand(click):
    # play the dealers hand
    # decide the winner
    # update score
    pass


#Handler - draw handler
def draw(canvas):
    #draw board elements
    #draw deck
    #draw cards
    pass

#Create frame and register
frame = create_frame.simplegui("BlackJack", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
# Need a separate command to change the background colour
frame.add_button("Deal", restart, 100)
frame.add_button("Hit", hit, 100)
frame.add_button("Stand", stand, 100)
frame.set_draw_handler(draw)


# start
restart()
frame.start()


# Notes from the learning curve:
    # remember arguments in obects are always self.arg!!!
    # __str__ only needs to return not print a string
    # random.shuffle(thing) does not need assigning to anything e.g. new_thing = random.shuffle(thing) -> NOO!!!
    # [i] creates a list containing that element, not the element itself
    # CHECK ARE YOU USING self.thing inside the object
    # CHECK do you have all the brackets in the right place, e.g. () [] and no brackets, are any unclosed
    # do you mean len(thing) or range(len(thing))?

# Want to do an analysis of their testing templates as they seem like a good thing to know how to build for yourself
# Also an analysis of their instructions - gives you a good order to build projects
    # Rule of thumb 0) - design objects, their (inter)actions, then methods, build bones of each
    # Rule of thumb 1) - get the code in before the pictures
    # Rule of thumb 2) - fill in init and strings then start with the most fundermental object and build in the methods
    # all each method has to do is isolate and return the thing in question e.g. pop a card, doesn't need ot save it anywhere, it's transient
    # Interesting but unhelpful self.__name__ will return the name of the class you are in
