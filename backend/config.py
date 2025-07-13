# Weights for each stat in the prediction scoring
STAT_WEIGHTS = {
    "Reach": 1.0,
    "Height": 0.5,
    "Wins": 3.0,
    "Losses": -2.0,  # Negative weight because more losses are bad
    "Draws": 0.0,    # Usually neutral but can be adjusted
    "SLpM": 1.5,     # Significant strikes landed per minute
    "Str_Acc": 1.5,  # Significant strike accuracy (%)
    "SApM": -1.5,    # Significant strikes absorbed per minute (negative weight)
    "Str_Def": 1.0,  # Significant strike defense (%)
    "TD_Avg": 1.0,   # Average takedowns landed per 15 min
    "TD_Acc": 1.0,   # Takedown accuracy (%)
    "TD_Def": 1.0,   # Takedown defense (%)
    "Sub_Avg": 0.5,  # Average submissions attempted per 15 min
    "Age": -0.2      # Older fighters might get a slight negative weight
}
