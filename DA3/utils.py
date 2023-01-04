'''
Tony Nguyen
CPSC 222 01
Data Assignment #3
10/13/2022
I attempted the bonus
Description: This file contains functions and implementations as required by DA3
'''

import pandas as pd

def read_data(filename):
    # This function reads data from a .csv file
    # Parameter: filename - the relative path of the file in the DA3 folder
    # Return: a DataFrame that contains the data from the .csv file

    data = pd.read_csv(filename, index_col=0, header=0)
    return data
    
def slice_column(data):
    # This function prompt the user to enter the date range and attribute name that they want to survey, and slice the data out of the original dataset
    # Parameter: data - a DataFrame of data
    # Return: desried_column - a series of desired_column_name and the value sliced, desired_column_name - the attribute name that the user wants to survey

    print("The data lasted from", data.index[0], "to", data.index[-1])
    date_start = input("Please enter the start date (inclusive) (MM/DD/YY - Please omit any 0 in Month and Date): ")
    date_end = input("Please enter the end date (inclusive) (MM/DD/YY - Please omit any 0 in Month and Date): ")

    # Displaying a dictionary of column names for user to choose
    count = 0
    col_list = {}
    print("Names of column:")
    for i in data.columns:
        col_list[count] = i
        count += 1
    print(col_list)
    desired_column_num = input("Please enter the number corresponding to your desired column: ")

    # Slice the column to the desired one
    desired_column_name = col_list[int(desired_column_num)]
    desired_column = pd.Series(dtype=str)
    desired_column[desired_column_name] = data.loc[date_start:date_end, desired_column_name]
    return desired_column, desired_column_name

def stat_computation(data):
    # This function computes statistical values
    # Parameter: data - a DataFrame of data
    # Return: void

    stat_index = ["Sum", "Mean", "StdDev", "Median", "Smallest", "Largest"]
    stat_result = []

    stat_result.append(data.sum())
    stat_result.append(data.mean())
    stat_result.append(data.std())
    stat_result.append(data.median())
    stat_result.append(data.min())
    stat_result.append(data.max())

    stat_result_series = pd.Series(stat_result, index=stat_index)
    stat_result_series.to_csv("stat_result.csv", header=False)

def join_data(data1, data2):
    # This function joins two datasets together
    # Parameter: two DataFrames of data
    # Return: a DataFrame of joined data

    merged_df = data1.merge(data2, on="Date")
    merged_df.to_csv("merged.csv")
    return merged_df

def split_apply(data, selected_column_name):
    # This function splits data into groups of "Day of Week" using Pandas groupby() and calculates the average value of user's input column
    # Parameter: data - a DataFrame of data, selected_column_name - the attribute name we want to split
    # Return: return a Series of key-pair value contains the Day of Week and their corresponding average value
    
    # Split step
    group_by_date = data.groupby("Day of Week")

    # Apply step
    group_mean_apply = pd.Series(dtype=float)
    for group_date, group_df in group_by_date:
        group_series = group_df[selected_column_name]
        group_mean = group_series.mean()
        group_mean_apply[group_date] = group_mean
    return group_mean_apply

def combine(series):
    # This function combines the value from split-apply step
    # Parameter: a Series
    # Return: a series of split-apply-combine in Day of Week order

    # Combine step
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    group_mean_combine = pd.Series(dtype=float)
    for i in range(len(day_list)):
        group_mean_combine[day_list[i]] = series[day_list[i]]
    return group_mean_combine

def split_apply_combine(data, selected_column_name):
    # This function performs split-apply-combine
    # Parameter: data - a DataFrame of data, selected_column_name - the attribute name we want to split
    # Return: void

    # Split-Apply step
    # group_by_date = split_apply(data, selected_column_name)
    group_by_date = groupby_apply_manual(data, selected_column_name) # Using the manual "groupby" function
    
    # Combine step
    group_mean_print = combine(group_by_date)
    print(group_mean_print)

def groupby_manual(data):
    # This function implements Pandas groupby() manually
    # Parameter: data - a DataFrame of data, split_column_name - the attribute name we want to split
    # Return: a dictionary contains key-value pairs of attribute's names and their corresponding DataFrame

    manual_col_list = data[:]["Day of Week"]
    group_dictionary = {}
    element_df = pd.DataFrame(dtype=str, columns=data.columns)

    # Create a dictionary of attribute's name and empty DataFrame
    for i in range(len(manual_col_list)):
        if not(manual_col_list.iloc[i] in group_dictionary):
            group_dictionary[manual_col_list.iloc[i]] = element_df

    # Concetanate data into the dictionary
    for j in range(len(manual_col_list)):
        for k in group_dictionary:
            if manual_col_list.iloc[j] == k:
                if len(group_dictionary[k]) == 0:
                    group_dictionary[k] = pd.DataFrame(data.iloc[j, :]).T
                else:
                    group_dictionary[k] = pd.concat([group_dictionary[k], data.iloc[j, :].to_frame().T], ignore_index=False)
                    # I have to change ignore_index=False to return a DataFrame that uses "Date" as index
                    # Thank you for helping me with this part!
    return group_dictionary

def groupby_apply_manual(data, split_column_name):
    # This function splits using groupby_manual() and apply the average calculation to the user's input data
    # Parameter: data - a DataFrame of data, selected_column_name - the attribute name we want to split
    # Return: return a Series of key-pair value contains the Day of Week and their corresponding average value

    dict = groupby_manual(data)
    group_mean_apply = pd.Series(dtype=float)
    for day in dict:
        apply_col = dict[day].loc[:, split_column_name]
        group_mean_apply[day] = apply_col.mean()
    return group_mean_apply

# ANSWER TO BONUS QUESTION:
# Gina's viewing history tends to be higher on the beginning of the week and reduces by the end of the week. Her highest 
# viewing day is Tuesday, while her lowest viewing day is on Saturday. For other attributes, though there are some 
# slight fluctuation, the pattern appears to be consistent throughout the rest of attribute lists surveyed.