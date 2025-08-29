from flask import Flask
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)



@app.route("/", methods=["GET"])
def home():
    return "<h1>Flask application is running</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)