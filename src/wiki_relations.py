import requests
import re

# Params
seed = 'Albert Einstein'
langage = 'en'

# Header
print('WikiRelations.')
print(f'Starting from {seed} :')

# Setup requests
s = requests.Session()
url = f"https://{langage}.wikipedia.org/w/api.php"

# Get links from a wiki page
def get_links(title):
    
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

    # Remove links that are are in the footer of the page
    footer_nb = 0
    for i in reversed(links):
        if  ':' in i:
            footer_nb += 1
        else:
            break
    links = links[:len(links) - footer_nb]
    
    # Remove links that ends by a number to remove dates
    regex = re.compile(r'[0-9]*$')
    links = [i for i in links if not regex.match(i)]

    return links

for i in get_links(seed):
    print(i)