'''
Programmer: Tony Nguyen
Class: CPSC 222, Fall 2022
Data Assignment #2
9/29/2022
I attempted the bonus
Description: This file is used to test the universialness of utils.py functions with Netflix Viewing History
'''

import utils

def main():
    # This function exercises the codings in utils.py
    # Parameter: void
    # Return: void

    # Read data from file
    headers, data = utils.read_data("netflix_data.csv")
    utils.display_table(headers, data)
    
    # Prompt the user to select date range
    input_col = input("Enter the name of the column you want to survey data: ") # This one may be redundent since there are only two atrributes in netflix_data.csv
    input_date_start = input("Enter the start date that you want to survey (m/dd/yy): ")
    input_date_end = input("Enter the end date that you want to survey (exclusive)(m/dd/yy): ")
    target_col = utils.get_column(headers, input_col, data)
    date_col = utils.get_column(headers, "Date", data)
    
    # Bonus Question
    date_col_extracted, col_extracted = utils.slice_column(date_col, target_col, input_date_start, input_date_end)
    utils.display_table_1D(date_col_extracted, col_extracted)

main()

# COMMENTS
# The code I wrote was universial enough for the Netflix databse to work perfectly like the Fitbit one
# Since netflix_data.csv doesn't have any statistical values, I could not run stat_computation()
# However, I am confident that the code should run properly if there has been any computable numbers
# I also manage to get the slice_column() function to work as well!