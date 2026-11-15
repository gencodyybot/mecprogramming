import webbrowser

import requests
from src.tracker.iss_tracker import get_iss_coordinates

url = "https://commons.wikimedia.org/w/api.php"
headers = {"User-Agent": "MyGeoImageApp/1.0 (suerderin@outlook.com)"}

def get_photos(latitude, longitude, radius=10000, limit=3):
    params = {
        "action": "query",
        "generator": "geosearch",
        "ggscoord": f"{latitude}|{longitude}",
        "ggsradius": radius,
        "ggsnamespace": 6,
        "ggsprimary": "all",
        "ggslimit": limit,
        "prop": "imageinfo|coordinates",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 400,
        "format": "json"
    }

    response = requests.get(url, params=params, headers=headers).json()
    pages = response.get("query", {}).get("pages", {})

    photos = []
    for page_id, page_data in pages.items():
        title = page_data.get("title")
        image_info = page_data.get("imageinfo", [{}])[0]
        full_url = image_info.get("url")
        thumb_url = image_info.get("thumburl")
        photos.append({
            "title": title,
            "full_url": full_url,
            "thumb_url": thumb_url
        })

    return photos


def main():
    latitude, longitude = get_iss_coordinates()
    print(f"ISS coordinates: {latitude}, {longitude}")

    photos = get_photos(latitude, longitude)
    if not photos:
        print("No nearby Wikimedia Commons photos found.")
        return

    for photo in photos:
        print(f"{photo['title']}: {photo['thumb_url']}")
        if photo["thumb_url"]:
            webbrowser.open(photo["thumb_url"])


if __name__ == "__main__":
    main()
