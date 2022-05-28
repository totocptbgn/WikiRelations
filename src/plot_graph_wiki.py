import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
filename = 'src/csv/sw_2.csv'

# Progress bar
def printProgressBar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total: 
        print('', end=printEnd)

# Creating the graph and the dataframe
g = nx.Graph()
df = pd.read_csv(filename, sep=';', header=None)
# print(df.shape)
# print(df.describe())
# print(df.head(100))   

# Adding edges 
printProgressBar(0, df.shape[0], prefix = 'Adding edges:', suffix = 'Done.', length = 100)
for index, row in df.iterrows():
    g.add_edge(row[0], row[1])
    printProgressBar(index + 1, df.shape[0], prefix = 'Adding edges:', suffix = 'Done.', length = 100)

# Setup node position following the spring layout
pos = nx.spring_layout(g)

# Plot and save the ouput
options = {
    'with_labels': False,
    'node_color': 'black',
    'node_size': 40,
    'width': 1
}
fig = plt.figure(1, figsize=(100, 100))
nx.draw_networkx(g, pos, **options)
plt.savefig("graph.png", format="PNG")
