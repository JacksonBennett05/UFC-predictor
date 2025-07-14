from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Load data from CSV once at startup
def load_fighters():
    fighters = []
    with open("fighters.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fighters.append(row["Name"])
    return fighters

fighter_names = load_fighters()

@app.route("/fighters")
def search_fighters():
    query = request.args.get("search", "").lower()
    
    matches = [name for name in fighter_names if query in name.lower()][:5]
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
