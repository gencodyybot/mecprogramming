from flask import Flask
import requests
import json
from src.tracker.iss_tracker import get_iss_position



# API call to get country from latitude and longitude

print(get_iss_position())

latitude = str(43.266337)
longitude = str(-79.915990)

geocode_response = requests.get(
    'https://geocode.maps.co/reverse?lat='+ latitude +'&lon='+ longitude +'&api_key=6af9faedd4683529312734utbab4201'
)

geocode_data = geocode_response.json()

country = geocode_data["address"]["country"]

# API call to get country data of each country
# Area(km), Flag images, Capital, Timezones, Languages
response = requests.get(
  'https://api.restcountries.com/countries/v5/names.common/' + country + '?response_fields=flag.url_png,area.kilometers,area.kilometers,population,timezones,languages.name',
  headers={'Authorization': 'Bearer rc_live_d8e77e9f44e64c0b994b8a19322312c9'}
)

country_data = response.json()

# Display API data on webpage

app = Flask(country)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"