#python learning 1
#week 1
#optional mini project - a magic eightball, now on console




#import function
import simplegui
import random

#convert number to fortune, will be used in later function
def number_to_fortune(number):
    """ambitiously using a dictionary as a switch statement"""
    #switcher is the dictionary
    switcher = {
        0 : 'Yes, for sure!',
        1 : 'Probably yes.',
        2 : 'Seems like yes...',
        3 : 'Definitely not!',
        4 : 'Probably not.',
        5 : 'I really doubt it...',
        6 : 'Not sure, check back later!',
        7 : 'I really cant tell.'
    }
    return switcher.get(number, "Problem with input")

def mystical_octosphere(question):
    """and now for linking the question to the answer"""
    print "Your dumb ass ass-in-ass question was..." + question
    print "You gently fondle the magic eight ball"

    #generate the answer fortune
    answer_number = random.randrange(0,8)
    answer_fortune = number_to_fortune(answer_number)

    #more wordy bits
    print "As your fingers become entangled in the curly husk, the reply explodes into view"
    print "The mythical octoball says..." + answer_fortune
    print

#create frame and register buttons


#A few testing questions
mystical_octosphere("will I get laid tonight")
mystical_octosphere("should I kick stuarts ass")
mystical_octosphere("ice cream?")
mystical_octosphere("hammer time?")




#Mini project Rock Paper Scissors Lizard Spock RPSLS
    #build a rock paper scissors player and judge
    #inputs: two choices (player, random) - become numbers
    #outputs: who is the victor - in some pretty print statement
    #functions helper - convert number to choice, primary - deciding the victor
    #invers dictionary lookup might be a little more complex but good for a second iteration

#helper functions:
def name_to_number(name):
    """dictionary lookup to convert name(key) into number(value)"""
    return {
    "rock" : 0,
    "Spock" : 1,
    "paper" : 2,
    "lizard" : 3,
    "scissors" : 4
    }.get(name, "Invalid choice")

def number_to_name(number):
    """dictionary lookup to convert number(key) into name(value)"""
    return {
    0 : "rock",
    1 : "Spock",
    2 : "paper",
    3 : "lizard",
    4 : "scissors"
    }.get(number, "Number out of range")


#Main function
def rpsls(player_choice):
    """main function taking player choice, making random choice, and deciding the victor"""

    #confirm player choice and generate number
    print "The player has chosen " + player_choice + " no take-backsies!"
    player_number = name_to_number(player_choice)

    #make random computer choice
    computer_number = random.randrange(0,5)
    computer_choice = number_to_name(computer_number)
    print "The computer has chosen " + computer_choice

    #calculating the winner
    value = (player_number - computer_number) % 5

    #declaring the winner
    if value == 1 or value == 2:
        print "The player wins"
    elif value == 3 or value == 4:
        print "The computer wins"
    elif value == 0:
        print "We have a draw"
    else:
        print "time to do some debugging"

    #print blank line to separate games
    print

#some test functions
# rpsls("Spock")
# rpsls("scissors")
# rpsls("paper")
# rpsls("rock")
# rpsls("lizard")
# rpsls("Spock")
# rpsls("Spock")
# rpsls("Spock")
