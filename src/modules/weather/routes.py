from flask import Blueprint, jsonify, request
from .weather import fetch_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather", methods=["GET"])
def get_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "lat and lon are required"}), 400

    weather_data = fetch_weather(lat, lon)
    return jsonify(weather_data)
