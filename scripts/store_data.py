"""
    Use my WikiScraper class to scrape a bunch of Wikipedia articles and store the text.
    This text file will be used by my ML models.
"""

from wiki_scraper import WikiScraper
from random import random
import time


articles = [
    'https://en.wikipedia.org/wiki/Evolution_of_cetaceans',
    'https://en.wikipedia.org/wiki/Wow%21_signal',
    'https://en.wikipedia.org/wiki/The_Hum',
    'https://en.wikipedia.org/wiki/Semantic_satiation',
    'https://en.wikipedia.org/wiki/Flynn_effect',
    'https://en.wikipedia.org/wiki/Antikythera_mechanism',
    'https://en.wikipedia.org/wiki/Year_10,000_problem'
]

ws = WikiScraper()

for article in articles:
    ws.scrape_page(article)

    # sleep 1 - 2 seconds between requests
    time.sleep(random() + 1)
    
ws.save_to_file('data/text.txt')
