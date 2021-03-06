# List of all the key variables that I keep forgetting the names of:
  # in declarative programming (stuff without objects) all the variables you are working with are combined with the logic that you are working with all in the one place. This makes them easy to find and remember.
  # I on the other hand have an appauling short term memory and would like to put together an index of the important variables and attributes so that I remember what they are. I will end up making notes on what they all do too (and what they do to each other!)
  # This will be a good habbit to have for when I am working as part of a larger project so people can easily get into a large page of code with a guide.
  # It is also a good post Christmas warm up to get me familiar with the code I am playing around with - it might prove not worth it for the effort, but it might not.

    # Game level variables and attributes:
score = 0
lives = 3
time = 0

    # mathematically important functions:
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2))

# Ways of adding vectors - depending on how they are defined
a = [1,0]
b = [2,3]
c = [a[0]+ b[0], a[1]+b[1]]

self.pos[0] += self.vel[0]
self.pos[1] += self.vel[1]

    # Ship variables and atributes:
TURN_ANGLE_VEL_INC = 0.02
self.pos = [pos[0], pos[1]]
self.vel = [vel[0], vel[1]]
self.thrust = False
self.angle = angle
self.angle_vel = 0
self.image = image
self.image_center = info.get_center()
self.image_size = info.get_size()
self.radius = info.get_radius()

# good number ranges:
    # rock angle_vel 0.02 - 0.08
    # rock vel - rand float from 0- 2pi, then convert to cartesian.

# Comparison of the thing I created at the end of wk 7 and the template given in week 8 (week8_template.py):
# imports:
    # I do mine on the same line, they break theirs out onto separate lines, any reason why?
# Classes:
    # I made a str method, to print out all the fields in a human understandable form, this step was ommited from the template; but I found it good practice
# Ship.draw() and ship.update():
    # I left the updates in the draw handler method, rather than putting them in the update method, the calling update then calling draw.. oops
# ship.thrusters()
    # rewind sound in a different place, they turn thrust on rather than thrust true.
# keyhandler functions:
    # they consolidate the up right and down left into the same function, much neater.
    # but they do an elif where I did a dictionary
    # they got rid of the turn angle vel inc
# shoot function:
    # the fire boolean flag seems to have dissapeared
# Sprite:
    # I have put the updates inside the draw handler - not helpful when update becomes more complex
# click mousehandler:
    # They have added one to give a start screen, I like the inside thing though, would be helpful as a stand alone function in other projects
# Rock spawner:
    # different ways of generating a random number random.random() vs random.choice

# General conclusions:
    # consolidate similar keyhandler functions, but also put into a dictionay as I like dictoinaries and the mapping is right
    # reduce the number of 'magic numbers' in code, bring back turn angle vel inc!
    # split out the update from the draw handler

    # Although my code is different I can pick up working from their template - go skills
