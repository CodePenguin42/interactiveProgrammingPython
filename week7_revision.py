# Python Learning 2
# Week 7
# Project introduction

# MIT style brainstorming - when in doubt make a Venn diagram, the solution is the intercept of all the circles
# In this case they had Rice Uni, Space, Big Bang Theory - they came up with Mike Massimino
# Dev process, single rock and single missile. Next week deals with groups of images
# time for some revision!
    # The different meanings of %s, %d, %f, %g - not python 3.6, check latest code when you need
    # %s - forced the thing to become a string keeping the formatting
    # %d - truncates the number e.g %d of 4.3 -> 4
    # %f - forces the number into a float format e.g. %f of 4.3 -> 4.3000
    # %g - makes the number generic e.g. %g of 4.3 -> 4.3
    # You cannot convert a string into a number using the above %'s
    # if something is a global then any changes made to it in the function will be 'saved' to the global name spce - NB, only for dynamic globals
    # both static and dynamic globals can be seen inside a function when they aren't declared as globals inside the function as globals
    # note the """ sometimes messes up atoms text colour coding
    # inputs and labels have a thing = frame.add....., so you can get and set text
    # when decreasing somethings size make sure it's current size is bigger than the decrement, equally when moving something make sure the position it is going to is within the game gutters
    # experiment with creating delays in various simplegui programms using a timer
    # need to use list(thing) to generate an identicle non linked copy of a list, saying list_a = list_b creates a pair of linked lists
    # dictionaries are good for multiple 1:1 mappings, where the inputs and putputs are known e.g. not a range. Could do with a way of it working for ranges, it would be so useful!! Perhaps some kind of flag method?
    # use gutters for keeping a non point 'object' within a given range e.g. ball in pong
    # pos += vel, to give contant xpeed e.g. 0 acceleration (with infinite acceleration between standstil and moving, but hey it's not a real system)
    # when you are updating something or drawing it, for an image use the center as the reference point, for a shape use the top left hand corner in line with the axis system
    # segregate repeated patterns of code - either into functions or objects, can be either properties (e.g. key information for an image), or behaviours (e.g a card in a game of black jack) or a collection of objects with or without new bwhaviours (e.g. a hand or deck of cards)
    # This abstraction separates when you should perform a complex set of actions and the detail of those actions.
    # Like evolutionary developmental biology, it makes it easy to change when stuff happens, with the added bonus that you can change what happens (far more easily than changing the structure of a protein)
    # class - general example of an object made of attributes (variables) and methods (functions)
    # an object does not exist until the class is called
    #  objects normally contain a draw method
    # remember it is always self.attribute or self.method within the class as when you make an object you will need replace self with the name of the object.
    # all objects should have an __init__ and a __str__ to describe all their attributes in a way that the computer and coder can understand; respectivley.
    # to move a child object between parent objects is must be popped from one and added to the other. e.g. need a remove / push method, that is the parameter for the add / pull method
    # all attributes are listed in the __init__ but only those that need to be specified each time at creation or come from an external source go in the paren e.g. all avatars start with a fixed amount of gold, but you set the physical characteristics upon creation.
    # you can alias an object OR list of parameters so they are linked or are separate (name = class(etc)) - if liked can update multiple objects without a for loop.
    # THE ABOVE IS VERY POWERFUL AND SUBTLE
    # cannot change the data you are looping through in a for loop - need a while loop for this
    # use flags to create various loops in the one elif statement, with initial, ingame, end paramters; all in the one statement, you just loop through the in game ones when required.
    # sing it with me "imports, globals, helper functions, class, (draw) handler, create frame, create objects, start"
    # use flags to subtly modify behaviour - fuzziness in the logic
    # testing - check type and functionality of classes made, and their outputs, ensure have the right imports and globals
    # The rules of thumb:
        # identify objects, design classes including their properties and (inter)actions
        # map out a skeleton of code with init and str, and names of all methods
        # follow the various logical pathways and build the methods, adding flags etc and you need; starting from most fundermental object or interaction - test code
        # add in graphics and gui features - test will load sounds and images on any set up
        # try and break what you have just made - make required improvments

# and now for something completley different....
