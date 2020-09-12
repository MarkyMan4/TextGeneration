"""
    This class can be used to get text from Wikipedia articles
    i.e. anything inside of p tags
"""

import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import re


class WikiScraper:
    def __init__(self):
        self.text = []

    def get_text(self):
        return self.text

    # scrape a Wikipedia page and store each sentence as an element in an array
    def scrape_page(self, url):
        r = requests.get(url)
        html = r.text

        soup = BeautifulSoup(html, features='html.parser')
        paragraphs = soup.find_all('p')

        for p in paragraphs:
            # tokenize paragraphs as sentences so each line can be a sentence
            sentences = sent_tokenize(p.text)

            for s in sentences:
                # remove citations
                s = re.sub('\[.+\]', '', s)

                # remove blank spaces at beginning of lines
                s = re.sub('^\s+', '', s)

                # remove punctuation
                s = re.sub('(\.|\!|\?|\,)', '', s)

                # only save if s isn't an empty string
                if len(s) > 0:
                    self.text.append(s)

    # Save the text to a file. Each sentence is one line in the file
    def save_to_file(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            for t in self.text:
                f.write(t)
                f.write('\n')
