from bs4 import BeautifulSoup
from datetime import datetime as dt
import json
import requests
import urllib.parse

with open("config.json", "r") as file:
    config = json.loads(file.read())

print("Searching for results...")
search_results = requests.get(f"https://pubmed.ncbi.nlm.nih.gov/?term={urllib.parse.quote(config['search_query'])}&size=200")

output_file = open(config["output_csv"], "w+")
output_file.write("PMID,Title,Authors,Citation,First Author,Journal/Book,Publication Year,Create Date,DOI\n")

soup = BeautifulSoup(search_results.text, "html.parser")
results = soup.find_all("div", {"class": "docsum-content"})

print("Parsing results...")
for result in results:
    citation_data = result.div.find_all("span")

    pmid = result.a["data-article-id"]
    title = result.a.text.strip().replace("\n", "")
    authors = citation_data[0].text.strip().replace("\n", "")
    citation = citation_data[2].text.strip().replace("\n", "")
    first_author = authors.split(",")[0]
    journal_book = citation.split(".")[0]
    publication_year = citation_data[3].text.split(".")[1]
    create_date = citation.split(";")[0].split(". ")[1]
    doi = citation.split("doi: ")[1].split(" ")[0][:-1]

    try:
        create_date = dt.strptime(create_date, "%Y %b %d").strftime("%m/%d/%Y")
    except:
        create_date = dt.strptime(create_date, "%Y %b").strftime("%m/%Y")

    output_file.write(f'"{pmid}","{title}","{authors}","{citation}","{first_author}","{journal_book}","{publication_year}","{create_date}","{doi}"\n')

print("Complete!")

output_file.close()