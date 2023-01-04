from audioop import add
import random

table = []
#table = [[for j in range(5)] for i in range(10)]

for i in range(10):
    row = []
    for j in range(5):
        rand_num = random.randrange(1, 11)
        row.append(rand_num)
    table.append(row)
print(table)

def printTable(table):
    for i in range(10):
        for j in range(5):
            print(table[i][j], end = "\t")
        print()

num_min = table[0][0]
for i in range(10):
    for j in range(5):
        if table[i][j] < num_min:
            num_min = table[i][j]
print("Min number is", num_min)

num_max = table[0][0]
for i in range(10):
    for j in range(5):
        if table[i][j] > num_max:
            num_max = table[i][j]
print("Max number is", num_max)

'''
specific_num = input("Enter your number: ")
count = 0
for i in range(10):
    for j in range(5):
        if table[i][j] == int(specific_num):
            count += 1
print("The number of time:", count)

rev_num = int(input("Enter the number you want to remove: "))
removed = False
for row in range(10):
    while rev_num in range(5):
        row.remove(rev_num)
        removed = True
if not removed:
    print("Sorry, your number is not here")
printTable(table)
'''

#LIST ALIASING
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1 #not a copy of value but rather copy of list1's location. This is called aliasing
print(list1, list2, list3)
list3[0] = 200
print(list1, list2, list3)

def add_one_to_each_element(some_list):
    #some_list is an alias to same list list3 is referring to
    for i in range(len(some_list)):
        some_list[i] += 1

add_one_to_each_element(list3)
print(list1, list2, list3)
#python is "pass by object reference"
#if you pass a list to a fucntion, code in that function can modify the list in memory

#MORE ON STRINGS
word = "Gonzaga"
#like list, is also 0-based indexing
print(word[0], word[-1], word[2:4])
#strings cannot be changed
word = "G" + word[1:]
print(word)
#string concatenation +
#string repitition
print(word * 5)
#string comparison < > <= >= == !=
print("bird" < "cat") #string is compared character by characters according to ASCII

#string methods
#join() and split()
#strip()
word = "    \n \t\t     Hello       \n\n\t"
print(repr(word))
word = word.strip()
print(repr(word))
#find()
print(word.find("zz"))
