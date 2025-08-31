import random
from config import STAT_WEIGHTS
from typing import Dict, Tuple

# Input dicts of fighter stats then applies rule-based logic (reach longer = +1point) ties are randomly broken
# Returns winner's name and explanation

def predict_outcome(f1_dict: dict, f2_dict: dict) -> Tuple[str, str, Dict[str, str]]:
    fighter1_score = 0
    fighter2_score = 0
    category_winners = {}
    

    # Reach
    if (f1_dict.get('Reach', 0) > f2_dict.get('Reach', 0)):
        fighter1_score += 1 * STAT_WEIGHTS["Reach"]
        print(f"{f1_dict['Name']} wins Reach")
        category_winners["Reach"] = f1_dict['Name']
    elif (f1_dict.get('Reach', 0) < f2_dict.get('Reach', 0)):
        fighter2_score += 1 * STAT_WEIGHTS["Reach"]
        print(f"{f2_dict['Name']} wins Reach")
        category_winners["Reach"] = f2_dict['Name']

    # Win Percentage
    f1_totalFights = f1_dict.get('Wins') + f1_dict.get('Losses')
    f2_totalFights = f2_dict.get('Wins') + f2_dict.get('Losses')
    f1_winPercentage = f1_dict.get('Wins') / f1_totalFights
    f2_winPercentage = f2_dict.get('Wins') / f2_totalFights

    if (f1_winPercentage > f2_winPercentage):
        fighter1_score += 2
        print(f"{f1_dict['Name']} wins Win %")
        category_winners["Win %"] = f1_dict['Name']
    elif (f1_winPercentage < f2_winPercentage):
        fighter2_score += 2
        print(f"{f2_dict['Name']} wins Win %")
        category_winners["Win %"] = f2_dict['Name']

    # SLpM
    if (f1_dict.get('SLpM') > f2_dict.get('SLpM')):
        fighter1_score += 1 *STAT_WEIGHTS["SLpM"]
        print(f"{f1_dict['Name']} wins SLpM")
        category_winners["Significant Strikes per Minute"] = f1_dict['Name']
    elif (f1_dict.get('SLpM') < f2_dict.get('SLpM')):
        fighter2_score += 1 * STAT_WEIGHTS["SLpM"]
        print(f"{f2_dict['Name']} wins SLpM")
        category_winners["Significant Strikes per Minute"] = f2_dict['Name']

    # Str_Acc
    if (f1_dict.get('Str_Acc') > f2_dict.get('Str_Acc')):
        fighter1_score += 1 * STAT_WEIGHTS["Str_Acc"]
        print(f"{f1_dict['Name']} wins Striking Accuracy")
        category_winners["Striking Accuracy"] = f1_dict['Name']
    elif (f1_dict.get('Str_Acc') < f2_dict.get('Str_Acc')):
        fighter2_score += 1 * STAT_WEIGHTS["Str_Acc"]
        print(f"{f2_dict['Name']} wins Striking Accuracy")
        category_winners["Striking Accuracy"] = f2_dict['Name']

    # SApM (lower is better)
    if (f1_dict.get('SApM') < f2_dict.get('SApM')):
        fighter1_score += -1 * STAT_WEIGHTS["SApM"] 
        print(f"{f1_dict['Name']} wins Strikes Absorbed")
        category_winners["Strikes Absorbed per Minute"] = f1_dict['Name']
    elif (f1_dict.get('SApM') > f2_dict.get('SApM')):
        fighter2_score += -1 * STAT_WEIGHTS["SApM"]
        print(f"{f2_dict['Name']} wins Strikes Absorbed")
        category_winners["Strikes Absorbed per Minute"] = f2_dict['Name']

    # Str_Def
    if (f1_dict.get('Str_Def') > f2_dict.get('Str_Def')):
        fighter1_score += 1 * STAT_WEIGHTS["Str_Def"]
        print(f"{f1_dict['Name']} wins Striking Defense")
        category_winners["Striking Defense"] = f1_dict['Name']
    elif (f1_dict.get('Str_Def') < f2_dict.get('Str_Def')):
        fighter2_score += 1 * STAT_WEIGHTS["Str_Def"]
        print(f"{f2_dict['Name']} wins Striking Defense")
        category_winners["Striking Defense"] = f2_dict['Name']

    # TD_Avg
    if (f1_dict.get('TD_Avg') > f2_dict.get('TD_Avg')):
        fighter1_score += 1 * STAT_WEIGHTS["TD_Avg"]
        print(f"{f1_dict['Name']} wins Takedown Avg")
        category_winners["Takedown Average"] = f1_dict['Name']
    elif (f1_dict.get('TD_Avg') < f2_dict.get('TD_Avg')):
        fighter2_score += 1 * STAT_WEIGHTS["TD_Avg"]
        print(f"{f2_dict['Name']} wins Takedown Avg")
        category_winners["Takedown Average"] = f2_dict['Name']

    # TD_Def
    if (f1_dict.get('TD_Def') > f2_dict.get('TD_Def')):
        fighter1_score += 1 * STAT_WEIGHTS["TD_Def"]
        print(f"{f1_dict['Name']} wins Takedown Defense")
        category_winners["Takedown Defense"] = f1_dict['Name']
    elif (f1_dict.get('TD_Def') < f2_dict.get('TD_Def')):
        fighter2_score += 1 * STAT_WEIGHTS["TD_Def"]
        print(f"{f2_dict['Name']} wins Takedown Defense")
        category_winners["Takedown Defense"] = f2_dict['Name']

    # Determine winner
    if fighter1_score > fighter2_score:
        winner = f1_dict['Name']
        reason = f"By Total Points: {fighter1_score} to {fighter2_score}"
    elif fighter1_score < fighter2_score:
        winner = f2_dict['Name']
        reason = f"By Total Points: {fighter2_score} to {fighter1_score}"
    else:
        winner = random.choice([f1_dict['Name'], f2_dict['Name']])
        reason = "Scores tied, picked randomly"
        print("Tie — picking randomly!")

    print(f"🏆 Winner: {winner} ({reason})")
    return winner, reason, category_winners, f1_dict, f2_dict
