# a sequence of item
# 1D list is like a single row in excel

list_ins = [0, 1, 10, 20]
#           0  1   2   3
#           -4 -3 -2  -1
# could be either one
print(list_ins[0])
print(list_ins[-4])

# unlike C++'s array, list can be mixed with types

list_number = [0, 1, -2, -3]
print(type(list_number))
list_number[0] = "Hello"
print(list_number)

# use len() to find out how many elements are in a list
print(len(list_number))
list_number.append("another element")
# suppose you don't know how many elements they are in the list, you can always print out the last one
print(list_number[len(list_number) - 1])

# we can declare an empty list
empty_list = []

# we can have a list of list or multidimensonal list (similar to 2D array in C++)
nested_list = [[0, 1], [2], [3], [4, 5], []]
print(len(nested_list))

# looping thru list items
candies = ["twix", "reeses", "oreo", "snickers"]

for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)):
    print(i, candies[i])

# common list ops
# list connection - connect 2 lists together
print(candies)
candies += ["m&m", "starburst"]
print(candies)
# list repitition - repeating elements in a list
bag_of_candies = 5 * ["twix", "snicker"]
print(bag_of_candies)
# list slicing
print(candies[1:3]) # ":" is the slice operator. start index is inclusive and end index is exclusive
# if you ever need a copy of a list, you can use ":" w/o the start or end indexes
copy_of_candies = candies[:]
copy_of_candies [0] = "TWIX"
print(candies)
print(copy_of_candies)

# list method
cars = ["corolla", "lamborghini"]
cars.append("bmw")
cars.extend(["sentra", "mercedes"])
print(cars)
#use operators
cars += ["civic", "acura"]
print(cars)
#remove
cars.remove("civic")
print(cars)
#pop()
cars.pop(-1)
print(cars)
#create a string from a list of strings
word_list = ["c", "or", "r", "o", "lla"]
word_str = " ".join(word_list)
print(word_str)
#create a list from a string
word_list2 = list(word_str)
print(word_list2)
comma_seperated_value_str = "c,or,ro,ll,a"
word_list3 = comma_seperated_value_str.split(",")
print(word_list3)