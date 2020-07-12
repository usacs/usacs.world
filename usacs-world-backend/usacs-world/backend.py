from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/<id>', methods=['GET'])
def get_user_profile(id):
    with open("data.json", "r") as f:
        data = json.load(f)
        return jsonify(data[id]) 

@app.route('/sign_up', methods=['POST'])
def add_new_user():
    raw = request.get_json()
    with open("data.json", "r") as f:
        data = json.load(f)
        data[raw['name']] = raw

    with open("data.json", "w") as f:
        json.dump(data, f)

    return "yeet yeet yeet"

@app.route('/directory', methods=['GET'])
def get_all_user():
    with open("data.json", "r") as f:
        data=json.load(f) 
        return jsonify(data)

if __name__ == "__main__":
    app.run()