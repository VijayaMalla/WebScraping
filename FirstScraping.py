# Import Packages
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

# Download and Parse the HTML
start_url = 'http://books.toscrape.com/index.html'

# Download the HTML from start_url
downloaded_html = requests.get(start_url)

# Parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text, "lxml")

full_list = soup.select('.side_categories ul li ul li')

regex = re.compile(r'\n[ ]*')

book_dict = [{}]
for element in full_list:
    link_text = element.get_text()
    link_text = regex.sub('', link_text)

    anchor_tag = element.select('a')
    fullbooklink = "http://books.toscrape.com/"+anchor_tag[0]['href']

    if (len(link_text) > 0 or len(fullbooklink) > 0):
        book_dict.append({'Category': link_text,
                          'Link': fullbooklink})

# Save a local copy
with open('BookCategoryList', 'w') as file:
    for item in book_dict:
        if (len(item) > 0):
            file.write("%s\n" % item)
