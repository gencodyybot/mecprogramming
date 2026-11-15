# function to filter out bad or unneccessary stuff that might disrupt listening experience

# allowing only the most common audio formats
ALLOWED_CODECS = ["MP3", "AAC", "OGG"]
# so that only music channels are playing
BANNED_WORDS = ["news", "talk", "speech", "sports", "politics", "religion", "traffic", "weather", "podcast"]

def clean_stations(raw_stations):
    cleaned = []
    for station in raw_stations:
        # 1. Skip offline stations
        if station.get("lastcheckok") != 1:
            continue

        # 2. Skip non-HTTPS links (browsers block HTTP audio)
        stream_url = station.get("url_resolved", "")
        if not stream_url.startswith("https://"):
            continue

        # 3. Skip audio formats browsers can't play
        codec = station.get("codec", "").upper()
        if codec not in ALLOWED_CODECS:
            continue

        # 4. Skip news, talk, or sports stations
        text = f"{station.get('tags', '')} {station.get('name', '')}".lower()
        has_banned_word = False
        for word in BANNED_WORDS:
            if word in text:
                has_banned_word = True
                break

        if has_banned_word:
            continue

        # Keep only the fields the rest of the app needs
        cleaned.append({
            "stationuuid": station.get("stationuuid"),
            "name": station.get("name"),
            "url_resolved": stream_url,
            "countrycode": station.get("countrycode"),
            "tags": station.get("tags"),
            "bitrate": station.get("bitrate"),
        })
    return cleaned