import networkx as nx, pylab

g = nx.read_edgelist("social_structure.txt", create_using = nx.DiGraph())
nx.draw(g, with_labels = True)
pylab.show()
