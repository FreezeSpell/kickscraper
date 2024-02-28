# :grin: README.md

## :exclamation: Intro:
This project is a web scraper that extracts data from Kickstarter campaigns. It is designed to gather specific information from large Kickstarter datasets and store it in a structured format for further analysis.

## :open_file_folder: Tech Stack:
The project is built using the following technologies:
- Python: The programming language used for the scraper.
- Pandas: A Python library for data manipulation and analysis.

## :pushpin: Features:
The web scraper has the following features:
- Extracts data from large JSON files based on specified criteria.
- Stores the extracted data in a CSV file for easy analysis.
- Outputs the data in a nicely formatted console message, along with the CSV file.

## :chart_with_upwards_trend: Process:
I started this project as a novice in Python, which was noticable from my code. It was inefficient, yes, but mostly messy and unorganised. After I finished the basic CLI app, I put
this project down for a while, and only came back to it after having gained significantly more insight into programming and Python in general. Most (if not all) code is now properly
formatted and documented, which took a while. Most of the code has been completely rewritten as it was simply too messy or slow.

However, writing this scraper has given me significant understanding of data analysis, and the Pandas package in specific. I am now confident with this package and look forward to using it in future projects.

## :mortar_board: Learnings:
During the development of this project, the following key learnings were gained:
- Understanding large-scale data handling;
- Working with and learning the Pandas library;
- Getting used to best practices in regards to data analysis;
- Working with and learning the JSON library;
- Learning algorithmic efficiency to optimise scraping times.

## :sparkles: Improvement:
Some potential areas for improvement in the project include:
- Enhancing error handling and logging to handle edge cases and exceptions.
- Implementing a user-friendly command-line interface for easier usage.
- Adding support for scraping straight from websites using BeautifulSoup.

## :rocket: Running the project:
(Make sure you have Python and Git installed)
To run the project, follow these steps:
1. Clone the repository from GitHub: `git clone https://github.com/freezespell/special-octo-barnacle.git`
2. Install the required dependencies: `pip install -r requirements.txt` 
3. Navigate to the `Scraper` directory: `cd special-octo-barnacle/Scraper`
4. Modify the scraper configuration in `config.py` to specify the target website and data extraction criteria.
5. Run the scraper: `python main.py`
6. The extracted data will be stored in a CSV file named `output.csv`.

<!-- TODO: add a `config.py` -->
<!-- TODO: output to JSON or CSV? -->

