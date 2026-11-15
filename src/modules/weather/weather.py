import requests

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_bootstrap_icon(code):
    if code == 0:
        return "Clear", "bi-sun-fill"
    elif code in [1, 2]:
        return "Partly Cloudy", "bi-cloud-sun-fill"
    elif code == 3:
        return "Overcast", "bi-cloud-fill"
    elif code in [45, 48]:
        return "Foggy", "bi-cloud-fog2-fill"
    elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        return "Rain", "bi-cloud-rain-fill"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "Snow", "bi-cloud-snow-fill"
    elif code in [95, 96, 99]:
        return "Thunderstorm", "bi-cloud-lightning-rain-fill"
    return "Unknown", "bi-cloud"


def fetch_weather(lat, lon):
    parameters = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,weather_code,wind_speed_10m",
    }

    response = requests.get(WEATHER_URL, params=parameters, timeout=5)

    if response.status_code == 200:
        data = response.json()
        current = data.get("current", {})
        code = current.get("weather_code", -1)
        condition, icon_class = get_bootstrap_icon(code)

        return {
            "latitude": lat,
            "longitude": lon,
            "temperature": current.get("temperature_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "condition": condition,
            "icon": icon_class,
        }

    return {}
