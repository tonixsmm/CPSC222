'''
Programmer: Tony Nguyen
Class: CPSC 222, Fall 2022
Data Assignment #2
9/29/2022
I attempted the bonus
Description: This file exercises functions in utils.py 
'''

import utils

def main():
    # This function exercises the codings in utils.py
    # Parameter: void
    # Return: void

    # Read data from file
    headers, data = utils.read_data("fitbit_data.csv")
    utils.display_table(headers, data)

    # Prompt the user to select the target data to survey
    input_col = input("Enter the name of the column you want to survey: ")
    input_date_start = input("Enter the start date that you want to survey (m/dd/yy): ")
    input_date_end = input("Enter the end date that you want to survey (exclusive) (m/dd/yy): ")
    target_col = utils.get_column(headers, input_col, data)
    date_col = utils.get_column(headers, "Date", data)
    utils.convert_to_float_1D(target_col)
    utils.stat_computation(target_col)

    # Bonus Question
    date_col_extracted, col_extracted = utils.slice_column(date_col, target_col, input_date_start, input_date_end)
    utils.display_table_1D(date_col_extracted, col_extracted)

main()