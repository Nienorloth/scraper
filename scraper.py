import requests
from bs4 import BeautifulSoup

<<<<<<< HEAD
# Variables que se pasarán como argumentos en la CLI
job_description = 'chef'
place = 'Arizona'
keyword = ''
URL = f"https://www.monster.com/jobs/search/?q={job_description}&where={place}"
=======
# Variables que se pasaran como argumentos en la CLI
job_description = 'developer'
place = 'Australia'
keyword = 'Python'
URL = 'https://www.monster.com/jobs/search/?q={}&where={}'.format(job_description, place)
>>>>>>> 5a0f73471a7d486a0996dbc34ad8aea127d4b951
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


###########################################################
#    indeed

URL = 'https://www.indeed.com.mx/jobs?q=devops&l=Chihuahua%2C+Chih.'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="resultsCol")

#print(results.prettify())
# el cdigo imprime el html

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    title_elem = job_elem.find('a', class_="jobtitle turnstileLink")
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find('span', class_='location')

    if None in (title_elem, company_elem, location_elem):
            continue

    print("Vacante " + title_elem.text.strip())
    print("Empresa " + company_elem.text.strip())
    print("Lugar " + location_elem.text.strip())
