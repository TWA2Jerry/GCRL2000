import networkx as nx, community as comm, pylab 

g = nx.karate_club_graph()
bp = comm.best_partition(g)
nx.draw(g, node_color = [bp[i] for i in bp])
pylab.show()
