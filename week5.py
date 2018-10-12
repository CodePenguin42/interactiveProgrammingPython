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
frame = simplegui.create_frame("clcik", 400, 400)
frame.set_mouseclick_handler(on_click)

#start
frame.start()

#2) print colour of displayed circle on click in circle
#imports
import simplegui, math

#globals
RADIUS = 20
BALL = [[50, 100, "Red"], [150, 100, "Green"], [250, 100, "Blue"]]

#helper and handler - distance
def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

#helpers and handlers - click
def on_click(pos):
    for ball in BALL:
        if distance(pos, ball) < RADIUS:
            print str(BALL[ball][2])

#helpers and handlers - draw
def draw(canvas):
    canvas.draw_circle([BALL[0][0], BALL[0][1]], RADIUS, 1, BALL[0][2], BALL[0][2])
    canvas.draw_circle([BALL[1][0], BALL[1][1]], RADIUS, 1, BALL[1][2], BALL[1][2])
    canvas.draw_circle([BALL[2][0], BALL[2][1]], RADIUS, 1, BALL[2][2], BALL[2][2])

#create and register
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(on_click)
frame.set_draw_handler(draw)

#start
frame.start()

#okay so look at this a little later and finish the for statment later...
