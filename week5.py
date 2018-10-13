#python learning 2
#week 5

#notes from lectures - more on Lists
#when copying the value of a tuple use list e.g. list(tuple); to create a mutable list
#list.append(n), list.pop(n), list.index(n), remove(n)
#pop removes the selected element fromt he list and returns it
#BUT len(list)
#in can match numbers or whole strings
#if x in list - returns t/f
#for x in list: action - performs the action for every x in list
#cannot remove from a list that you are iterating over, you have to create a separate list of stuff to remove, then if there is stuff in it remove those things from the origional list
#OR build a new list of the things you want to keep
#can store multiple pieces of data about an object in a list e.g ball = [1,2,"green"]; x,y,colour
#build something that works, test it, change it a little, test, change etc.
#boolean flags, keep track if something has happened or not

#Practice Exercise for Mouse and List Methods
#1) print mouse poition to console

#imports
import simplegui

#globals

#helpers and handlers - click event
def on_click(pos):
    print pos

#create and register
frame = simplegui.create_frame("click", 400, 400)
frame.set_mouseclick_handler(on_click)

#start
frame.start()

#2) print colour of displayed circle on click in circle
#imports
import simplegui, math

#globals
RADIUS = 20
BALLS = [[50, 100, "Red"], [150, 100, "Green"], [250, 100, "Blue"]]

#helper and handler - distance
def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

#helpers and handlers - click
def on_click(pos):
    for ball in BALLS:
        if distance(pos, ball) < RADIUS:
            print "Clicked the " + str(BALLS[BALLS.index(ball)][2]) + " ball"

#helpers and handlers - draw
def draw(canvas):
    for ball in BALLS:
        canvas.draw_circle([ball[0], ball[1]], RADIUS, 1, ball[2], ball[2])

#create and register
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(on_click)
frame.set_draw_handler(draw)

#start
frame.start()

#3) return position of element in list

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def day_to_number(day):
    global days
    for i in days:
        if i == day:
            return (days.index(day) + 1)
        else:
            return "Please enter a day of the week"

print day_to_number("Monday")
print day_to_number("Cheese")

#They have used this format:
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    pos = 0
    for i in range(len(day_list)):
        if day_list[i] == day:
            pos = i
    return pos

#Firstly they have retunred the index not the position (index starts at 0, position starts at 1 e.g. 1st)
#storing the index in a variable - good if you need to manipulate or pass on to another function

#4) Concatenating strings with a for loop

string_list = ["Lorem ipsum dolor sit amet,", "consectetur adipiscing elit,", "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Ut enim ad minim veniam," "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."]

s = " "
s = s.join(string_list)
print s

#ok so they actually want me to use a for thing...
def string_list_join(string_list):
    ans = ""
    for i in range(len(string_list)):
        ans += string_list[i]
    return ans

print string_list_join(string_list)

#first style uses existing method built into python...
#second populates an empty string with each piece of the first string, still gets to me that you can concatenate strings just by adding them. Adding letters is an odd concept.

#5) Balls balls everywhere!
#imports
import simplegui

#globals
BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = WIDTH

#helpers and handlers
def draw(canvas):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            canvas.draw_circle([2 * BALL_RADIUS * i + BALL_RADIUS, 2 * BALL_RADIUS * j + BALL_RADIUS], BALL_RADIUS, 1, "White", "White")



#create and register
frame = simplegui.create_frame("Ballz", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

#start
frame.start()

#ok, so this works by creating an iterator in each dimension, setting the range(10) makes it take the numbers 0-9, to position the inital ball by adding BALL_RADIUS to each coordinate, the multiplier gives the spacing between each sphere (2 * BALL_RADIUS * iterator).

#6) Challenge - polyline creator

#imports
import simplegui

#globals
poly_line = []

#helpers and handlers - click
def click(pos):
    global poly_line
    poly_line.append(pos)

#helpers and handlers - clear button
def clear():
    global poly_line
    poly_line = []

#helpers and handlers - draw
def draw(canvas):
    if len(poly_line) > 0:
        canvas.draw_circle(poly_line[0], 1, 1, "White", "White")
        canvas.draw_polyline(poly_line, 3, "White")
#this works but how come it doesn't throw an error when you only have one point?

#create and register
frame = simplegui.create_frame("polyline", 300, 200)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear, 100)
frame.set_mouseclick_handler(click)

#start
frame.start()

#What I have learnt
    #There are multiple ways to do something, think about what you are going to do next with the code, what follows the dRY rules, and what style you like
    #you can iterate in 2D you just need multiple iterators e.g. i, j, k (like the roots of -1)
    #often for i in len(list) is used rather than just iterating over list,
    #remember the logic goes in the draw function
