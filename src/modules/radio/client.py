import time
import requests

# different servers to avoid lag
MIRROR_SERVERS = [
    "https://de1.api.radio-browser.info",
    "https://nl1.api.radio-browser.info",
    "https://at1.api.radio-browser.info",
]

HEADERS = {"User-Agent": "mecprogramming/1.0"}

# time for how long list is saved from memory before changing
CACHE_TTL_SECONDS = 300 

_STATION_CACHE = {}

# main function for fetching stations
def fetch_raw_stations(country_code, tag="music", limit=25):
    parameters = {
        "countrycode": country_code,
        "tag" : "music",
        "is_https": "true",
        "hidebroken": "true",
        "limit": 10
    }

    if not country_code:
        return []
    cache_key = (country_code.strip().upper(), tag.strip().lower())
    if cache_key in _STATION_CACHE:
        saved_time, saved_stations = _STATION_CACHE[cache_key]
        if time.time() - saved_time < CACHE_TTL_SECONDS:
            return saved_stations

    response = requests.get(
        f"{MIRROR_SERVERS[0]}/json/stations/search",
        params=parameters,
        headers=HEADERS,
        timeout=5,
    )

    if response.status_code == 200:
        stations = response.json()
        _STATION_CACHE[cache_key] = (time.time(), stations)
        return stations

    return []

stations = fetch_raw_stations("CA")
print(stations[0]["name"], stations[0]["url_resolved"])