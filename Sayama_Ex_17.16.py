import networkx as nx, community as comm ,pylab

g = nx.read_gml("lesmis/lesmis.gml")
bp  = comm.best_partition(g)
nx.draw(g, node_color = [bp[i] for i in bp])
pylab.show() 
