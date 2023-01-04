# Tony Nguyen
# CPSC 222 01
# Data Assignment #4
# 10/26/2022
# I attempted the bonus
# Description: This file contains functions and implementations as required by DA4

import pandas as pd
import numpy as np
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_address():
    # This function prompts the user for their address and processes them into url-compatible format
    # Parameter: void
    # Return: five variables corresponding to address, city, state, zip code, and country that user entered

    # Prompt user to enter their address information
    address = input("Please enter the address: ")
    city = input("Please enter city name: ")
    state = input("Please enter state name (enter n/a if not applicable): ")
    zip_code = input("Please enter zip code (enter n/a if not applicable): ")
    country = input("Please enter country name: ")

    # Process the address information and turn them into url-compatible format
    address = address.replace(" ", "+")
    city = city.replace(" ", "+")
    state = state.replace(" ", "+")
    zip_code = zip_code.replace(" ", "+")
    country = country.replace(" ", "+")

    return address, city, state, zip_code, country

def get_coordinate(address, city, state, zip_code, country):
    # This function requests a geographical coordinate system from MapQuest API using address information passed in and stores them in two variables
    # Parameter: five variables representing address, city, state, zip_code, and country information correspondingly
    # Return: two variables representing the latitude and longtitude returned from MapQuest API

    # Load API key
    infile = open("mapquest_api_key.txt", "r")
    api_key = infile.readline()
    infile.close()
    
    # Create the url query string
    url = "http://www.mapquestapi.com/geocoding/v1/address"
    url += "?key=" + api_key
    url += "&location=" + address + "," + city
    if state != "n/a":
        url += "," + state
    if zip_code != "n/a":
        url += "," + zip_code
    url += "," + country

    # Request information from MapQuest API
    geo_location = requests.get(url=url)

    # Process the JSON text returned from the API query
    json_obj = json.loads(geo_location.text)
    result_list = json_obj["results"]
    result_obj = result_list[0]
    locations = result_obj["locations"]
    locations_obj = locations[0]
    coordinate_obj = locations_obj["displayLatLng"]
    latitude = coordinate_obj["lat"]
    longtitude = coordinate_obj["lng"]

    return latitude, longtitude

def get_weather_station(latitude, longtitude):
    # This function requests a weather station id from MeteoStat API using geographical coordinate system passed in and stores it in a variable
    # Parameter: two variables representing the latitude and longtidue
    # Return: the nearest station id to the given latitude and longtitude
    
    # Load API key
    infile = open("meteostat_api_key.txt")
    api_key = infile.readline()
    infile.close()

    # Create the url query string
    headers = {"x-rapidapi-key": api_key, "X-RapidAPI-Host": "meteostat.p.rapidapi.com"}
    params = {"lat": latitude, "lon": longtitude}
    url = "https://meteostat.p.rapidapi.com/stations/nearby"

    # Request information from Meteostat API
    weather_station = requests.get(url=url, headers=headers, params=params)

    # Process the JSON text returned from the API query
    json_obj = json.loads(weather_station.text)
    data_list = json_obj["data"]
    data_obj = data_list[0]
    station_id = data_obj["id"]

    return station_id

def get_daily_weather_data(station_id, city):
    # This function requests daily weather data from 10/23/2021 to 10/22/2022 from MeteoStat API using a station id and exports them into a .csv file
    # Parameter: station_id - weather station id, city - weather station's city
    # Return: a dataframe contains weather information

    # Load API key
    infile = open("meteostat_api_key.txt")
    api_key = infile.readline()
    infile.close()

    # Create the url query string
    headers = {"x-rapidapi-key": api_key, "X-RapidAPI-Host": "meteostat.p.rapidapi.com"}
    params = {"station": station_id, "start": "2021-10-23", "end": "2022-10-22", "units": "imperial"}
    url = "https://meteostat.p.rapidapi.com/stations/daily"

    # Request information from Meteostat API
    daily_data = requests.get(url=url, headers=headers, params=params)

    # Process the JSON text returned from the API query and load them into a dataframe
    json_obj = json.loads(daily_data.text)
    data_list = json_obj["data"]
    daily_data_df = pd.DataFrame(data_list)
    daily_data_df.set_index("date", inplace=True)
    
    # Convert city's formatting to file-compatible format and export it to a .csv file
    city = city.replace("+", "_")
    filename = city.lower() + "_daily_weather.csv"
    daily_data_df.to_csv(filename)

    return daily_data_df

def clean_data(data, city):
    # This function cleans the daily weather data and exports them to a new .csv file
    # Parameter: data - a dataframe, city - name of the city that data was recorded
    # Return: a dataframe contains cleaned daily weather data

    # Iterate through atrributes to see if there is any that is missing more than 50% of its instances' value.
    # If there is, drop it
    data.replace("", np.NaN, inplace=True)
    for col in data.columns:
        if data.loc[:, col].isnull().sum() > (data.shape[0] / 2):
            data.drop(columns=col, inplace=True)

    # Fill the remaining missing data points
    # Call interpolate() to fill "middle" values using linear mode first
    # Then use fillna() to fill the remaining beginning and ending missing values, if any
    data.interpolate(method='linear', inplace=True)
    data.fillna(method="ffill", inplace=True)
    data.fillna(method="bfill", inplace=True)

    # Convert city to file-compatible format and export the cleaned dataframe to a .csv file
    city = city.replace("+", "_")
    filename = city.lower() + "_daily_weather_cleaned.csv"
    data.to_csv(filename)

    return data

def data_visualization(data, city):
    # This function visualizes prompts the user for an attribute name (in a dataframe) and visualizes it with a bar chart
    # Parameter: data - a dataframe, city - name of the city that data was recorded
    # Return: void

    # Print out available attribute names and prompt user to select one
    count = 0
    att_dictionary = {}
    print("Names of attribute:")
    for i in data.columns:
        att_dictionary[count] = i
        count += 1
    print(att_dictionary)
    desired_attribute_num = input("Please enter the number corresponding to your desired attribute: ")

    # Convert the dataframe's index type to datetime format
    data.index = pd.to_datetime(data.index)
    
    # Plot the bar chart
    plt.figure()
    fig, ax = plt.subplots()
    ax.bar(data.index, data.iloc[:, int(desired_attribute_num)])

    # Set the x-tick to readable month-year format
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b`%y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    # source: https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html#sphx-glr-gallery-text-labels-and-annotations-date-py

    # Format the bar chart
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Month")
    plt.ylabel("Temperature (F)")

    title_name = city.replace("+", " ")
    title_name = title_name.title() + " Daily " + att_dictionary[int(desired_attribute_num)].title() + " Data"
    plt.title(title_name)
    
    plt.tight_layout()

    # Process city name and export the chart to a new .png file
    city = city.replace("+", "_")
    filename = city.lower() + "_daily_" + att_dictionary[int(desired_attribute_num)] + ".png"
    plt.savefig(filename)