# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
import requests
import argparse
import os
import sys

API_KEY = os.getenv('API_KEY')
print(API_KEY)

parser = argparse.ArgumentParser(description='get the current weather information for your zipcode')

parser.add_argument('zipcode', help='zipcode of the area you require the weather forecast for')
parser.add_argument('--country', default='GB', help='enter 2 character country code defaults to \'GB\'')

args = parser.parse_args()

if not API_KEY:
    print("Error: No \'API_KEY\' environment variable set")
    sys.exit(1)

url = f'http://api.openweathermap.org/data/2.5/weather?zip={args.zipcode},{args.country}&appid={API_KEY}'

response = requests.get(url)

if(response.status_code != 200):
    print(f"error connecting to weather API: HTTP Status code: {response.status_code}" )
    sys.exit(1)

print(response.json())

