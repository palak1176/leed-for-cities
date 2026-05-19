# LEED for Cities – Atlanta MSA Scraper
This script scrapes data from the U.S. Green Building Council (USGBC) LEED for Cities webpage and identifies Georgia cities participating in the program. It then filters those cities to return only those located within the Atlanta Metropolitan Statistical Area (MSA).

What it does:
- Sends a request to the USGBC LEED for Cities webpage
- Parses the HTML using BeautifulSoup
- Extracts a list of cities participating in LEED for Cities
- Filters results to include only cities located in Georgia (", GA")
- Compares them against a predefined set of Atlanta MSA cities

Outputs:
- A list of matching Atlanta MSA cities participating in LEED for Cities
- The total count of matched cities
  
Technologies used:
- Python
- requests (for HTTP requests)
- BeautifulSoup from bs4 (for HTML parsing)
