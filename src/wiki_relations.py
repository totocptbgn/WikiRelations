import wikipediaapi as wikiapi

# Params
seed = 'Oscar Isaac'
langage = 'fr'

wiki = wikiapi.Wikipedia(langage)
p = wiki.page(seed)

# Header
print('WikiRelations.')
print(f'Starting from {seed} ({p.fullurl})\n')

# Get links from a wiki page
def get_links(page):

    print(f'Number of links : {len(page.links)}')

    for l in page.links:

        # Remove links outside
        if ':' in l:
            continue
        
        # Remove links with number
        if any(char.isdigit() for char in l):
            continue
        
        # Get page (Cost too much...)
        pg = wiki.page(l)

        # Print it title and link
        try:
            print("{: <50} {: <50}".format(*[l, pg.fullurl]))
        except KeyError:
            continue

get_links(p)