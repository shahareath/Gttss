from flask import Flask, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}, 400

    filename = f"/tmp/{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)

    return send_file(filename, mimetype="audio/mpeg")

@app.route("/", methods=["GET"])
def home():
    return {"message": "gTTS API is running on Render!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
