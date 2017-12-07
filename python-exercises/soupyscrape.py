import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/?mcubz=1'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml')
for link in soup.find_all('story-heading'):
	print(link)