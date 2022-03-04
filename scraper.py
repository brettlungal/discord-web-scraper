import requests
from bs4 import BeautifulSoup
import config

DEBUGGING = True
#get request and response parsing
x = requests.get('https://ca.indeed.com/jobs?q=Software+Developer&l=Calgary%2C+AB')
soup = BeautifulSoup(x.content,"html.parser")

def extract_job_title_from_result(soup): 
    jobs = []
    for div in soup.find_all(name="div", attrs={'class':"row"}):
      for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
        jobs.append(a["title"])
    return jobs

jobs = extract_job_title_from_result(soup)

print(jobs)
# results = soup.find(id='resultsBody')

# next = results.find(id='mosaic-zone-jobcards')

# jobs = next.find('section',class_='resultContent')
# print(jobs)

# info = ''
# for job in jobs:
#     title_elem = job.find('h2', class_='title')
#     company_elem = job.find('div', class_='company')
#     location_elem = job.find('div', class_='location')
    
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     info += "```"+title_elem.text.strip()+"\n"+company_elem.text.strip()+"\n"+location_elem.text.strip()+"```\n"


# #post for webhook
# payload = {
#     "username": "Job-Scraper",
#     "avatar_url": "https://i.imgur.com/IFPMBBC.jpg",
#     "content": info
# }
# url = ""
# if DEBUGGING:
#     url = config.TEST_WEBHOOK
# else:
#     url = config.SEGFAULT_WEBHOOK

# resp = requests.post(url,data=payload)

# print(resp.text)