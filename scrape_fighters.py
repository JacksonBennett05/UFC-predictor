import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


BASE_URL = "http://ufcstats.com/statistics/fighters?char={}&page=all"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def height_to_inches(height_str):
    """
    Convert height string like "5' 11\"" or "6' 0\"" to total inches as int.
    Returns None if format unexpected.
    """
    match = re.match(r"(\d+)'\s*(\d+)\"", height_str)
    if match:
        feet = int(match.group(1))
        inches = int(match.group(2))
        return feet * 12 + inches
    else:
        return None   
    
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

def extract_stat_from_li(li_tag):
    label_tag = li_tag.find('i', class_='b-list__box-item-title')
    if label_tag is None:
        return None, None
    label = label_tag.get_text(strip=True).rstrip(':')  # e.g. 'SLpM'
    label_tag.extract()  # remove label <i> tag
    value = li_tag.get_text(strip=True)  # what's left is value
    return label, value

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
    else:
        stat_dict['Wins'] = stat_dict['Losses'] = stat_dict['Draws'] = "0"

    # Grab all the stats <li> tags
    stats = soup.find_all('li', class_='b-list__box-list-item')

    # Map labels to keys you want
    for li in stats:
        label, value = extract_stat_from_li(li)
        if label is None:
            continue
        # Normalize labels as needed
        if label == "Age":
            stat_dict['Age'] = value
        elif label == "Height":
            stat_dict['Height'] = value
        elif label == "Reach":
            stat_dict['Reach'] = value
        elif label == "SLpM":
            stat_dict['SLpM'] = value
        elif label == "Str. Acc.":
            stat_dict['Str_Acc'] = value
        elif label == "SApM":
            stat_dict['SApM'] = value
        elif label == "Str. Def.":
            stat_dict['Str_Def'] = value
        elif label == "TD Avg.":
            stat_dict['TD_Avg'] = value
        elif label == "TD Acc.":
            stat_dict['TD_Acc'] = value
        elif label == "TD Def.":
            stat_dict['TD_Def'] = value
        elif label == "Sub. Avg.":
            stat_dict['Sub_Avg'] = value

    if 'Height' in stat_dict:
        height_inches = height_to_inches(stat_dict['Height'])
        stat_dict['Height'] = height_inches
    else:
        stat_dict['Height'] = None

    return {'Name': name, **stat_dict}

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