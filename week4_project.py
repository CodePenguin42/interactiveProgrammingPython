#python learning 1
#week 4
#Mini Project - Pong

#Instructions
#Draw court paddles scores and ball - Done
#get paddles moving - Done
#keep paddles on screen - done
#get ball moving - Done
#set boundaries for bounce and score - Done
#update score - Done
#ball spawn moving towards the player that scored the last point - Done
#new game button - done
#win function and win screen - Done
#test - Done
#implement cool ideas - for v2+
# DO IT WITH OBJECTS!! - and with the inside function / method



#import
import simplegui, random

#globals
#Frame
WIDTH = 600
HEIGHT = 400

#Paddles
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_CENTER_TOP = (HEIGHT / 2) - (PAD_HEIGHT / 2)
PAD_CENTER_BOTT = (HEIGHT / 2) + (PAD_HEIGHT / 2)
paddle_vel_mult = 6.0
paddle_one_pos = [[0, PAD_CENTER_TOP], [PAD_WIDTH, PAD_CENTER_TOP], [PAD_WIDTH, PAD_CENTER_BOTT], [0, PAD_CENTER_BOTT]]
paddle_two_pos = [[WIDTH - PAD_WIDTH, PAD_CENTER_TOP], [WIDTH, PAD_CENTER_TOP], [WIDTH, PAD_CENTER_BOTT], [WIDTH - PAD_WIDTH, PAD_CENTER_BOTT]]
paddle_one_vel = [0, 0]
paddle_two_vel = [0, 0]

#Ball
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-2, -2] #px per 1/60s
#allows you to mess around with average ball speed
ball_vel_mult = 0.6
#allows you to increase speed of ball on paddle bounce
ball_vel_bounce = 1.2
ball_gutter_upper = BALL_RADIUS
ball_gutter_lower = HEIGHT - BALL_RADIUS
ball_gutter_left = BALL_RADIUS + PAD_WIDTH
ball_gutter_right = WIDTH - BALL_RADIUS - PAD_WIDTH

#Scores
score_one = 0
score_two = 0
score_total = 0
LEFT = False
RIGHT = True

#Register helper and handler functions
#helpers and handlers - on score
def score_left():
    global score_one, score_total, LEFT, RIGHT
    score_one += 1
    score_total += 1
    RIGHT = False
    LEFT = True
    spawn_ball()

def score_right():
    global score_two, score_total, LEFT, RIGHT
    score_two += 1
    score_total += 1
    RIGHT = True
    LEFT = False
    spawn_ball()

#helpers and handlers - ball spawn
def spawn_ball():
    global ball_pos, ball_vel, ball_vel_mult, LEFT, RIGHT
    #put ball back in middle
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #set random motion
    ball_vel[0] = (ball_vel_mult * (random.randrange(400.0, 700.0))/100)
    #set sign for vertial motion
    ball_vel_sign = [1,-1]
    ball_vel[1] = (ball_vel_mult * (random.randrange(400.0, 700.0))/100) * random.choice(ball_vel_sign)
    #if left scored make ball_vel[0] -ve
    if LEFT == True:
        ball_vel[0] = ball_vel[0] * -1.0

#helpers and handlers - paddle, ball, corner bounce
def ball_reflect():
    global ball_vel, paddle_one_vel, paddle_two_vel
    #random y multiplier decreases the likelyhood of
    sample = [-0.95, -0.96, -0.97, -0.98, -0.99, -0.1, -1.01, -1.02, -1.03, -1.04, -1.05]
    ball_vel[0] = ball_vel[0] * random.choice(sample) * ball_vel_bounce
    ball_vel[1] = ball_vel[1] * random.choice(sample) * ball_vel_bounce

#helpers and handlers - paddle ball collision
def ball_bounce():
    global ball_vel, paddle_one_vel, paddle_two_vel
    ball_vel[0] = ball_vel[0] * -1 * ball_vel_bounce


#helpers and handlers - new game
def new_game():
    global score_one, score_two, score_total, LEFT, RIGHT
    global paddle_one_pos, paddle_two_pos
    paddle_one_pos = [[0, PAD_CENTER_TOP], [PAD_WIDTH, PAD_CENTER_TOP], [PAD_WIDTH, PAD_CENTER_BOTT], [0, PAD_CENTER_BOTT]]
    paddle_two_pos = [[WIDTH - PAD_WIDTH, PAD_CENTER_TOP], [WIDTH, PAD_CENTER_TOP], [WIDTH, PAD_CENTER_BOTT], [WIDTH - PAD_WIDTH, PAD_CENTER_BOTT]]
    score_one = 0
    score_two = 0
    score_total = 0
    LEFT = False
    RIGHT = True
    spawn_ball()

#helpers and handlers - draw canvas
def draw(canvas):
    global score_one_width, score_two_width
    global ball_pos, ball_vel, ball_vel_bounce
    global paddle_one_pos, paddle_two_pos, paddle_vel_one, paddle_vel_two
    global ball_gutter_upper, ball_gutter_lower, ball_gutter_left, ball_gutter_right

    #win condition and message
    if score_total == 5:
        if score_one > score_two:
            #Left player wins
            canvas.draw_text("Left player wins!", [100, 200], 60, "White")
        else:
            #right player wins
            canvas.draw_text("Right player wins!", [80, 200], 60, "White")
    else:
        #draw court - midline and gutters
        canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
        canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
        canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

        #draw ball - update position
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
        canvas.draw_circle( ball_pos, BALL_RADIUS, 1, "White", "White")

        #draw paddles - update position
        #move a single point, test if in bounds, then use that point as a reference for redrawing the paddle
        #Paddle One
        paddle_one_origin = paddle_one_pos[0][1] + paddle_one_vel[1]
        if paddle_one_origin < 0:
            paddle_one_origin = 0
        elif paddle_one_origin > (HEIGHT - PAD_HEIGHT):
            paddle_one_origin = (HEIGHT - PAD_HEIGHT)
        #then take the value of paddle origin and draw the paddle
        paddle_one_pos = [[0, paddle_one_origin], [PAD_WIDTH, paddle_one_origin], [PAD_WIDTH, (paddle_one_origin + PAD_HEIGHT)], [0, (paddle_one_origin + PAD_HEIGHT)]]
        canvas.draw_polygon(paddle_one_pos, 1, "White", "White")

        #Paddle Two
        paddle_two_origin = paddle_two_pos[0][1] + paddle_two_vel[1]
        if paddle_two_origin < 0:
            paddle_two_origin = 0
        elif paddle_two_origin > (HEIGHT - PAD_HEIGHT):
            paddle_two_origin = (HEIGHT - PAD_HEIGHT)
        #then take the value of paddle origin and draw the paddle
        paddle_two_pos = [[WIDTH - PAD_WIDTH, paddle_two_origin], [WIDTH, paddle_two_origin], [WIDTH, paddle_two_origin + PAD_HEIGHT], [WIDTH- PAD_WIDTH, paddle_two_origin + PAD_HEIGHT]]
        canvas.draw_polygon(paddle_two_pos, 1, "White", "White")

        #paddle, ball, and frame collisions
        #ball is at left gutter
        if ball_pos[0] <= ball_gutter_left:
            #if ball and paddle at bottom corner
            if ball_pos[1] >= ball_gutter_lower and paddle_one_pos[2][1] >= HEIGHT:
                ball_reflect()
            #if ball and paddle at top corner
            elif ball_pos[1] <= ball_gutter_upper and paddle_one_pos[1][1] <= 0:
                ball_reflect()
            #if ball meets paddle
            elif paddle_one_pos[2][1] >= ball_pos[1] and paddle_one_pos[1][1] <= ball_pos[1]:
                ball_bounce()
                #if no paddle
            else:
                score_right()
        #if ball is at the right gutter
        elif ball_pos[0] >= ball_gutter_right:
            #if ball and paddle at bottom corner
            if ball_pos[1] <= ball_gutter_lower and paddle_two_pos[2][1] >= HEIGHT:
                ball_reflect()
            #if ball and paddle at top corner
            elif ball_pos[1] <= ball_gutter_upper and paddle_two_pos[1][1] <= 0:
                ball_reflect()
            #if ball meets paddle
            elif paddle_two_pos[2][1] >= ball_pos[1] and paddle_two_pos[1][1] <= ball_pos[1]:
                ball_bounce()
            #if no paddle
            else:
                score_left()
        #if the ball hits the top or bottom of the frame
        elif ball_pos[1] <= ball_gutter_upper or ball_pos[1] >= ball_gutter_lower:
            ball_vel[1] = ball_vel[1] * -1

        #draw scores - update scores
        canvas.draw_text(str(score_one), [150 - (score_one_width / 2), 100], 80, "White")
        canvas.draw_text(str(score_two), [450 - (score_two_width / 2), 100], 80, "White")


#helpers and handlers - key events, change the velocitites of the paddles
def keydown(key):
    global paddle_one_vel, paddle_two_vel, paddle_vel_mult
    if key == simplegui.KEY_MAP['w']:
        paddle_one_vel[1] = -1 * paddle_vel_mult
    elif key == simplegui.KEY_MAP["up"]:
        paddle_two_vel[1] = -1 * paddle_vel_mult
    elif key == simplegui.KEY_MAP['s']:
        paddle_one_vel[1] = paddle_vel_mult
    elif key == simplegui.KEY_MAP["down"]:
        paddle_two_vel[1] = paddle_vel_mult
    #stuff here change paddle velocity to not 0 (up and w), (down and s)

def keyup(key):
    global paddle_one_vel, paddle_two_vel
    if key == simplegui.KEY_MAP['w'] or  key == simplegui.KEY_MAP['s']:
        paddle_one_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle_two_vel[1] = 0

#create and register
frame = simplegui.create_frame("pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
score_one_width = frame.get_canvas_textwidth(str(score_one), 80, 'serif')
score_two_width = frame.get_canvas_textwidth(str(score_two), 80, 'serif')
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)

#start
new_game()
frame.start()

#Things I have learnt
#globals have to be defined before they are used!
#Process:
    #you can define the frame using variables, why not do this before?
    #create frame and relevant globals
    #create key event handlers
    #create handler functions and define purpose
    #create relevant globals for new functions
    #declare globals for vars used in functions
    #nomenclature item_var_detail e.g. paddle_one_pos paddle_one_vel, the last one should change!
    #everything has a gutter as you are doing the math on a point and then drawing a shape based on that point, could have a lower paddle gutter - height - pad_width

#Key improvements that I have made and were more subtle than I first thought
    #get paddles moving to exactly the edge of the screen
    #get the corner bounces happening correctly
    #get a good random function for the spawned ball so it has a mostly horizontal velocity but still random in the y component
    #add a random element to the ball reflections to break out of bounce loops
    #drawing the paddles by controling the origin point, like the way you draw the circle from the center
    #controlling the incidences (bounces and reflections etc) case by case, most specific to the least in a big elif
    #reflect bounce and score functions really neaten up the code
    #if statements are not in chronological order, often reverse or least likely first e.g. game over screen before the code for the game

#Error checking
    #check nomenclature
    #check for grammar errors e.g. ' ] and : missing or in the wrong place
    #make sure (un)commented the various bits of code and handlers
    #add heights to heights and widths to widths
    #make sure you have the right data type float vs int
    #make sure you have the right comparators < > = etc

#Cool ideas
    #Get ball speed to increase per hit, user set speed increase
    #change ball colour (black would really mess with you) per hit
    #First to x, or x's point ahead wins; tennis scoring?
    #shrinking ball on bounce or point score!
    #buttons to turn on and off all the various options
    #create a function wrap that wraps a value to the screen - nicer for bigger projects
    #make paddles grow/shrink on point score
    #make paddles or ball change colour on score
    #make paddles move in on score
    #single and up to four player options
    #unpredicatble bounce functions
    #velocity of paddle to add to ball velocity, if gave paddles acceleration this would be quite fun
    #tennis or table tennis rules for scoring and win conditions
    #multiple balls, a growing ball splits when gets to big
    # collect bonuses that appear on screen
