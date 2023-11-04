import requests
from lxml import html

cookies = {}

headers = {
    'authority': 'r6.tracker.network',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_ranked_stats(platform, username):
    response = requests.get(f'https://r6.tracker.network/profile/{platform}/{username}', cookies=cookies, headers=headers)

    if response.status_code != 200:
        return "Profile doesn't exist"

    page = html.fromstring(response.text)

    ranked_stats = {}

    time_played_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/text()')
    wins_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[2]/text()')
    losses_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div[2]/text()')
    matches_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[4]/div[2]/text()')
    deaths_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[5]/div[2]/text()')
    kills_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[6]/div[2]/text()')
    wins_percent_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[7]/div[2]/text()')
    kd_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[8]/div[2]/text()')
    kills_match_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[9]/div[2]/text()')
    kills_min = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[10]/div[2]/text()')
    level_element = page.xpath('//div[@class="trn-defstat__name" and text()="Level"]/following-sibling::div[@class="trn-defstat__value-stylized"]')
    current_rank_element = page.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[1]/svg/g/text[2]/tspan[1]')

    if time_played_element:
        time_played_text = time_played_element[0].strip()
        ranked_stats['Time Played'] = time_played_text

    if wins_element:
        wins_text = wins_element[0].strip()
        ranked_stats['Wins'] = wins_text

    if losses_element:
        losses_text = losses_element[0].strip()
        ranked_stats['Losses'] = losses_text

    if matches_element:
        matches_text = matches_element[0].strip()
        ranked_stats['Matches Played'] = matches_text

    if deaths_element:
        deaths_text = deaths_element[0].strip()
        ranked_stats['Deaths'] = deaths_text

    if kills_element:
        kills_text = kills_element[0].strip()
        ranked_stats['Kills'] = kills_text
        
    if wins_percent_element:
        wins_percent_text = wins_percent_element[0].strip()
        ranked_stats['Win %'] = wins_percent_text
        
    if kd_element:
        kd_text = kd_element[0].strip()
        ranked_stats['K/D'] = kd_text
        
    if kills_match_element:
        kills_match_text = kills_match_element[0].strip()
        ranked_stats['Kills/Match'] = kills_match_text
        
    if kills_min:
        kills_min_text = kills_min[0].strip()
        ranked_stats['Kills/Min'] = kills_min_text

    if current_rank_element:
        current_rank_text = current_rank_element[0].text_content().strip()
        ranked_stats['Current Rank'] = current_rank_text

    if level_element:
        level_text = level_element[0].text_content().strip()
        ranked_stats['Player Level'] = level_text

    return ranked_stats
