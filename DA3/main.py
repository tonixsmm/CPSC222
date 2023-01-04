'''
Tony Nguyen
CPSC 222 01
Data Assignment #3
10/13/2022
I attempted the bonus
Description: This file exercises functions in utils.py 
'''

import utils

def main():
    # This function exercises the codings in utils.py
    # Parameter: void
    # Return: void

    youtube_df = utils.read_data("youtube_data.csv")
    days_df = utils.read_data("days_list.csv")
    selected_list, selected_column_name = utils.slice_column(youtube_df)
    utils.stat_computation(selected_list[selected_column_name])
    merged_df = utils.join_data(days_df, youtube_df)
    utils.split_apply_combine(merged_df, selected_column_name)

main()