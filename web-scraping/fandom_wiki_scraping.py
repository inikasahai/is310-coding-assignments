import csv
import cloudscraper
from bs4 import BeautifulSoup

url = "https://scoobydoo.fandom.com/wiki/Category:Characters"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

data = []

for link in links:
    name = link.get_text(strip=True)
    href = link.get("href")

    if name != "" and href is not None:
        if "/wiki/" in href:
            if href.startswith("/wiki/"):
                full_link = "https://scoobydoo.fandom.com" + href
            else:
                full_link = href

            data.append([name, full_link])

clean_data = []
seen = set()

for row in data:
    if tuple(row) not in seen:
        seen.add(tuple(row))
        clean_data.append(row)

with open("scoobydoo_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Character Name", "Link"])

    for row in clean_data:
        writer.writerow(row)

print("Scraping complete!")
print("Data saved to scoobydoo_data.csv")