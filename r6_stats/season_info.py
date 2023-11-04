import requests
from bs4 import BeautifulSoup as bs

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_season_info(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)
    soup = bs(response.text, 'html.parser')
    
    season_info = {}

    for quickseason in soup.select('.r6-quickseason'):
        label_element = quickseason.select_one('.r6-quickseason__label')
        value_element = quickseason.select_one('.r6-quickseason__value')
        matches_element = quickseason.select_one('.r6-quickseason__value.trn-text--dimmed')
        kd_elements = quickseason.select('small.r6-quickseason__value.trn-text--dimmed')

        if label_element and value_element and matches_element and len(kd_elements) >= 3:
            label = label_element.text.strip()
            value = value_element.text.strip()
            matches = matches_element.text.strip()
            kd = kd_elements[2].text.strip()

            if label and value and matches and kd:
                season_info[label] = {
                    'MMR': value,
                    'Matches': matches,
                    'KD': kd
                }

    return season_info
