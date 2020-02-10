#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Collect data from top news websites
page = requests.get('https://ns7.tv/ta')

soup = BeautifulSoup(page.text, 'html.parser')
translator = Translator()

list_text = soup.find_all(class_='headlinecard')

for s in list_text:
    time_of_news = s.find(class_='clockico')
    if not("day" or "days" or "week") in time_of_news.text.strip():
        news = s.find('p')
        news_translated = translator.translate(news.text.encode("utf-8"))
        print ("{} published {}".format(news_translated.text.strip(), time_of_news.text.strip()))