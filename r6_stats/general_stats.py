import requests
from lxml import html

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_general_stats(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)

    if response.status_code != 200:
        return "Profile doesn't exist"

    page = html.fromstring(response.text)

    stats = {}

    headshot_percent_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]')
    kd_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]')
    kills_element = page.xpath('//div[@class="trn-defstat__name" and contains(text(), "Kills")]/following-sibling::div[@class="trn-defstat__value"]')
    deaths_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/text()')
    wins_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/text()')
    losses_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/text()')
    win_percentage_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[6]/div[2]')
    time_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[7]/div[2]/text()')
    matches_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[8]/div[2]/text()')
    level_element = page.xpath('//div[@class="trn-defstat__name" and text()="Level"]/following-sibling::div[@class="trn-defstat__value-stylized"]')

    if headshot_percent_element:
        headshot_percent_text = headshot_percent_element[0].text_content().strip()
        stats['Headshot %'] = headshot_percent_text
    
    if kd_element:
        kd_text = kd_element[0].text_content().strip()
        stats['K/D'] = kd_text

    if kills_element:
        kills_text = kills_element[0].text_content().strip()
        stats['Kills'] = kills_text

    if deaths_element:
        deaths_text = deaths_element[0].strip()
        stats['Deaths'] = deaths_text

    if wins_element:
        wins_text = wins_element[0].strip()
        stats['Wins'] = wins_text

    if losses_element:
        losses_text = losses_element[0].strip()
        stats['Losses'] = losses_text

    if win_percentage_element:
        win_percentage_text = win_percentage_element[0].text_content().strip()
        stats['Win %'] = win_percentage_text

    if time_element:
        time_text = time_element[0].strip()
        stats['Time Played'] = time_text

    if matches_element:
        matches_text = matches_element[0].strip()
        stats['Matches Played'] = matches_text

    if level_element:
        level_text = level_element[0].text_content().strip()
        stats['Player Level'] = level_text

    return stats
