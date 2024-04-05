from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# Create a Flask application
app = Flask(__name__)

# Disable automatic sorting of JSON keys
app.config['JSON_SORT_KEYS'] = False

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from other domains
CORS(app)

# Set the path to the JSONL file
jsonlfile = "prompts.jsonl"

# Define the route for the index page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define the route to load the JSONL file
@app.route('/load-jsonl', methods=['GET'])
def load_jsonl():
    try:
        # Open the JSONL file and read its contents
        with open(jsonlfile, 'r') as file:
            data = [json.loads(line) for line in file]
        # Return the data as a JSON response
        return jsonify(data)
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500

# Define the route to save the JSONL file
@app.route('/save-jsonl', methods=['POST'])
def save_jsonl():
    try:
        # Get the data from the request
        data = request.json
        # Open the JSONL file and write the data to it
        with open(jsonlfile, 'w') as file:
            for record in data:
                file.write(json.dumps(record) + '\n')
        # Return a JSON response with a success message
        return jsonify({"status": "success"})
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)