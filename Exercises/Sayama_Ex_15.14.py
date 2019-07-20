import networkx as nx

g=nx.karate_club_graph()
nx.write_adjlist(g,'karate_club_graph_adj.txt')
nx.write_edgelist(g,'karate_club_graph_adj.txt')

