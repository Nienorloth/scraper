import requests
from bs4 import BeautifulSoup
import argparse


def scrape_jobs(job=None, location=None):
    """Scrapes job postings from indeed, optionally by job and location.
    :param job: job title
    :param location: Where the job is located
    :type location: str
    :type job: str
    :return: all job postings from first page that match the search results
    :rtype: BeautifulSoup object
    """
    if location and job:
        URL = f"https://www.indeed.com.mx/jobs?q={job}&l={location}"
    elif location and not job:
        URL = f"https://www.indeed.com.mx/trabajo?q=developer&l={location}"
    elif job and not location:
        URL = f"https://www.indeed.com.mx/jobs?q={job}&l="
    elif not job and not location:
        URL = "https://www.indeed.com.mx/jobs?q=&l="

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="resultsCol")
    return results


def print_all_jobs(results):
    """Print details of all jobs returned by the search.
    The printed details are title, link, company name and location of the job.
    :param results: Parsed HTML container with all job listings
    :type results: BeautifulSoup object
    :return: None - just meant to print results
    :rtype: None
    """
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

    for job_elem in job_elems:
        title_elem = job_elem.find('a', class_="jobtitle turnstileLink")
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('span', class_='location')
        link_cont_elem = job_elem.find('div', class_='title')

        if None in (title_elem, company_elem, location_elem):
            continue
            # print(job_elem.prettify())  # to inspect the 'None' element

        print("Vacante" + title_elem.text.strip())
        link_elem = link_cont_elem.find("a")
        print("Empresa " + company_elem.text.strip())
        print("Lugar " + location_elem.text.strip())
        print("https://www.indeed.com.mx" + link_elem["href"])
        print()


# USE THE SCRIPT AS A COMMAND-LINE INTERFACE
# ----------------------------------------------------------------------------
my_parser = argparse.ArgumentParser(
    prog="jobs web-scraper", description="Web-scraping tool for job search", epilog="Good luck with the search!"
)
my_parser.add_argument(
    "-job", metavar="job", type=str, help="A keyword to look for the desired job"
)
my_parser.add_argument(
    "-location", metavar="location", type=str, help="The location of the job"
)

args = my_parser.parse_args()
job, location = args.job, args.location

results = scrape_jobs(job, location)

if not results:
    print("Ingresa los datos para tu búsqueda (-job, -location)")
else:
    print_all_jobs(results)
