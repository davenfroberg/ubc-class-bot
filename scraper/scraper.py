import requests
import json
from bs4 import BeautifulSoup

URL = 'https://wiki.ubc.ca/List_of_UBC_Buildings_with_Classrooms'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find(id="mw-content-text")
rows = table.find_all("tr")
rows.pop(0) #remove title row

buildings = []
for row in rows:
    building = {}
    elements = row.find_all("td")
    building['name'] = (elements[0].text).replace("\n", "")
    building['code'] = (elements[1].text).replace("\n", "")
    building['address'] = (elements[2].text).replace("\n", "")
    buildings.append(building)


buildings_json = json.dumps(buildings)

with open("buildings.json", "w") as outfile:
    outfile.write(buildings_json)