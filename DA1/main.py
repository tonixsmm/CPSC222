'''
Programmer: Tony Nguyen
Class: CPSC 222, Fall 2022
Data Assignment #1
9/12/2022
I attempted the bonus

Description: This program exercises various tasks as required by the DA1
'''

import math

### TASK 1
point_per_game = [2.4, 0.9, 14.1, 0.1, 11.8, 18.4, 7.3, 11.2, 4.3, 0.7, 1.8, 1.0, 11.8, 5.1]
print(point_per_game)
copy_of_points = point_per_game[:]
point_per_game.sort()
point_per_game.reverse()
# the final result
print(point_per_game)

### TASK 2
print("Count of the numbers:", len(point_per_game))
print("Average (mean) of the numbers:", round(sum(point_per_game)/len(point_per_game), 2))
print("Median number:", round((point_per_game[int(len(point_per_game)/2)] + point_per_game[int(len(point_per_game)/2 - 1)]) / 2, 2))
print("Smallest number:", point_per_game[-1])
print("Largest number:", point_per_game[0])

### TASK 3
desired_index = input("Please enter the desired index (0-13): ")
new_value = input("Please enter the new value: ")
point_per_game[int(desired_index)] = int(new_value)
print("The modified list:", point_per_game)

### BONUS TASK
manual_arrangement = []
i = 13
while i >= 0:
    manual_arrangement.append(copy_of_points[i])
    i -= 1
print(*manual_arrangement, sep=' ~ ')