#!/usr/bin/python3

import requests
import re
import sys

# Params
seed = sys.argv[1]
langage = 'en'
search_depth = int(sys.argv[2])

# Header
print('WikiRelations.', file=sys.stderr)
print(f'Starting from {seed} :', file=sys.stderr)

# Array that store egdes for the graph
edges = []

# Setup requests
s = requests.Session()
url = f"https://{langage}.wikipedia.org/w/api.php"

# Get links from a wiki page
def get_links(title, depth):
    
    msg = ('    ') * (search_depth - depth)
    msg += '├── ' + title
    print(msg, file=sys.stderr)

    # Call the API to retrieve all the links in the page
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": "max"
    }
    response = s.get(url=url, params=params)
    data = response.json()
    pages = data["query"]["pages"]
    links = []

    # Parse the response and return empty array if no page found
    try:
        for key, val in pages.items():
            for link in val["links"]:
                links.append(link["title"])
    except KeyError:
        return []
    
    # Keep calling the API if links are missing
    while "continue" in data:
        plcontinue = data["continue"]["plcontinue"]
        params["plcontinue"] = plcontinue

        response = s.get(url=url, params=params)
        data = response.json()
        pages = data["query"]["pages"]

        for key, val in pages.items():
            for link in val["links"]:
                links.append(link["title"])

    # Remove links that are in the footer of the page
    footer_nb = 0
    for i in reversed(links):
        if ':' in i:
            footer_nb += 1
        else:
            break
    links = links[:len(links) - footer_nb]
    
    # Remove links that has number to remove dates and unrelevant duplicates
    regex = re.compile(r'[0-9]')
    links = [i for i in links if not any(char.isdigit() for char in i)]


    # Add new edges and call recursively on the links
    end = depth == 1
    for link in links:
        edges.append((title, link))
        if not end:
            get_links(link, depth - 1)

# First call to parse from the seed page
get_links(seed, search_depth)

# Print in a CSV format the edges of the graph produced
for edge in edges:
    print(f"{edge[0].replace(';', ',')};{edge[1].replace(';', ',')}")

