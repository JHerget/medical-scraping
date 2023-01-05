# Data Scraping
Given a search query, format the results of the search (from https://pubmed.ncbi.nlm.nih.gov/) as a .csv file.

### Usage
In the root directory of the project run:
```
pip install -r requirements.txt
```
If that does not work, try the same command but use `pip3` instead.

In `config.json` provide a search query and the location to which you would like the output .csv file to be saved.

Finally, run:
```
python main.py
```
If that does not work, try the same command but use `python3` instead.