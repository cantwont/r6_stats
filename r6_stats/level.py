import requests
from lxml import html

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_profile_level(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)

    if response.status_code != 200:
        return "Failed to retrieve the page"

    page = html.fromstring(response.text)

    level_element = page.xpath('//div[@class="trn-defstat__name" and text()="Level"]/following-sibling::div[@class="trn-defstat__value-stylized"]')

    if level_element:
        level = level_element[0].text_content().strip()
        return level
    
    return "Level not found"
