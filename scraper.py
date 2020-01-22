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
    elif location & ~job:
        URL = f"https://www.indeed.com.mx/trabajo?q=developer&l={location}"
    elif job & ~location:
        URL = f"https://www.indeed.com.mx/jobs?q={job}&l="
    else: 
        URL = "https://www.indeed.com.mx/jobs?q=&l="

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="resultsCol")
    return results


# def filter_jobs_by_keyword(results, word):
#     """Filters job postings by word and prints matching job title plus link.
#     :param results: Parsed HTML container with all job listings
#     :type results: BeautifulSoup object
#     :param word: keyword to filter by
#     :type word: str
#     :return: None - just meant to print results
#     :rtype: None
#     """
#     filtered_jobs = results.find_all(
#         "h2", string=lambda text: word in text.lower()
#     )
#     for f_job in filtered_jobs:
#         link = f_job.find("a")["href"]
#         print(f_job.text.strip())
#         print(f"Apply here: {link}\n")


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
        link_elem = job_elem.find("a")

        if None in (title_elem, company_elem, location_elem, link_elem):
            continue
            # print(job_elem.prettify())  # to inspect the 'None' element

        print("Vacante " + title_elem.text.strip())
        print("Empresa " + company_elem.text.strip())
        print("Lugar " + location_elem.text.strip())    
    
        print(link_elem["href"])
        print()


# USE THE SCRIPT AS A COMMAND-LINE INTERFACE
# ----------------------------------------------------------------------------
my_parser = argparse.ArgumentParser(
    prog="jobs", description="Find Developer Jobs"
)
my_parser.add_argument(
    "-job", metavar="job", type=str, help="The desired job title"
)
my_parser.add_argument(
    "-location", metavar="location", type=str, help="The location of the job"
)

args = my_parser.parse_args()
job, location = args.job, args.location

results = scrape_jobs(job, location)
# if keyword:
#     filter_jobs_by_keyword(results, keyword.lower())
# else:
#     print_all_jobs(results)
print_all_jobs(results)