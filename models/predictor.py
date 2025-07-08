# Input dicts of fighter stats then applies rule-based logic (reach longer = +1point) ties are randomly broken
# Returns winner's name and explanation

def predict_outcome(f1_dict, f2_dict) -> (str, str):