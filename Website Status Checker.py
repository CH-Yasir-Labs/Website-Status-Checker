#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chyas
#
# Created:     14/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website {url} is ONLINE!")
        else:
            print(f"The website {url} is NOT reachable. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: The website {url} could not be reached. {e}")

# Example usage
url = input("Enter the website URL (e.g., http://example.com): ")
check_website_status(url)
