#Imports
import requests
from src.tracker.iss_tracker import get_iss_coordinates
import os
from dotenv import load_dotenv

#URLS
nominatim = "https://nominatim.openstreetmap.org/reverse"
unsplash = "https://api.unsplash.com/search/photos"
headers = {"User-Agent": "MyGeoImageApp/1.0 (suerderin@outlook.com)"}

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
unsplash_access_key = os.getenv("UNSPLASH_ACCESS_KEY")

#get country from longitude and latitude
def get_country(latitude, longitude):
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json"
    }
    response = requests.get(nominatim, params=params, headers=headers).json()
    country = response.get("address", {}).get("country")
    return country

#get 1 photo from unsplash
def get_photo(query):
    if not unsplash_access_key:
        raise RuntimeError("UNSPLASH_ACCESS_KEY is not set (add it to a .env file)")
    params = {
        "query": query,
        "per_page": 1,
        "client_id": unsplash_access_key,
    }
    response = requests.get(unsplash, params=params, headers=headers).json()
    results = response.get("results", [])
    if results:
        photo_url = results[0].get("urls", {}).get("regular")
        return photo_url
    return None

#returns a photo URL from unsplash, or the local ocean image path if over water
OCEAN_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ocean.jpg")

def country_photos():
    latitude, longitude = get_iss_coordinates()
    country = get_country(latitude, longitude)
    if country:
        photo_url = get_photo(country)
        if photo_url:
            return photo_url
    return OCEAN_IMAGE

if __name__ == "__main__":
    print(country_photos())
