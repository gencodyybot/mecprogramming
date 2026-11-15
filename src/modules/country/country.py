from flask import Flask
import requests
import json


# API call to get country from latitude and longitude

latitude = str(43.266337)
longitude = str(-79.915990)

geocode_response = requests.get(
    'https://geocode.maps.co/reverse?lat='+ latitude +'&lon='+ longitude +'&api_key=6af9faedd4683529312734utbab4201'
)

geocode_data = geocode_response.json()

# try:
#     with open("./geocode_data.json", "r") as json_file:
#         existing_geocode_data = json.load(json_file)
# except (FileNotFoundError, json.decoder.JSONDecodeError):
#     existing_geocode_data = []

# existing_geocode_data.append(geocode_data)
                    
# with open("./geocode_data.json", "w") as json_file:
#     json.dump(existing_geocode_data, json_file, indent=4)
#     print("Data appended to data.json file.")




country = geocode_data["address"]["country"]

# API call to get country data of each country
# Area(km), Flag images, Capital, Timezones, Languages
response = requests.get(
  'https://api.restcountries.com/countries/v5/names.common/' + country + '?response_fields=flag.url_png,area.kilometers,area.kilometers,population,timezones,languages.name',
  headers={'Authorization': 'Bearer rc_live_d8e77e9f44e64c0b994b8a19322312c9'}
)


status = response.status_code 

country_data = response.json()

# Country that we want to get data for

# Append API call to a JSON file
# if status == 200:
#     try:
#         with open("./country_data.json", "r") as json_file:
#             existing_country_data = json.load(json_file)
#     except (FileNotFoundError, json.decoder.JSONDecodeError):
#         existing_country_data = []

#     existing_country_data.append(country_data)
                        
#     with open("./country_data.json", "w") as json_file:
#         json.dump(existing_country_data, json_file, indent=4)
#         print("Data appended to data.json file.")
# else:
#     print("Failed to retrieve data from the API. Status code:", response.status_code)


# Display API data on webpage

app = Flask(country)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"