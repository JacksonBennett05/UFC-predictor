import random

# Input dicts of fighter stats then applies rule-based logic (reach longer = +1point) ties are randomly broken
# Returns winner's name and explanation

def predict_outcome(f1_dict, f2_dict) -> (str, str):
    fighter1_score = 0
    fighter2_score = 0

    # Reach
    if (f1_dict.get('Reach', 0) > f2_dict.get('Reach', 0)):
        fighter1_score += 1
        print(f"{f1_dict['Name']} wins Reach")
    elif (f1_dict.get('Reach', 0) < f2_dict.get('Reach', 0)):
        fighter2_score += 1
        print(f"{f2_dict['Name']} wins Reach")

    # Win Percentage
    f1_totalFights = f1_dict.get('Wins') + f1_dict.get('Losses')
    f2_totalFights = f2_dict.get('Wins') + f2_dict.get('Losses')
    f1_winPercentage = f1_dict.get('Wins') / f1_totalFights
    f2_winPercentage = f2_dict.get('Wins') / f2_totalFights

    if (f1_winPercentage > f2_winPercentage):
        fighter1_score += 2
        print(f"{f1_dict['Name']} wins Win %")
    elif (f1_winPercentage < f2_winPercentage):
        fighter2_score += 2
        print(f"{f2_dict['Name']} wins Win %")

    # SLpM
    if (f1_dict.get('SLpM') > f2_dict.get('SLpM')):
        fighter1_score += 1
        print(f"{f1_dict['Name']} wins SLpM")
    elif (f1_dict.get('SLpM') < f2_dict.get('SLpM')):
        fighter2_score += 1
        print(f"{f2_dict['Name']} wins SLpM")

    # Str_Acc
    if (f1_dict.get('Str_Acc') > f2_dict.get('Str_Acc')):
        fighter1_score += 1.5
        print(f"{f1_dict['Name']} wins Striking Accuracy")
    elif (f1_dict.get('Str_Acc') < f2_dict.get('Str_Acc')):
        fighter2_score += 1.5
        print(f"{f2_dict['Name']} wins Striking Accuracy")

    # SApM (lower is better)
    if (f1_dict.get('SApM') < f2_dict.get('SApM')):
        fighter1_score += 1.5
        print(f"{f1_dict['Name']} wins Strikes Absorbed")
    elif (f1_dict.get('SApM') > f2_dict.get('SApM')):
        fighter2_score += 1.5
        print(f"{f2_dict['Name']} wins Strikes Absorbed")

    # Str_Def
    if (f1_dict.get('Str_Def') > f2_dict.get('Str_Def')):
        fighter1_score += 1
        print(f"{f1_dict['Name']} wins Striking Defense")
    elif (f1_dict.get('Str_Def') < f2_dict.get('Str_Def')):
        fighter2_score += 1
        print(f"{f2_dict['Name']} wins Striking Defense")

    # TD_Avg
    if (f1_dict.get('TD_Avg') > f2_dict.get('TD_Avg')):
        fighter1_score += 1
        print(f"{f1_dict['Name']} wins Takedown Avg")
    elif (f1_dict.get('TD_Avg') < f2_dict.get('TD_Avg')):
        fighter2_score += 1
        print(f"{f2_dict['Name']} wins Takedown Avg")

    # TD_Def
    if (f1_dict.get('TD_Def') > f2_dict.get('TD_Def')):
        fighter1_score += 1
        print(f"{f1_dict['Name']} wins Takedown Defense")
    elif (f1_dict.get('TD_Def') < f2_dict.get('TD_Def')):
        fighter2_score += 1
        print(f"{f2_dict['Name']} wins Takedown Defense")

    # Determine winner
    if fighter1_score > fighter2_score:
        winner = f1_dict['Name']
        reason = "By Total Points"
    elif fighter1_score < fighter2_score:
        winner = f2_dict['Name']
        reason = "By Total Points"
    else:
        winner = random.choice([f1_dict['Name'], f2_dict['Name']])
        reason = "Scores tied, picked randomly"
        print("Tie — picking randomly!")

    print(f"🏆 Winner: {winner} ({reason})")
    return winner, reason
