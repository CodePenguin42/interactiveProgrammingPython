#python learning 1
#week 0
#optional exercises
#http://www.codeskulptor.org/#user44_Y86ewltRD3_0.py

#1) convert 13 miles to feet, 5280 foot/miles
print 13*5280
#and now with some variables
distance_in_miles = 13
foot_per_mile = 5280
print distance_in_miles*foot_per_mile

#2) How many seconds in 7h 21min 37s
print (7*60*60) + (21*60) + 37
#and now with some variables
hours_to_seconds = 3600
minutes_to_seconds = 60
hours = 7
minutes = 21
seconds = 37
print (hours_to_seconds*hours)+(minutes_to_seconds*minutes)+seconds

#3) Perimeter 2w+2h where w=4 and h=7
print 2*(4+7)
#and now for something completley different
width = 4
height = 7
print 2*(width+height)

#4) Area wh where w=4 and h=7
print 4*7
#and now for something completley different
print width*height

#5) Circumference 2pir where r=8, take pi=3.14
print 2*3.14*8
#and now for something completley different
pi = 3.14
radius = 8
print 2*pi*radius

#6) Area pir^2 where r=8, take pi=3.14
print 3.14*(8**2)
#and now for something completley different
print pi*(radius**2)

#7) Interest at 7% cumulative on $1,000 over 10 years
print 1000*(1+(0.01*7))**10
#and now for something completley different
initial_investment = 1000
percentage_interest = 7
years_invested = 10
print initial_investment*(1+(0.01*percentage_interest))**years_invested

#8) Practice concatination of strings
print "My name is " + "Joe" + " " + "Warren"
#and now for something completley different
name_first = "Joe"
name_second = "Warren"
print "My name is " +name_first + " " +name_second

#9) Practice concatination of strings with interger
print "Joe Warren is " + str(52) + " years old."
#and now for something completley different
age = 52
print name_first + " " + name_second + " is " + str(age) + " years old."

#10) Distance between two points formulae is incorrect but functional
print ((5-2)**2+(6-2)**2)**0.5
#and now for something completley different
x0 = 2
x1 = 5
y0 = 2
y1 = 6
print ((x1-x0)**2+(y1-y0)**2)**0.5

#python learning 1
#week 0
#mini project
#http://www.codeskulptor.org/#user44_kQiTgLYouC_0.py


# program template for mini-project 0

# Modify the print statement according to
# the mini-project instructions

print "We want... a shrubbery!"
