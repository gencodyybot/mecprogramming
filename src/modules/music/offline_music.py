import random

OFFLINE_TRACKS = [
    {
        "stationuuid": "offline-elevator",
        "name": "Orbital Hold — Elevator Lounge",
        "url_resolved": "/music/stream/elevator.mp3",
        "countrycode": "OFFLINE",
        "tags": "elevator,lounge,fallback",
        "is_fallback": True,
    },
    {
        "stationuuid": "offline-calm",
        "name": "Deep Space Drift — Calm Ambient",
        "url_resolved": "/music/stream/calm.mp3",
        "countrycode": "OFFLINE",
        "tags": "calm,ambient,fallback",
        "is_fallback": True,
    },
]

def get_offline_track(mode=None):
    # If frontend asks for a specific track ("elevator" or "calm"), return that one
    if mode == "elevator":
        return OFFLINE_TRACKS[0]
    if mode == "calm":
        return OFFLINE_TRACKS[1]

    # Otherwise pick one at random
    return random.choice(OFFLINE_TRACKS)