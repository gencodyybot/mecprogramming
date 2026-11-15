#import json
import requests
from src.tracker.iss_tracker import get_iss_coordinates


latitude, longitude = get_iss_coordinates()
print(f"ISS Coords: {latitude},  {longitude}")

# API call to get country from latitude and longitude
geocode_response = requests.get(
    f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key=6af9faedd4683529312734utbab4201'
)

geocode_data = geocode_response.json()

try:
    country = geocode_data["address"]["country"]
except(KeyError):
    country = ""
    print("No country found at this location")

# API call to get country data of each country
response = requests.get(
  'https://api.restcountries.com/countries/v5/names.common/' + country + '?response_fields=flag.url_png,area.kilometers,area.kilometers,area.miles,population,subregion,languages.name',
  headers={'Authorization': 'Bearer rc_live_d8e77e9f44e64c0b994b8a19322312c9'}
)   # Area(km), Flag images, Capital, Timezones, Languages

country_data = response.json()

# Append all data to variables
try:
    flag_url = country_data["data"]["objects"][0]["flag"]["url_png"]
    area_km = country_data["data"]["objects"][0]["area"]["kilometers"]
    area_miles = country_data["data"]["objects"][0]["area"]["miles"]
    population = country_data["data"]["objects"][0]["population"]
    languages = country_data["data"]["objects"][0]["languages"]
    subregion = country_data["data"]["objects"][0]["subregion"]
except(KeyError):
    print("No country found at this location")



# Append data to JSON file for debugging

# try:
#     with open("data.json", "r") as json_file:
#         existing_data = json.load(json_file)
# except (FileNotFoundError, json.decoder.JSONDecodeError):
#         existing_data = []

# existing_data.append(country_data)

# with open("data.json", "w") as json_file:
#         json.dump(existing_data, json_file, indent=4)
#         print("Data appended to data.json file.")