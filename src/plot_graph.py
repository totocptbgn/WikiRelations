import networkx as nx
import matplotlib.pyplot as plt
import random

g = nx.Graph()

a = 30000
b = 10000

for i in range(a):
    x = random.randint(0, b)
    y = random.randint(0, b)

    if x != y:
        for j in range(random.randint(1, 9)):
            g.add_edge(x, y)

fig = plt.figure(1, figsize=(100, 100))

options = {
    'with_labels': False,
    'node_color': 'black',
    'node_size': 40,
    'width': 1
}

pos = nx.spring_layout(g, pos={0:(0,0)}, fixed=[0], center=(0,0))
nx.draw_networkx(g, pos, **options)
plt.savefig("graph.png", format="PNG")