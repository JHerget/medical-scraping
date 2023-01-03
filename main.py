from bs4 import BeautifulSoup
import json

with open("config.json", "r") as file:
    config = json.loads(file.read())

with open(config["html_file"], "r") as file:
    html = file.read()

output_file = open(config["output_csv"], "w")
output_file.write("PMID,Title,Authors,Citation,First Author,Journal/Book,Publication Year,Create Date,PMCID,NIHMS ID,DOI")

soup = BeautifulSoup(html, "html.parser")
results = soup.find_all("div", {"class": "docsum-content"})

for result in results:
    citation_data = result.div.find_all("span")

    pmid = result.a["data-article-id"]
    title = result.a.text.strip()
    authors = citation_data[0].text.strip()
    citation = citation_data[2].text.strip()
    print(citation)

output_file.close()