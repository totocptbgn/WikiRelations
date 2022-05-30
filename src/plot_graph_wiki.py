import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
filename = 'src/csv/lotr_2.csv'

# Creating the graph and the dataframe
g = nx.Graph()
df = pd.read_csv(filename, sep=';', header=None)
df = df.sample(frac=0.01)
print(f'Dataframe created.')

# print(df.shape)
# print(df.describe())
# print(df.head(100))   

# Adding edges 
for index, row in df.iterrows():
    g.add_edge(row[0], row[1])
print('Added edges.')

# Setup node position following the spring layout
pos = nx.spring_layout(g)
print('Layout edges.')

# Plot and save the ouput
options = {
    'with_labels': False,
    'node_color': 'white',
    'node_size': 20,
    'width': 0.5,
    'alpha': 0.5
}
fig = plt.figure(1, figsize=(40, 40), dpi=300.0, facecolor='black', frameon="False")
nx.draw_networkx(g, pos, **options)
print('Drawn graph.')
plt.savefig("graph.png", format="PNG")
print('Saved PNG.')
