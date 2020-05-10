# coding=utf-8
"""
Created on Monday 28 March 00:53:34 2020

@author: nkalyan🤠
        Description: program that uses the US Census geocoding API (Links to an external site.)
        (access link for a full description of the API) to retrieve the location (latitude and longitude) of the U.S.
        White House (1600 Pennsylvania Avenue, Washington, DC) and that of your local residence,
        and compute the approximate distance, in miles, between the two locations.
"""

import urllib.request, urllib.parse, urllib.error
import re
import ssl
import json
from math import pi, sin, cos, sqrt, asin

ctx = ssl.create_default_context()          # ignore SSL certificate errors
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def lookup_address(street, city, state, zip):
    """method that takes the input parameters and make an http request to get back
        the json response"""
    params = {                  # get the params ready for encoding
        'street': street,
        'city': city,
        'state': state,
        'zip': zip,
        'benchmark': 'Public_AR_Current',
        'format': 'json'
    }

    params = urllib.parse.urlencode(params)
    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'
    url = url + '?' + params

    try:
        """make the request and catch if an error occurs"""
        json = urllib.request.urlopen(url, context=ctx).read()
    except:
        print('An error occurred while looking up the address! Please check your internet connection and try again.')
        exit()

    json = json.decode()
    return json


def parse_address_json(json_data):
    """Method which takes the json response from lookup_address and attempts to parse out the
        coordinates from the json. """
    try:
        json_data = json.loads(json_data)
        coordinates = json_data['result']['addressMatches'][0]['coordinates']
        return coordinates
    except:
        print('The address could not be found! Please check the address and try again.')
        exit()


def convert_to_radians(value):
    """method converts an individual value to radians"""
    try:
        return value * pi / 180
    except:
        print('An unexpected error occurred! Please try again.')
        exit()
        

try:
    """error handling"""
    street = input('Enter your house number and street name (Ex: 123 Smith Street): ')
    city = input('Enter your city (Ex: Trenton): ')
    state = input('Enter your state (Ex: California): ')
    zip = input('Enter your zip code (Ex: 07016): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

if len(street) == 0 or len(city) == 0 or len(state) == 0 or len(zip) == 0:
    """verifies that they filled out all fields"""
    print('One or more of your inputs was blank. All fields are required. Please try again!')
    exit()
else:
    print('Great! Looking up your address...')

# calls the lookup_address method with their inputs, and stores the result in user_address_json
user_address_json = lookup_address(street, city, state, zip)
user_coordinates = parse_address_json(user_address_json)

try:
    user_lon = float(user_coordinates['x'])
    user_lat = float(user_coordinates['y'])
except:
    print('An unexpected error occurred! Please try again.')
    exit()

print('We found your address! Looking up the address of The White House...')

street = "1600 Pennsylvania Ave NW"
city = "Washington"
state = "DC"
zip = "20500"

# calls the look up method to store the address of white house
white_house_address_json = lookup_address(street, city, state, zip)
white_house_coordinates = parse_address_json(white_house_address_json)

try:
    white_house_lon = float(white_house_coordinates['x'])
    white_house_lat = float(white_house_coordinates['y'])
except:
    print('An unexpected error occurred! Please try again.')
    exit()

print('The White House address found. Calculating the distance between them...')

# Convert to radians
user_lon_radians = convert_to_radians(user_lon)
user_lat_radians = convert_to_radians(user_lat)
white_house_lon_radians = convert_to_radians(white_house_lon)
white_house_lat_radians = convert_to_radians(white_house_lat)

# approximate radius of earth in mi
R = 3956

# assigns the radian variables to new variables
lat1 = white_house_lat_radians
lon1 = white_house_lon_radians
lat2 = user_lat_radians
lon2 = user_lon_radians


try:
    """wrap the math in a try/except incase anything goes wrong."""
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(min(1, sqrt(a)))

    distance = R * c
except:
    print('An unexpected error occurred! Please try again.')
    exit()

# round to the nearest mile.
distance = round(distance)

# return the result to the user.
print(f'The distance between your home and The White House is about {distance} miles.')