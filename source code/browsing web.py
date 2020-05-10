# coding=utf-8
"""
Created on Friday April 17 00:53:34 2020

@author: nkalyan🤠
        '''implementing Python scripts to read website'''
"""

import re
import ssl
import urllib.error                             
import urllib.parse
import urllib.request
from typing import Set

ctx = ssl.create_default_context()                          # ignore SSL certificate errors
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    """ask the user for a URL and lowercase the input in case its capital, with error handling"""
    url: str = input("Enter a URL (Be sure to include http(s)://): ")
    url: str = url.lower()
except EOFError:
    print("EOF command given. Quitting...bye!")
    exit()
except ValueError:
    print("Input is invalid! Please try again.")
    exit()

if not (url.startswith("http://") or url.startswith("https://")):
    """if the user did not enter a properly formatted URL, then throw an error."""
    print("This URL is invalid! Please make sure it starts with http(s):// and try again.")
    exit()

try:
    """makes the request and stores it in an html variable."""
    html  = urllib.request.urlopen(url, context=ctx).read()
except:
    print("An error occurred while opening this URL! Please check the URL, website, or internet connection and try "
          "again.") 
    exit()

links = re.findall(b'"(http[s]?://.*?)"', html)      # gets all the links by applying the regex to the html contents

items: Set = set()                                            # creates a new unique set

if len(links) == 0:
    """Make sure the program found at least 1 link before proceeding."""
    print("The program did not find any links! Please check your URL and try again.")
    exit()

for link in links:
    """loops through the links"""
    link = link.decode()
    link = link.lower()
    items.add(link)

output = len(items)                 # gets the length of the set and stores it to an output variable for easier printing

print(f'There are {output} unique links parsed from your URL.')