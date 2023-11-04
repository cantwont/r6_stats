import requests
import re
from bs4 import BeautifulSoup as bs

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_profile_views(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)
    soup = bs(response.text, 'html.parser')
    try:
        profile_views_span = soup.find('span', class_='trn-profile-header__views trn-text--dimmed')
        text = profile_views_span.get_text()
        profile_views = re.search(r'\d[\d,]+', text)

        if profile_views:
            profile_views = profile_views.group(0).replace(',', '')
            return profile_views
        else:
            return "Profile/Element does not exist"
    except Exception:
        return "An error occurred while retrieving the profile views"
