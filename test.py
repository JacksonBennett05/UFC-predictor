from backend.preprocess import load_fighter_data

# Load the data
fighters = load_fighter_data("fighters.csv")

# Print how many fighters were loaded
print(f"Loaded {len(fighters)} fighters.")

# Print first 3 entries to manually check
for i, (name, data) in enumerate(fighters.items()):
    print(f"{name}: {data}")
    if i == 2:
        break

