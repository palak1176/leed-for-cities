import requests
from bs4 import BeautifulSoup

# Scrape USGBC cities
response = requests.get("https://www.usgbc.org/leed/rating-systems/leed-for-cities")
soup = BeautifulSoup(response.text, "html.parser")
main = soup.find("div", {"class": "dialog-off-canvas-main-canvas"})
wrapper = main.find("div", {"id": "wrapper"})
cities = wrapper.find_all("li")

# Find all Georgia cities participating in LEED for Cities
georgia_cities = [
    city.get_text(strip=True)
    for city in cities
    if city.get_text(strip=True).endswith(", GA")
]

# Atlanta MSA cities
atlanta_msa_cities = {
    "Acworth", "Adairsville", "Aldora", "Alpharetta", "Atlanta",
    "Auburn", "Austell", "Avondale Estates", "Ball Ground", "Barnesville",
    "Berkeley Lake", "Bethlehem", "Between", "Bostwick", "Bowdon",
    "Braselton", "Braswell", "Bremen", "Brookhaven", "Brooks",
    "Buchanan", "Buckhead", "Buford", "Canton", "Carl",
    "Carrollton", "Cartersville", "Centralhatchee", "Chamblee",
    "Chattahoochee Hills", "Clarkston", "College Park", "Concord",
    "Conyers", "Covington", "Cumming", "Dacula", "Dallas", "Dawsonville", 
    "Decatur", "Doraville", "Douglasville", "Duluth", "Dunwoody", 
    "East Point", "Emerson", "Ephesus", "Euharlee", "Fairburn", 
    "Fayetteville", "Flovilla", "Forest Park", "Franklin", "Goggins", 
    "Milner", "Milton", "Mulberry", "Newnan", "Roswell", "Sandy Springs", 
    "Smyrna", "Snellville", "South Fulton", "Stockbridge", "Stone Mountain", 
    "Stonecrest", "Suwanee", "Tucker", "Union City", "Villa Rica", "Woodstock"
}

# Find MSA cities participating in LEED for Cities
filtered = []

for item in georgia_cities:
    city_name = item.split(",")[0].strip() # Find just the city name (original format: "City, GA")

    if city_name in atlanta_msa_cities:
        filtered.append(item)

# Print results
print("\nMSA cities participating in LEED for Cities:")
for city in filtered:
    print(city)

print(f"Total count: {len(filtered)}\n")
