import time
import requests

# different servers to avoid lag
MIRROR_SERVERS = [
    "https://de1.api.radio-browser.info",
    "https://nl1.api.radio-browser.info",
    "https://at1.api.radio-browser.info",
]

HEADERS = {}

# time for how long list is saved from memory before changing.
CACHE_TTL_SECONDS = 300 

_STATION_CACHE = {}