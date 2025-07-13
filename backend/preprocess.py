import csv

# Loads fighter data from a CSV into a dict with typed fields for easy access.
# Handles missing or invalid data gracefully.

def load_fighter_data(filepath='fighters.csv') -> dict:
    fighters = {}
    try:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                fighters[row["Name"]] = {
                    "Name": row["Name"],
                    "Height": float(row["Height"]) if row["Height"] else None,
                    "Reach": int(row["Reach"].replace('"', '').strip()) if row["Reach"] != '--' else None,
                    "Wins": int(row["Wins"]),
                    # "Draws": int(row["Draws"]),
                    "Losses": int(row["Losses"]),
                    "SLpM": float(row["SLpM"]),
                    "Str_Acc": int(row["Str_Acc"].replace('%', '').strip()),
                    "Str_Def": int(row["Str_Def"].replace('%','').strip()),
                    "SApM": float(row["SApM"]),
                    "TD_Avg": float(row["TD_Avg"]),
                    "TD_Def": int(row["TD_Def"].replace('%','').strip()),
                    "Sub_Avg": float(row["Sub_Avg"])
                }
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error loading data: {e}")
    
    return fighters