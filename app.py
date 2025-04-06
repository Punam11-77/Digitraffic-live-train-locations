from flask import Flask, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/train-locations')
def train_locations():
    url = "https://rata.digitraffic.fi/api/v1/train-locations/latest/"
    headers = {
        'Digitraffic-User': 'YourAppName/1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print('Train location data received:', data)
        return jsonify(data)
    else:
        print('Failed to fetch data:', response.status_code) 
        return jsonify({"error": "Failed to fetch data"}), response.status_code

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == "__main__":
    app.run(debug=True)