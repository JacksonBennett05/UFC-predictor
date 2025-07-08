import csv

def load_fighter_data(filepath='data/fighters_cleaned.csv') -> dict:
    fighters = {}
    try:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fighters[row["Name"]] = {
                    "Name": row["Name"],
                    "Age": int(row["Age"]),
                    "Height": int(row["Height"]),
                    "Reach": int(row["Reach"]),
                    "Wins": int(row["Wins"]),
                    "Losses": int(row["Losses"]),
                }
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
    
    return fighters