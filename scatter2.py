import requests
from bs4 import BeautifulSoup
import time

url = "https://www.overbuff.com/heroes?platform=pc&timeWindow=month"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant elements
    hero_div = soup.find('div', class_='relative shadow shadow-dark overflow-hidden w-8 h-8 rounded-lg sm:w-12 sm:h-12')

    if hero_div:
        name = hero_div.find('a', class_='font-semibold uppercase whitespace-nowrap')
        name = name.text.strip() if name else "Name not found"

        stats_div = hero_div.find_next('div', class_='hidden sm:block')

        pick_rate_elem = stats_div.find('td', class_='py-2 px-2 sm:first:px-4 sm:last:px-4').find('span')
        pick_rate = pick_rate_elem.text.strip() if pick_rate_elem else "Pick rate not found"

        win_rate_elem = stats_div.find_all('td', class_='py-2 px-2 sm:first:px-4 sm:last:px-4')[1].find('span')
        win_rate = win_rate_elem.text.strip() if win_rate_elem else "Win rate not found"

        # Display the extracted data
        print(f"Name: {name}")
        print(f"Pick Rate: {pick_rate}")
        print(f"Win Rate: {win_rate}")
    else:
        print("Hero data not found on the page.")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

# Add a delay to avoid being rate-limited
time.sleep(2)
