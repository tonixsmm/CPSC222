#This is a one line comment
"""
a block/multilines comment (triple quotes)
"""

import math
import random

#VARIABLES
x = "hello"
month = "September"
print(x)
print(type(x)) #what type of value stored in x is
#string type in Python is denoted as str

#OPERATORS
#mathematic op rules are the same in Python
print(4*5)
# "/" is a floating point division (normal devision)
# "//" is an integer division (5 // 2 = 2) - like the mod function in c++
# "%" is a modulus op, the remainder of a division (5 & 2 = 1)
#"**" is exponentiate op

print(3%5)

#we can also do exponentiation with the pow() function
#we need to import the math module
#a module is a python file
#if we use math.pow() it will return the float function
print(type(pow(2,2)))
print(type(math.pow(2,2)))
"""""
#GETTING INFO FOR USERS
print("Enter your favorite number")
fav_num = input()
print(type(fav_num))
#we often need to convert between types
fav_num_int = int(fav_num)
print("Your favorite number doubled is:", 2 * fav_num_int)
"""""
#DECIMAL FORMATTING
#there is a lot of ways to do this
print(math.pi)
print("%.2f" % (math.pi))
print("{:.2f}".format(math.pi))
print(f"{math.pi:.2f}")
print(round(math.pi, 2))

#CONDITIONALS
#if some condition is true, then execute some code
x = 5
if x == 5:
    print("Hello") #there should be 4 spaces before print. VSCode would probably do it for you. Use "Tab"
#we also have an else keyworld
#execute when the preceding if is false
if x == 5:
    print("x is 5")
else:
    print("x is not 5")
#we also have elif - short for else if
#if you want to test a bunch of condition
x = -2
if x < 0:
    print("x is neg")
elif x > 0:
    print("x is positive")
else:
    print("x is 0")
#you can nest your code
#be aware of indentation

#LOOPS
#use it when you want to repeat codes

#for loop
#for item in sequence:
#   (indented)
#   do something
for item in [3, 5, 7, "hello"]:
    print(item)
for letter in "slalom":
    print(letter)
#we can make our own sequences using range()
#range(stop) means [0, stop)
for i in range(9):
    print(i, end=" ")
print()
#or range(start, stop) means [start, stop)
for i in range(4, 9):
    print(i, end=" ")
print()
# or range(start, stop, step) means [start, stop) up by step
for i in range(4, 9, 2):
    print(i, end=" ~ ")
print()

for i in range(8, 2, -2):
    print(i, end=" ")
print()

for i in range(2, 42, 2):
    print(i, end=" ")
print(i + 2)

# ADVANCED LOOPS
#we can also nest loops
#we can get an early exit from a loop with the break keyworld

# WHILE LOOPS
# while some conditions is true:
#   body of loop (indented)
''''
while True:
    user_input = input("Enter a word (stop to exit): ")
    if user_input == "stop":
        break
'''

i = 0
while i < 39:
    print(i + 2, end=" ")
    i += 2
print()

# FUNCTIONS
# a named sequence of statements
# function accepts input (argument when you call the function)
# parameter when you define the function
# def fucntion_name(parameter list):
#   body of function (indented)
def say_hello():
    print("Hello")
for i in range(10):
    say_hello()

def say(message):
    print("Message:", message)
say("hello")
# "hello" is the argument
# message is the parameter

def circle_area(radius):
    print("The area is:", round(radius ** 2 * math.pi, 2))
circle_area(3)

def compute_circle_area(radius):
    area = round(radius ** 2 * math.pi, 2)
    return area #send the value back to area
circle_area(3)

def num_check(list1, list2):
    same_first = False
    same_last = False
    #assume false until proven otherwise
    if len(list1) > 0 and len(list2):
        if list1[1] == list2[1]:
            same_first = True
        if list1[-1] == list2[-1]:
            same_last = True
    return same_first, same_last

result1, result2 = num_check([], [])
print(result1, result2)

#Why use function? reusability and code organization

#Random Numbers
#we may need random number to initialize random events or the state of an algorithm

#if you want the same random number each time you run your program, "seed" the random number generator
random.seed(0)

#let's role a 6-faced fice
#import the random model
roll = random.randrange(1, 7)
roll1 = random.randint(1,6)
print("roll:", roll)
print("roll:", roll1)