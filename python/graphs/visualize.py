import networkx as nx 
import matplotlib.pyplot as plt

class graphs:
	class adjacency:
		one = {
			0: [6],
			1: [9, 2, 3],
			2: [4, 2, 9, 8],
			3: [6, 5, 7],
			4: [1, 3, 7],
			6: [4, 8],
			}
	class edge:
		one = [
			[0, 2], [1, 2],[1, 3],
			[5, 3], [3, 4], [1, 0],
			]

def visualize_edge_list(edg_list):
	G = nx.Graph() 
	G.add_edges_from(edg_list)
	nx.draw_networkx(G)

def visualize_adjacency_list(adj_list):
	H = nx.Graph(adj_list) 
	nx.draw_networkx(H)

# visualize_edge_list(graphs.edge.one)
visualize_adjacency_list(graphs.adjacency.one)

plt.show() 