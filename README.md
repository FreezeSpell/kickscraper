# README.md

## Intro:
This project is a web scraper that extracts data from Kickstarter campaigns. It is designed to gather specific information from large Kickstarter datasets and store it in a structured format for further analysis.

## Tech Stack:
The project is built using the following technologies:
- Python: The programming language used for the scraper.
- Pandas: A Python library for data manipulation and analysis.

## Features:
The web scraper has the following features:
- Extracts data from target websites based on specified criteria.
- Stores the extracted data in a CSV file for easy analysis.
- Supports parallel processing for faster scraping.

## Process:
The scraper follows the following process:
1. Fetches the HTML content of the target website using the Requests library.
2. Parses the HTML content using BeautifulSoup to extract relevant data.
3. Applies filters and criteria to extract specific information.
4. Stores the extracted data in a CSV file using the Pandas library.

## Learnings:
During the development of this project, the following key learnings were gained:
- Understanding of web scraping techniques and best practices.
- Familiarity with HTML parsing and data extraction using BeautifulSoup.
- Knowledge of handling HTTP requests and responses using the Requests library.
- Experience in working with data manipulation and analysis using Pandas.

## Improvement:
Some potential areas for improvement in the project include:
- Enhancing error handling and logging to handle edge cases and exceptions.
- Implementing a user-friendly command-line interface for easier usage.
- Adding support for scraping dynamic websites using tools like Selenium.

## Running the project:
To run the project, follow these steps:
1. Clone the repository from GitHub: `git clone https://github.com/freezespell/special-octo-barnacle.git`
2. Install the required dependencies: `pip install -r requirements.txt` 
3. Navigate to the `Scraper` directory: `cd special-octo-barnacle/Scraper`
4. Modify the scraper configuration in `config.py` to specify the target website and data extraction criteria.
5. Run the scraper: `python scraper.py`
6. The extracted data will be stored in a CSV file named `output.csv`.

<!-- TODO: add a `config.py` -->
<!-- TODO: output to JSON or CSV? -->

