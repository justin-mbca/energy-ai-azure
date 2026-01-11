import requests
from bs4 import BeautifulSoup
import re

def scrape_eia_reports():
    url = 'https://www.eia.gov/petroleum/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    texts = []
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if len(text) > 50:
            texts.append(text)
    return texts

def scrape_wikipedia_energy():
    url = 'https://en.wikipedia.org/wiki/Oil_production'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    texts = []
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if len(text) > 50:
            texts.append(text)
    return texts

if __name__ == "__main__":
    eia = scrape_eia_reports()
    wiki = scrape_wikipedia_energy()
    with open('energy_text.txt', 'w') as f:
        for line in eia + wiki:
            f.write(line + '\n')
