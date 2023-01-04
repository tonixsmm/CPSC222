'''
Programmer: Tony Nguyen
Class: CPSC 222, Fall 2022
Data Assignment #2
9/29/2022
I attempted the bonus
Description: This file contains functions and their implementations as required by DA2
'''

import math

def clean_file(set):
    # This function removes any excessive blank space out of the data value
    # Parameter: a list of data to be "cleaned"
    # Return: void

    for i in range(len(set)):
        set[i] = set[i].strip()

def data_restructure(set):
    # This function removes commas after each data value
    # Parameter: a list of data values that needs to have commas removed
    # Return: a list that contains the value of data only without comma

    table = []
    for value in set:
        values = value.split(",")
        table.append(values)
    return table

def convert_to_float_1D(set):
    # This function converts values in a given list to float type
    # Parameter: a list of data to be converted
    # Return: void

    for i in range(len(set)):
            set[i] = float(set[i])

def read_data(filename):
    # This function reads in the originial file, processes the header and data parts, and loads them into their corresponding lists
    # Parameter: the file input
    # Return: two lists contain the header part and the data part

    infile = open(filename, "r")
    original_data = infile.readlines()
    clean_file(original_data)

    # Process the header
    original_headers = []
    original_headers = original_data.pop(0)
    headers = original_headers.split(",")

    # Process the data
    data = data_restructure(original_data)

    infile.close()
    return headers, data

def display_table(headers, data):
    # This function displays the given header and data input in a grid-like format
    # Parameter: two lists contain the header and the data seperately (both are 1D lists)
    # Return: void

    data.insert(0, headers)
    for i in range(len(data)):
        for j in range(len(data[0])):
            print(data[i][j], end = "\t")
        print()

def display_table_1D(headers, data):
    # This function displays the given header and data input in a grid-like format
    # Parameter: two lists contain the header and the data seperately (the data list is 2D)
    # Return: void

    data.insert(0, headers)
    for i in range(len(data)):
        print(data[i], end = "\t")
    print()

def get_column(headers, col_name, data):
    # This function seperates a given column of a dataset and loads them into a 1D list
    # Parameter: headers - the original header list, col_name - string type, the name of the column we want to seperate, data - the original data list
    # Return: a list that contains only a column's value (without the header)
    
    # Find the order of the wanted column name in the dataset
    count = 0
    for i in range(len(headers)):
        if col_name != headers[i]:
            count += 1
        else:
            break
    
    # Load the column's value into a new list
    table = []
    for i in range(len(data)):
        table.append(data[i][count])

    # Remove the header out of the data set
    table.pop(0)
    
    return table

def stat_computation(table):
    # This function seperates a given column of a dataset and loads them into a 1D list
    # Parameter: headers - the original header list, col_name - string type, the name of the column we want to seperate, data - the original data list
    # Return: a list that contains only a column's value (without the header)

    count = len(table)
    mean = sum(table)/len(table)

    # Calculate the Standard Deviation
    sd_num = 0.0
    sd_variance = 0.0
    for i in range(count):
        sd_num += pow((table[i] - mean), 2)
    sd_variance = sd_num * (1/count)
    standard_deviation = math.sqrt(sd_variance)

    # Find the median value
    table_sorted = table[:]
    table_sorted.sort()
    if count % 2 == 0:
        median = (table_sorted[int(count/2)] + table_sorted[int(count/2 - 1)]) / 2
    else:
        median = table_sorted[int((count - 1) / 2)]

    print("Count of the numbers:", count)
    print("Average (mean) of the numbers:", round(mean, 2))
    print("Standard deviation of the numbers:", round(standard_deviation, 2))
    print("Median number:", round(median, 2))
    print("Smallest number:", table_sorted[0])
    print("Largest number", table_sorted[-1])

def slice_column(date_col, col, start_date, end_date):
    # This function finds the corresponding data values to their given dates, and load the selected date period as well as its data into two lists
    # Parameter: date_col - a list of dates only, col - a list of selected data attribute (select prior to calling the function), start_date - the beginning date INCLUSIVE, end_date - the ending date EXCLUSIVE
    # Return: two lists of selected dates and their corresponding values

    # Find the selected dates in the date list
    count = 0
    count_start = 0
    count_end = 0 
    for i in range(len(date_col)): # run thru the length of the list
        if start_date != date_col[i]:
            count_start += 1
        else:
            break
    for j in range(len(date_col)): # run thru the length of the list
        if end_date != date_col[j]:
            count_end += 1
        else:
            break
    
    # Calculate the number of rows that contains matching criterias
    count = abs(count_end - count_start)

    # Load the data found into two new lists
    return_date = []
    return_col = []
    for k in range(count):
        return_date.append(date_col[count_start + k])
        return_col.append(col[count_start + k])

    return return_date, return_col
### ANSWER TO THE BONUS QUESTION
# 1. Since Gina finished her marathon run on 7/24/21, her pattern doesn't change that much. 
# However, her run distance got generally less than it was before
# 2. When Fall 21 semester commenced, Gina still maintained her daily workout schedule like what
# she has been doing since March. However, it was noticable that her workload was less than she used to do,
# especially during her marathon training
