import requests
from flask import Flask, jsonify

ISS_URL="https://api.wheretheiss.at/v1/satellites/25544"

app = Flask(__name__)

@app.route("/")
def get_iss_position():
    response = requests.get(ISS_URL)
    data = response.json()
    return jsonify(data["latitude"], data["longitude"])
