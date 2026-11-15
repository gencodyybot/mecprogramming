import requests
import json

country = 'ger'

response = requests.get(
  'https://api.restcountries.com/countries/v5/names.common?q=ger',
  headers={'Authorization': 'Bearer rc_live_d8e77e9f44e64c0b994b8a19322312c9'}
)

status = response.status_code 

data = response.json()

if status == 200:
    try:
        with open("./country_data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = []

    existing_data.append(data)
                        
    with open("./country_data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4)
        print("Data appended to data.json file.")
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)