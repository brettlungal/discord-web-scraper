import requests
from bs4 import BeautifulSoup
import config

DEBUGGING = True
#get request and response parsing
x = requests.get('https://www.monster.ca/jobs/search/?q=Software-Developer&where=Manitoba')
soup = BeautifulSoup(x.content,"html.parser")

results = soup.find(id='ResultsContainer')
jobs = results.find_all('section',class_='card-content')

info = ''
for job in jobs:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    
    if None in (title_elem, company_elem, location_elem):
        continue
    info += "```"+title_elem.text.strip()+"\n"+company_elem.text.strip()+"\n"+location_elem.text.strip()+"```\n"


#post for webhook
payload = {
    "username": "Job-Scraper",
    "avatar_url": "https://i.imgur.com/IFPMBBC.jpg",
    "content": info
}
url = ""
if DEBUGGING:
    url = config.TEST_WEBHOOK
else:
    url = config.SEGFAULT_WEBHOOK

resp = requests.post(url,data=payload)

print(resp.text)