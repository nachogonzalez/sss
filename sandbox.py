import requests
from bs4 import BeautifulSoup

def get_current_opportunities(url):
    try:
        # Send a GET request to the page
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the section containing opportunities (adjust selectors as needed)
        opportunities = []
        for item in soup.select('.opportunity-item'):  # Replace with actual class or tag
            title = item.select_one('.opportunity-title').get_text(strip=True)  # Replace with actual class or tag
            link = item.select_one('a')['href']
            opportunities.append({'title': title, 'link': link})

        return opportunities

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    url = "https://www.ncia.nato.int/business/procurement/current-opportunities"
    opportunities = get_current_opportunities(url)
    for opp in opportunities:
        print(f"Title: {opp['title']}, Link: {opp['link']}")