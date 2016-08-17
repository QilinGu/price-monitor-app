import re

import requests
from bs4 import BeautifulSoup


def load_price(url, tag_name, query):
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    element = soup.find(tag_name, query)
    string_price = element.text.strip()

    pattern = re.compile("(\d+.\d+)")
    match = pattern.search(string_price)
    return match.group()

item = load_price("http://www.johnlewis.com/apple-ipad-air-2-apple-a8x-ios-9-7-wi-fi-64gb/p1731703?colour=Space%20Grey","span", {"itemprop":"price", "class":"now-price"})
print(item)

item2 = load_price('http://www1.macys.com/shop/product/the-north-face-bombay-jacket?ID=2712651&CategoryID=120',
                   'span', {"class":"singlePrice"})
print(item2)