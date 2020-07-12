from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def add_new_user():
    return "yeet!"

if __name__ == "__main__":
    app.run()