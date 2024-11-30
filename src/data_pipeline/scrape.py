from bs4 import BeautifulSoup
import requests

def scrape_fashion_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = [img["src"] for img in soup.find_all("img") if "fashion" in img["src"]]
    return images
