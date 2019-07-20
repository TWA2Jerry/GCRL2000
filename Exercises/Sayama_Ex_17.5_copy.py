import networkx as nx, pylab

g = nx.karate_club_graph()
g.pos = nx.spring_layout(g)

pylab.subplot(2,3,1)
nx.draw(g, node_color = [nx.degree_centrality(g)[i] for i in nx.degree_centrality(g)], pos = g.pos)
pylab.title('Degree centrality')
pylab.subplot(2,3,2)
nx.draw(g, node_color = [nx.betweenness_centrality(g)[i] for i in nx.betweenness_centrality(g)], pos = g.pos)
pylab.title('Betweenness centrality')
pylab.subplot(2,3,3)
nx.draw(g, node_color = [nx.closeness_centrality(g)[i] for i in nx.closeness_centrality(g)],pos=g.pos)
pylab.title('Closeness centrality')
pylab.subplot(2,3,4)
nx.draw(g, node_color = [nx.eigenvector_centrality(g)[i] for i in nx.eigenvector_centrality(g)], pos=g.pos)
pylab.title('Eigenvector centrality')
pylab.subplot(2,3,5)
nx.draw(g, node_color = [nx.pagerank(g)[i] for i in nx.pagerank(g)], pos=g.pos)
pylab.title('pagerank')
pylab.show()

