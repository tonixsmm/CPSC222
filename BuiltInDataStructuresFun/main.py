#three common used "built-in" data structures
#1. List
#2. tuple
#3. dictionary

#List
#it is a sequence of item
#0-based for indexing
#lists can be changed
#lists have an order to their items
nums = [3, 6, -1, 7, 9, 7]
print(nums)
print(nums[-len(nums)], nums[0:2]) 

#lits can be changed
nums.append(100)
nums.remove(7)
print(nums)

#1D-list is like a line
#2D-list is like a grid
#3D-list is like a  cube
#4D-ND...

#2D list
# here are two main ways to think about it
#1. Like a table (rows and columns)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][0])
print(matrix[1][2])

#2. a 1D list where each item is a 1D list (nested lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))
print(type(matrix[0][0]))

#3D lists
cube = [[[0, 0,], [1, 1]],[[2, 2], [3, 3]]]

#Tuples
#a tuple is a list that cannot be changed
tuples = "x", "y", "z"
print(tuples)
print(type(tuples))

#when declaring a single item typle, we need a comma after it
single_tuple = (1,)
print(single_tuple)
#we can create an empty tuple
#tuple indexing and slicing is the same as lists
#tuples are used for returning multiple values

#Dictionaries
#dictionary is a list with keys and indexes and values mapped from those keys
#a key values pair
#use a key to look up a value
#keys in dictionary must be unique
#example of a key: studentID
#example of a student name
# loop up ID 12345 -> "Jane Doe"
my_dict = {} #empty dictionary
print(my_dict)
my_empty_dict = dict()
my_dict["12345"] = "Jane Doe"
print(my_dict)

state_capital ={"Washington": "Olympia", "Idaho": "Bosie", "Oregon": "Portland"}
print(state_capital)
state_capital["Washington"] = "Spokane"
print(state_capital)
state_capital["California"] = "Sacremento"
#the key value pair in the dictionary are not ordered

#initialize a dictionary using a list of tuples
roman_numerals = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50)])
print(roman_numerals)
roman_numerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

#types can be used for keys: integers, strings, files, tuples, etc.)
#list cannot be as keys
#types of value: any types

#len()
print(len(state_capital))
#check for the existence of keys
print("Washington" in state_capital)
print("Olympia" in state_capital.values())
#loop thru the key value pairs in a dictionary
for state in state_capital:
    print(state, state_capital[state])
for state, capital in state_capital.items():
    print(state, capital)

myname = "Edgar Allan Poe"  
namelist = myname.split()  
init = ""  
for aname in namelist:      
    init = init + aname[0]  
print(init)
