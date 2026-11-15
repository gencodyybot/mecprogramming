import os
from flask import Blueprint, jsonify, request, send_from_directory
from .offline_music import get_offline_track

music_bp = Blueprint("music", __name__)

AUDIO_FOLDER = os.path.abspath("public/audio")


@music_bp.route("/offline", methods=["GET"])
def offline_music():
    mode = request.args.get("mode")
    track = get_offline_track(mode)
    return jsonify({
        "count": 1,
        "stations": [track],
    })


@music_bp.route("/stream/<filename>", methods=["GET"])
def stream_local_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)