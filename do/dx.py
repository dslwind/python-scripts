import requests
from bs4 import BeautifulSoup

htmlfile = open('1.html', 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'lxml')

titles = soup.select('div.search-inaccount-title')
urls = [i['data-url'] for i in titles]