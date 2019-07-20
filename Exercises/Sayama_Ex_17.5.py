import networkx as nx, pylab

g = nx.karate_club_graph()
g.pos = nx.spring_layout(g)

pylab.subplot(1,3,1)
nx.draw(g, node_color = [nx.degree_centrality(i) for i in list(g.nodes())], pos = g.pos)
pylab.subplot(1,3,2)
nx.draw(g, node_color = [nx.betweenness_centrality(i) for i in list(g.nodes())], pos = g.pos)
pylab.subplot(1,3,3)
nx.draw(g, node_color = [nx.closeness_centrality(i) for i in list(g.nodes())],pos=g.pos)
pylab.subplot(1,2,1)
nx.draw(g, node_color = [nx.eigenvector_centrality(i) for i in list(g.nodes())], pos=g.pos)
pylab.subplot(1,2,2)
nx.draw(g, node_color = [nx.pagerank(i) for i in list(g.nodes())], pos=g.pos)
pylab.show()

