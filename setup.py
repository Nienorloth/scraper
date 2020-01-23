from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='scraper',
    version='0.0.1',
    description='Job searcher',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['scrape_jobs', 'print_all_jobs', 'prueba'],
    package_dir={'': 'src'},
    url='https://github.com/Nienorloth/scraper',
    clasiffiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: MIT License"
    ],
    )
