# WikiRelations

> Graph visualisation on wikipedia pages proximity.

![Graph](/docs/wiki.png)
> The points represent every pages and they are linked when one page appears in the other (is linked).

## Description

I was trying to have fun visualisation of Wikipage page relationships but the data is way too heavy and the graphs produced with networkx weren't good. I had to sample the data to plot it so I wasn't satified with the result but it gave us a fun image !

- `parse_wiki.py` is for creating a csv files from a wiki page, a langage and a depth.
- `plot_graph_wiki.py` is for ploting the csv files with networkx.

## Use

Create a csv file a seed and a depth : 
```sh
python3 src/parse_wiki.py [Name of the page] [Depth] > src/csv/[Output filename].csv

# Example:
python3 src/parse_wiki.py 'Star Wars' 2 > src/csv/sw_2.csv
```

Plot graph :
```sh
python3 src/plot_graph_wiki.py
```

## Dependencies :

```sh
pip3 install networkx scipy
```
