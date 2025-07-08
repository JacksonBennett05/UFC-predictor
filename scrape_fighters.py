import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://ufcstats.com/statistics/fighters?char={}&page=all"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_fighter_links(letter):
    url = BASE_URL.format(letter)
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Collect all fighter profile links
    links = soup.select("td.b-statistics__table-col a")
    hrefs = [link['href'] for link in links]

    # Remove duplicates by converting to set
    unique_hrefs = list(set(hrefs))
    return unique_hrefs

def parse_fighter(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    name = soup.find('span', class_='b-content__title-highlight').text.strip()

    stat_dict = {}

    record_span = soup.find('span', class_='b-content__title-record')
    if record_span:
        record_text = record_span.get_text(strip=True).replace("Record:", "").strip()
        parts = record_text.split('-')
        if len(parts) == 3:
            stat_dict['Wins'] = parts[0]
            stat_dict['Losses'] = parts[1]
            stat_dict['Draws'] = parts[2]
        elif len(parts) == 2:
            stat_dict['Wins'] = parts[0]
            stat_dict['Losses'] = parts[1]
            stat_dict['Draws'] = "0"  # default if missing


    stats = soup.find_all('li', class_='b-list__box-list-item')
    
    for stat in stats:
        text = stat.get_text(strip=True)
        if "Age:" in text:
            stat_dict['Age'] = text.replace("Age:", "").strip()
        elif "Height:" in text:
            stat_dict['Height'] = text.replace("Height:", "").strip()
        elif "Reach:" in text:
            stat_dict['Reach'] = text.replace("Reach:", "").strip()

    return {
        'Name': name,
        'Age': stat_dict.get('Age'),
        'Height': stat_dict.get('Height'),
        'Reach': stat_dict.get('Reach'),
        'Wins': stat_dict.get('Wins'),
        'Losses': stat_dict.get('Losses'),
        'Draws' : stat_dict.get('Draws'),
    }

def scrape_all_fighters():
    all_fighters = []
    for letter in 'Q':
        print(f"Scraping fighters starting with '{letter}'...")
        links = get_fighter_links(letter)
        for link in links:
            try:
                fighter = parse_fighter(link)
                all_fighters.append(fighter)
                print(f" Fetched: {fighter['Name']}")
                time.sleep(0.5) #to not kill the server
            except Exception as e:
                print(f"Failed to scrape {link}: {e}")
    return all_fighters

if __name__ == "__main__":
    fighters = scrape_all_fighters()
    df = pd.DataFrame(fighters)
    df.to_csv("fighters.csv", index=False)
    print(f"Saved {len(df)} fighters to fighters.csv")

