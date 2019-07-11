import networkx as nx

g = nx.Graph()

g.add_node('Jesse')
g.node['Jesse']['Height'] = 1.86
print(g.node['Jesse']['Height'])
