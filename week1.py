#python learning 1
#week 1
#optional exercises 1a Functions

#modules imported
import math
import random

#1) convert miles to feet
def miles_to_feet(miles):
    return feet = miles*5280
#test
print miles_to_feet(10)

#2) calculate total seconds
def total_seconds(hours, minutes, seconds):
    return hours*60*60 + minutes*60 + seconds
#test
print total_seconds(1,1,1)

#3) calculate rectangle perimeter
def rectangle_perimeter(width, height):
    return 2*(width+height)
#test
print rectangle_perimeter(2,2)

#4) calculate rectangle area
def rectangle_area(width, height):
    return width*height
#test
print rectangle_area(2,2

#5) calculate circle circumference
def circle_circumference(radius):
    return 2*math.pi*radius
#test
print circle_circumference(0.5)

#6) calculate circle area
def circle_area(radius):
    return math.pi*(radius**2)
#test
print circle_area(1)

#7) calculate investment value
def future_val(present_val, annual_rate, years):
    return present_val*(1+(0.01*annual_rate))**years
#test
print future_val(1000,1,10)

#8) name tag string generator
def name_tag(first_name, last_name):
    print ("My name is %s %s." % (first_name, last_name))
#test
name_tag("Alice", "Parry")

#9) name and age tag string generator
def name_and_age(name, age):
    print ("%s is %d years old." % (name, age))
#test
name_and_age("Alice", 27)

#10) distance between two points
def point_distance(x0, y0, x1, y1):
    return ((x1-x0)**2+(y1-y0)**2)**0.5
#test
print point_distance(0,0,3,4)

#challenges....ooooo
#11) calculate area of any triangle using Heron's formula
def triangle_area(x0, y0, x1, y1, x2, y2):
    side_one = point_distance(x0, y0, x1, y1)
    side_two = point_distance(x0, y0, x2, y2)
    side_three = point_distance(x1, y1, x2, y2)
    semi_perim = 0.5*(side_one + side_two + side_three)
    return (semi_perim*(semi_perim - side_one)*(semi_perim - side_two)*(semi_perim - side_three))**0.5
    #I have an odd feeling that I should be able to generate both the variable names and numbers using a loop of some kind.
#test
print triangle_area(0, 0, 3, 0, 3, 4)

#12) printing the digits of a given number from 0-100
def print_digits(number):
    if (number > 100 or number < 0):
        print "Your number is out of range! Please choose a number from 0 to 100"
    else:
        tens_digit = number // 10
        ones_digit = number % 10
        print ("The tens digit is %d, and the ones digit is %d." %(tens_digit, ones_digit))
#test
print_digits(200)
print_digits(45)

#13) Powerball game allowing duplicates
def powerball():
    #generate an array of 5 random numbers range 1-60.
    random_array = []
    for i in range (5):
        random_array.append(random.randrange(1,61,1))
    #print random_array
    #generate a random number range 1-36.
    random_number = random.randrange(1,37,1)
    #print random_number
    print ("Today's numbers are %d, %d, %d, %d, and %d. The Powerball number is %d." % (random_array[0], random_array[1], random_array[2], random_array[3], random_array[4], random_number))
powerball()

#13) and now with no duplicates
def powerball_two():
    #generate an array of 5 random numbers range 1-60.
    random_array = random.sample(range(61),5)
    #this looks syntactically correct but does not work in codesculptor
    #print random_array
    #generate a random number range 1-36.
    random_number = random.randrange(1,37,1)
    #print random_number
    print ("Today's numbers are %d, %d, %d, %d, and %d. The Powerball number is %d." % (random_array[0], random_array[1], random_array[2], random_array[3], random_array[4], random_number))
powerball_two()



#Optional exercises 1b Logic and Conditionals

#1) even tester function
def is_even(number):
    """tests the parity of a number, return true of even"""
    return (number % 2) == 0

#test of the is_even function
is_even(0)
is_even(-2)
is_even(10)
is_even(11)

#2) testing the coolness of lame people
def is_cool(name):
    """name matching function"""
    return (name == "Joe") or (name == "John") or (name == "Stephen")

#test of the is cool function
is_cool("Joe")
is_cool("John")
is_cool("Stephen")
is_cool("Alice")

#3) testing to see if it is lunchtime
def is_lunchtime(hour, is_am):
    """matching hour and am pm too arbitary lunchtime parameters"""
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

#test for lunctime function
is_lunchtime(11,false)
is_lunchtime(11,true)
is_lunchtime(12,true)
is_lunchtime(12,false)
is_lunchtime(1,true)
is_lunchtime(13, false)

#4) testing for a leap year using Gregorian calendar

def is_leap_year(year):
    """test to see if a year is a leap year"""
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 40 ))

#5) test if intervals intersect
def interval_intersect(a,b,c,d):
    """testing the overlap of intervals given that a<=b and c<=d"""
    return (c <= b) or (a <= d)

#6) string interpolation for name and age
def name_and_age(name, age):
    """function for printng name and age with some validation"""
    if age > 0:
        print ("%s id %d years old." %(name, age))
    else:
        print "Error: Invalid age"

#test of name age function
name_and_age(Alice, -20)
name_and_age(Alice 0)
name_and_age(Steve, 20)

#7) printing digits of numbers 1-99, excluding 0 and 100
def print_digits(number):
        """printing digits of a two digit positive number, with some error validation"""
    if (number > 100 or number < 0):
        print "Error: Input is not a two-digit number."
    else:
        tens_digit = number // 10
        ones_digit = number % 10
        print ("The tens digit is %d, and the ones digit is %d." %(tens_digit, ones_digit))

#test of function
print_digits(0)
print_digits(-20)
print_digits(350)
print_digits(54)

#8) name lookup, adding family name to first name
def name_lookup(first_name):
    """return full name from first name, error validation on first name"""
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"

#test of the function
print name_lookup("Joe")
print name_lookup("Alice")
print name_lookup("Stephen")

#9) Pig latin generator, can make this way more complex if you want!
def pig_latin(word):
    """makes words into pig latin"""
    if (word[0] = "a") or (word[0] = "e") or (word[0] = "i") or (word[0] = "o") or (word[0] = "u"):
        return word + "ay"
    else:
        return word[1 : ] + word[0] + "ay"
#create vowel iterator function that runs inside the if and returns true of the letter word[n] is a vowel
#regex to do cluster recognition of vowel and consonant groups

#test of the function
print pig_latin("pig")
print pig_latin("cat")
print pig_latin("owl")

#10) Challenge, interpretation and use of the quadratic formula
def smaller_root(a, b, c):
    """calculating the smaller root if the equation has one"""
    determinant = b**2 - 4*a*c
    if determinant < 0 or a == 0:
        return "Error: No real solution"
    else:
        """finding the negative roots"""
        determinant_sqrt = determinant ** 0.5
        if a > 0:
            negative_root = (-b - determinant_sqrt) / (2*a)
            return negative_root
        else:
            negative_root = (-b + determinant_sqrt) / (2*a)
            return negative_root

#do not assume that all functions given are quadratic, a could be 0 hence linear
#assume that smaller means negative
#the numerator and denominator need to be in their own brackets or it just doesn't work
#really you have to put the return on a separate line, I think code sculptor is running old python

#a few test cases
print smaller_root(1,2,3)
print smaller_root(2,0,-10)
print smaller_root(6,-3,5)
