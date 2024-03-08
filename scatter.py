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

    # Save the raw HTML data to a file
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print("HTML data has been saved to output.html.")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

# Add a delay to avoid being rate-limited
time.sleep(2)
