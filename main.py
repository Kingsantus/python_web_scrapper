# module to be imported
from bs4 import BeautifulSoup 
import requests
from csv import writer

# establishing the url you want to scrap
url  = "https://www.intelregion.com/category/jobs/"

# assign the url to requests module to fetch the site
page = requests.get(url)

#use beautifulSoup to view only the html property of the site
soup = BeautifulSoup(page.content, 'html.parser')

#find a common div for what you want to scrap
jobs = soup.find_all('div', class_="td-module-container td-category-pos-above")

#initiate the csv file to be able to read, write and create
with open('jobs_posts.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Date_Posted', 'Link']
    thewriter.writerow(header)
    #getting everything you want from the common div
    for job in jobs:
        link = job.find('a',href=True)['href']
        if 'jobs' in link:
            title = job.find('h3', class_="entry-title td-module-title").text
            time_posted = job.find('time', class_="entry-date updated td-module-date").text
            info = [title, time_posted, link]
            thewriter.writerow(info)





    
