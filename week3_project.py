#python learning 1
#week 3
#project - the stopwatch game

#timer with interval 100ms - Done
#start stop reset buttons ( rest should set timer and counters to 0) - Done
#draw time elpased on canvas - Done
#format the time elapsed using a helper function - Done
#win/clicks counter in top right hand corner (two counters) - Done
#time limit 10 mins
#logic stop watch on whole seconds = win, if not = click - Done
#global boolean true when stop watch is running so can't keep clicking stop when watch is stopped - Done

#extras
#best of five, end screen that displays your final score and sucess rate
#if time elapsed > 10mins end game with annoying message and sucess rate
# sucess rate based comment like good job, try harder, ninja, your cheating etc etc




#imports
import simplegui

#globals
ticks = 0
timer_running = False
wins = 0
clicks = 0
A = 0
BC = 0
D = 0

#helpers and handlers - buttons
def start_timer():
    """Star the timer"""
    global timer_running
    timer_running = True
    timer.start()

def stop_timer():
    """Stop the timer, and logic for scoring"""
    global wins, clicks, D, timer_running
    if timer_running == True and D == 0:
        clicks += 1
        wins += 1
    elif timer_running == True:
        clicks +=1
    timer.stop()
    frame.set_draw_handler(draw)
    timer_running = False

def reset_all():
    """Start a new game"""
    stop_timer()
    global ticks, wins, clicks
    ticks = 0
    wins = 0
    clicks = 0

#helpers and handlers - timer
def tick():
    """fire draw handler on each tick"""
    global ticks
    ticks += 1
    frame.set_draw_handler(draw)

#helpers and handlers - draw messages
def draw(canvas):
    """Display time and in game comments"""
    global ticks, wins, clicks, A, BC, D
    if clicks < 5 and ticks < 6000:
        A = ticks // 600
        BC = (ticks % 600) // 10
        D = (ticks % 600) % 10
        canvas.draw_text(str(A) + ':' + '%02d' % (BC,) + '.' + str(D), [150, 100], 28, "White")
        canvas.draw_text(str(wins) + '/' + str(clicks), [360, 25], 20, "White")
    elif ticks < 6000 and clicks == 5:
        timer.stop()
        success_rate = int((wins*1.0 / clicks) * 100)
        canvas.draw_text("Game over", [155, 70], 22, "White")
        canvas.draw_text("Your success rate is " + str(success_rate) + " % ", [95, 100], 22, "White")
        canvas.draw_text(score_to_comments(wins), [score_to_format(wins), 130], 22, "White")
    elif ticks > 6000 and clicks < 5:
        timer.stop()
        canvas.draw_text("Too Slow", [165, 85], 22, "White")
        canvas.draw_text("Game Over", [155, 115], 22, "White")

#for now just use multiple draw statements, next iteration use the advice from
#https://stackoverflow.com/questions/33825723/multiple-line-text-unable-to-show-in-view

#Comments dictonary
def score_to_comments(wins):
    """comments based on score"""
    switcher = {
    0 : 'Better luck next time',
    1 : 'Keep trying',
    2 : 'Good job',
    3 : 'Well done',
    4 : 'Excellent',
    5 : 'I am sure you are cheating'
    }
    return switcher.get(wins, "oops")

#Score comment positioning dictionary
def score_to_format(wins):
    """formatting the comments based on width"""
    switcher = {
    0 : 115,
    1 : 155,
    2 : 165,
    3 : 160,
    4 : 162,
    5 : 93
    }
    return switcher.get(wins, "oopies")

#create and register
frame = simplegui.create_frame("lameGame", 400, 200)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_all, 100)
frame.set_draw_handler(draw)

#start
frame.start()

#What I have learnt from this
#you can pad numbers using python - no need for evil elif - although different syntax for different python versions
#you can only have one draw handler, the page is refreshed after each tick
#check you are working on the global variable, it's a global if you need it in more than one place!
#You have to redraw everything after every event, if doing this with a lot of stuff create a separate function for all the frame.set_draw_handler() statements in common
#the next step lives in the function that triggers it e.g. updating the score is in the code for pressing the stop button
#unless you are redrawing something based on variables then the logic goes in the draw handler
#when the game is over, stop timer!
#need draw handler before the start click in the start and register section to make sure you don't start with a banl screen
#time delays are harder than I thought, it's probably to do with the draw refresh

# would have to use a timer to create a delay in the program, if less than the required number of ticks then would have to do nothing, once ticks exceeded carry on with program.
# this would be nice for adding on delays moving between the screens in later games.
