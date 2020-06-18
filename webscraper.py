import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=united-states'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

#print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2',
                                string=lambda text: 'python' in text.lower())

#For all jobs on the page, returns: title, comapny, location.
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
    
#For all jobs with python on title returns, title & hyperlink.
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print()
    print(f"Apply here: {link}\n")
