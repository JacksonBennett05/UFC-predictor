#Loads fighter data using preprocess looks up fighters by name, calls predict_outcome from predictor
# Returns predicted winner and explanation
def simulate_fight(f1_name: str, f2_name: str) -> (str, str):
    