from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# This code was generated with the help of co-pilot.

# Load environment variables from .env if present
load_dotenv()

# set port as variable from .env and turn into an integer
port = int(os.getenv("PORT", 3030))

# Create Flask app
app = Flask(__name__)

# Apply CORS to the app to allow access from different origins to /products endpoint with GET calls

CORS(app , resources={r"/products": {"origins": "*", "methods": ["GET"]}})

# Define product list

products=[
  {"id": 1, "name": "Dog Food", "price": 19.99},
  {"id": 2, "name": "Cat Food", "price": 34.99},
  {"id": 3, "name": "Bird Seeds", "price": 10.99}
]

# Define route to get products with positive response ensure CORS is applied
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)