
import requests
import csv
import datetime
from bs4 import BeautifulSoup


url = "http://store.steampowered.com/search/?filter=topsellers"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

now = datetime.datetime.now()
name = now.strftime('%m/%d/%Y') + '.csv'
name = name.replace("/", ",")
print(name)
csv_file = open(name, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title','release date', 'review', 'discount'])

for game in soup.find_all('div', class_='responsive_search_name_combined'):

	title = game.find('span', class_="title").text
	release_date = game.find('div', class_="col search_released responsive_secondrow").text	
	discount = game.find('div', class_="col search_discount responsive_secondrow").text

	try:
		review = game.find('div',"col search_reviewscore responsive_secondrow")
		review = review.span['data-store-tooltip']
	except Exception as e:
		review = "none"
	csv_writer.writerow([title, release_date, review, discount])


csv_file.close()
