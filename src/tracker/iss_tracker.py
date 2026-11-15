import requests
from flask import Flask, jsonify

ISS_URL="https://api.wheretheiss.at/v1/satellites/25544"

app = Flask(__name__)

@app.route("/")
def get_iss_position():
    latitude, longitude = get_iss_coordinates()
    return jsonify(latitude, longitude)


def get_iss_coordinates():
    response = requests.get(ISS_URL)
    data = response.json()
    return data["latitude"], data["longitude"]
