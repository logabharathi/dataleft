import requests
from bs4 import BeautifulSoup

# Collect data from top news websites
page = requests.get('https://ns7.tv/ta')

soup = BeautifulSoup(page.text, 'html.parser')

list_text = soup.find(class_='head_news todaynews')

print(list_text)
