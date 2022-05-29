# WikiRelations

> Graph visualisation on wikipedia pages proximity.

![Graph](/docs/wiki.png)

## Use

Create a csv file a seed and a depth : 
```sh
$ python3 src/parse_wiki.py [Name of the page] [Depth] > src/csv/[Output filename].csv

# Example:
python3 src/parse_wiki.py 'Star Wars' 2 > src/csv/sw_2.csv
```

Plot graph :
```sh
python3 src/plot_graph_wiki.py
```

## Dependencies :

```sh
$ pip3 install networkx scipy
```