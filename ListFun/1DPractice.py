import random

num_list = []

for i in range(20):
    generate = random.randrange(1, 11)
    num_list.append(generate)

print(*num_list, sep=" ")
num_list.sort()
print(num_list[0])
print(num_list[-1])

number = input("what number do you want? ")
count = 0

for i in range(len(num_list)):
    if number == int(num_list[i]):
        count += 1
print("The number is specified for:", count, "time(s)")

#find the smallest or largest number of the list
