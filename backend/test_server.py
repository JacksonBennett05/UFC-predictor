import requests

BASE_URL = "http://127.0.0.1:5000"

def test_fighters_search():
    search_query = "John"  # Replace with a name or partial name from your dataset
    response = requests.get(f"{BASE_URL}/fighters", params={"search": search_query})
    print("Search Fighters Response:", response.json())

def test_simulate_fight():
    payload = {
        "fighter1": "John Adajar",  # Replace with actual fighter names from your dataset
        "fighter2": "John Albert"
    }
    response = requests.post(f"{BASE_URL}/simulate", json=payload)
    print("Simulate Fight Response:", response.json())

if __name__ == "__main__":
    print("Testing /fighters endpoint...")
    test_fighters_search()

    print("\nTesting /simulate endpoint...")
    test_simulate_fight()