from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API Keys
INSTAGRAM_API_KEY = "5f70d814bfmsh68143605098b3cbp158a99jsnaee998480404"
YOUTUBE_API_KEY = "5f70d814bfmsh68143605098b3cbp158a99jsnaee998480404"

# Instagram Downloader API Endpoint
INSTAGRAM_API_URL = "https://instagram-downloader-api.p.rapidapi.com/download"
# YouTube Downloader API Endpoint
YOUTUBE_API_URL = "https://youtube-downloader-api-fast-reliable-and-easy.p.rapidapi.com/fetch_thumbnail"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download/instagram", methods=["POST"])
def download_instagram():
    url = request.json.get("url")
    
    headers = {
        "x-rapidapi-key": INSTAGRAM_API_KEY,
        "x-rapidapi-host": "instagram-downloader-api.p.rapidapi.com"
    }

    response = requests.get(INSTAGRAM_API_URL, headers=headers, params={"url": url})
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch Instagram media"}), 400

@app.route("/download/youtube", methods=["POST"])
def download_youtube():
    url = request.json.get("url")

    headers = {
        "x-rapidapi-key": YOUTUBE_API_KEY,
        "x-rapidapi-host": "youtube-downloader-api-fast-reliable-and-easy.p.rapidapi.com"
    }

    response = requests.get(YOUTUBE_API_URL, headers=headers, params={"url": url})
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch YouTube media"}), 400

if __name__ == "__main__":
    app.run(debug=True)
