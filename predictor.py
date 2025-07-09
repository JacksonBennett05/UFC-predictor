import random

# Input dicts of fighter stats then applies rule-based logic (reach longer = +1point) ties are randomly broken
# Returns winner's name and explanation

def predict_outcome(f1_dict, f2_dict) -> (str, str):
    fighter1_score = 0
    fighter2_score = 0

    # Longer Reach is better
    if (f1_dict.get('Reach', 0) > f2_dict.get('Reach', 0)):
        fighter1_score += 1

    elif (f1_dict.get('Reach', 0) < f2_dict.get('Reach', 0)):
        fighter2_score += 1
    
    # More better win percentage is better
    f1_totalFights = f1_dict.get('Wins') + f1_dict.get('Losses')
    f2_totalFights = f2_dict.get('Wins') + f2_dict.get('Losses')
    f1_winPercentage = f1_dict.get('Wins')/f1_totalFights
    f2_winPercentage = f2_dict.get('Wins')/f2_totalFights

    if (f1_winPercentage > f2_winPercentage):
        fighter1_score += 2
    elif (f1_winPercentage < f2_winPercentage):
        fighter2_score += 2
    
    # More significant strikes per minute is better
    if (f1_dict.get('SLpM') > f2_dict.get('SLpM')):
        fighter1_score += 1
    elif (f1_dict.get('SLpM') < f2_dict.get('SLpM')):
        fighter2_score += 1
    
    # Higher Significant Strike Accurace is better
    if (f1_dict.get('Str_Acc') > f2_dict.get('Str_Acc')):
        fighter1_score += 1.5
    elif (f1_dict.get('Str_Acc') < f2_dict.get('Str_Acc')):
        fighter2_score += 1.5

    # Lower Significant Strikes Absorbed per minute is better
    if (f1_dict.get('SApM') < f2_dict.get('SApM')):
        fighter1_score += 1.5
    elif (f1_dict.get('SApM') > f2_dict.get('SApM')):
        fighter2_score += 1.5

    # Higher Significant Strike Defence is better
    if (f1_dict.get('Str_Def') > f2_dict.get('Str_Def')):
        fighter1_score += 1
    elif (f1_dict.get('Str_Def') < f2_dict.get('Str_Def')):
        fighter2_score += 1

    # Higher Takedown Average is better
    if (f1_dict.get('TD_Avg') > f2_dict.get('TD_Avg')):
        fighter1_score += 1
    elif (f1_dict.get('TD_Avg') < f2_dict.get('TD_Avg')):
        fighter2_score += 1

    # Higher Takedown Defense is better
    if (f1_dict.get('TD_Def') > f2_dict.get('TD_Def')):
        fighter1_score += 1
    elif (f1_dict.get('TD_Def') < f2_dict.get('TD_Def')):
        fighter2_score += 1


    # Calculate who has the most points if they are tied randomly pick
    if fighter1_score > fighter2_score:
        winner = f1_dict['Name']
        reason = ("By Total Points")
    elif fighter1_score < fighter2_score:
        winner = f2_dict['Name']
        reason = ("By Total Points")
    else:
        winner = random.choice(f1_dict['Name'], f2_dict['Name'])
        reason = ("Scores tied winner picked Randomly")

    return winner, reason

    