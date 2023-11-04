import requests
from bs4 import BeautifulSoup as bs

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_player_stats(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)
    soup = bs(response.text, 'html.parser')

    stats = {}

    for defstat in soup.select('.trn-defstat'):
        name_element = defstat.select_one('.trn-defstat__name')
        value_element = defstat.select_one('.trn-defstat__value')

        if name_element and value_element:
            name = name_element.text.strip()
            value = value_element.text.strip()
            if name and value:
                stats[name] = value

    return stats
