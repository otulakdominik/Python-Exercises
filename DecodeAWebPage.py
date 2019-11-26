import requests
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
ttl_lst = []

soup = BeautifulSoup(page.content, 'html.parser')
artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
