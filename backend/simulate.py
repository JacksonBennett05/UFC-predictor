import argparse
from preprocess import load_fighter_data
from predictor import predict_outcome

#Loads fighter data using preprocess looks up fighters by name, calls predict_outcome from predictor
# Returns predicted winner and explanation
def simulate_fight(f1_name: str, f2_name: str) -> (str, str):
     # Load fighter data from CSV
    fighters = load_fighter_data()

    # Look up each fighter by name
    f1_data = fighters.get(f1_name)
    f2_data = fighters.get(f2_name)


    if not f1_data:
        return f"Fighter '{f1_name}' not found.", ""
    if not f2_data:
        return f"Fighter '{f2_name}' not found.", ""

    winner, explanation = predict_outcome(f1_data, f2_data)
    return winner, explanation


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a fight between two fighters.")
    parser.add_argument("fighter1", type=str, help="Name of the first fighter")
    parser.add_argument("fighter2", type=str, help="Name of the second fighter")

    args = parser.parse_args()

    winner, explanation = simulate_fight(args.fighter1, args.fighter2)
    print(f"\nPredicted winner: {winner}")
    if explanation:
        print(f"Explanation: {explanation}")