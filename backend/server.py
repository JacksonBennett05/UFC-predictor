from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from predictor import predict_outcome


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Load data from CSV once at startup
def load_fighters():
    fighters = {}
    with open("fighters.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key in row:
                if key != "Name":  # keep name as string
                    try:
                        if "." in row[key]:
                            row[key] = float(row[key])
                        else:
                            row[key] = int(row[key])
                    except ValueError:
                        pass  # leave alone if not numeric
            fighters[row["Name"]] = row
    return fighters

fighters = load_fighters()

@app.route("/fighters")
def search_fighters():
    query = request.args.get("search", "").lower()
    matches = [name for name in fighters.keys() if query in name.lower()][:100]
    return jsonify(matches)

@app.route("/simulate", methods=["POST"])
def simulate_fight():
    data = request.get_json()
    fighter1_name = data.get("fighter1")
    fighter2_name = data.get("fighter2")

    fighter1 = fighters.get(fighter1_name)
    fighter2 = fighters.get(fighter2_name)

    if not fighter1:
        return jsonify({"error": f"Fighter '{fighter1_name}' not found."}), 404
    if not fighter2:
        return jsonify({"error": f"Fighter '{fighter2_name}' not found."}), 404
    if fighter1_name == fighter2_name:
        return jsonify({"error": "A fighter cannot fight themselves."}), 400

    winner, reason, category_winners, fighter1, fighter2 = predict_outcome(fighter1, fighter2)
    return jsonify({"winner": winner, "explanation": reason, "breakdown": category_winners, "fighter1": fighter1_name, "fighter2": fighter2_name})

if __name__ == "__main__":
    app.run(debug=True)
