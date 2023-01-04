# Tony Nguyen
# CPSC 222 01
# Data Assignment #3
# 10/13/2022
# I attempted the bonus
# Description: This file exercises functions in utils.py

import utils

def main():
    address, city, state, zip_code, country = utils.get_address()
    latitude, longtitude = utils.get_coordinate(address, city, state, zip_code, country)
    station_id = utils.get_weather_station(latitude, longtitude)
    daily_data = utils.get_daily_weather_data(station_id, city)
    daily_data_cleaned = utils.clean_data(daily_data, city)
    utils.data_visualization(daily_data_cleaned, city)

main()