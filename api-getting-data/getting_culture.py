import json
import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()

api_key = os.getenv("EUROPEANA_API_KEY")

#get data from star wars api
swapi_url = "https://swapi.dev/api/people/1/"
swapi_response = requests.get(swapi_url)
swapi_data = swapi_response.json()

console.print("SWAPI Response:", style="bold cyan")
console.print(swapi_data)
character_name = swapi_data["name"]

#search in europeana
europeana_search_url = "https://api.europeana.eu/record/v2/search.json"
params = {
    "wskey": api_key,
    "query": character_name,
    "rows": 1
}

europeana_response = requests.get(europeana_search_url, params=params)
europeana_data = europeana_response.json()

console.print("\nEuropeana Search Response:", style="bold magenta")
console.print(europeana_data)

#save item info
output_data = {
    "selected_api": "swapi",
    "swapi_item": {
        "name": swapi_data.get("name"),
        "birth_year": swapi_data.get("birth_year"),
        "gender": swapi_data.get("gender"),
        "homeworld": swapi_data.get("homeworld"),
        "url": swapi_data.get("url")
    },
    "europeana_item": None
}

if "items" in europeana_data and len(europeana_data["items"]) > 0:
    item = europeana_data["items"][0]

    output_data["europeana_item"] = {
        "title": item.get("title"),
        "guid": item.get("guid"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider"),
        "country": item.get("country"),
        "edmPreview": item.get("edmPreview")
    }

# save to json
with open("swapi_culture_data.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, indent=4)

console.print("\nData saved to swapi_culture_data.json", style="bold green")
console.print("Full path: " + os.path.abspath("swapi_culture_data.json"), style="bold yellow")