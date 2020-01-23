from setuptools import setup

setup(
    name='scraper',
    version='0.0.1',
    description='Job searcher',
    py_modules=['scrape_jobs', 'print_all_jobs', 'prueba'],
    package_dir={'': 'src'},
    clasiffiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: MIT License"
    ],
)
