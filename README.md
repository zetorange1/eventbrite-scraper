# Eventbrite Scraper

A Python 3+ scraper that pulls USA event data from Eventbrite. The data is stored into csv.

### Installation

1. Clone the repository
2. `pip install -r requirements.txt`

### Usage

To use, you will need to specify a category, a city, and a two letter USA state abbreviation. 

For example: `python main.py music altlanta ga`.


**Optional Parameters**

- *number* - You can specify the number of events -- 10 is the default -- with the optional `-n` parameter: `python main.py music chicago il -n 40`.

