from bs4 import BeautifulSoup 
import requests
from csv import writer


url  = "https://www.intelregion.com/category/jobs/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

jobs = soup.find_all('div', class_="td-module-container td-category-pos-above")

with open('jobs_posts.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Date_Posted', 'Link']
    thewriter.writerow(header)
    for job in jobs:
        link = job.find('a',href=True)['href']
        if 'jobs' in link:
            title = job.find('h3', class_="entry-title td-module-title").text
            time_posted = job.find('time', class_="entry-date updated td-module-date").text
            info = [title, time_posted, link]
            thewriter.writerow(info)





    
