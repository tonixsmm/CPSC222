# Tony Nguyen
# CPSC 222 01
# Data Assignment #4
# 10/26/2022
# I attempted the bonus
# Description: This file contains functions and implementations as required by DA4

import requests
import json

# API Description:
# This API is called Random Quotes API
# Documentation: https://github.com/lukePeavey/quotable
# For this project endpoint, I want to ask the user to enter two keywords and let the API
# return a quote that relates to either one of those two.

def main():
    # Prompt user to enter two keywords
    keyword_1 = input("Please enter your first keyword: ")
    keyword_2 = input("Please enter your second keyword (enter n/a if not applicable): ")

    # Create the url query string
    keyword_1.replace(" ", "-")
    keyword_2.replace(" ", "-")

    url = "https://api.quotable.io/random?"
    url += "tags=" + keyword_1.lower()

    if keyword_2 != "n/a":
        url += "|" + keyword_2.lower()

    # Request information from Random Quote API
    inspi_quote = requests.get(url=url)
    json_obj = json.loads(inspi_quote.text)

    # Pretty print the response
    if json_obj["statusCode"] == 404:
        print("Sorry, your keyword does not exist in the API database.")
    else:
        quote = json_obj["content"]
        author = json_obj["author"]

        print("Your quote:", quote)
        print("Author:", author)

main()