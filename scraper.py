import requests
from bs4 import BeautifulSoup

# Variables que se pasarán como argumentos en la CLI
job_description = 'chef'
place = 'Arizona'
keyword = ''
URL = f"https://www.monster.com/jobs/search/?q={job_description}&where={place}"
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
key_job_elems = results.find_all('h2', string=lambda text: keyword in text.lower())

#print(len(key_job_elems))

if len(keyword) > 0:
    for key_job_elem in key_job_elems:

        key_title_elem = key_job_elem.find('h2', class_='title')
        key_company_elem = key_job_elem.find('div', class_='company')
        key_location_elem = key_job_elem.find('div', class_='location')
        if None in (key_title_elem, key_company_elem, key_location_elem):
            continue

        print(key_title_elem.text.strip())
        print(key_company_elem.text.strip())
        print(key_location_elem.text.strip())
        print()
else:

    for job_elem in job_elems:

        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        link = job_elem.find('a')['href']

        if None in (title_elem, company_elem, location_elem, link):
            continue


        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print(f"Apply here: {link}\n")
        print()
    
