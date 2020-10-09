# [Graph Theory](https://www.youtube.com/watch?v=09_LlHjoEiY)

# Types

| Type | definition |
|---|---|
| undirected | all edged have no orientation |
| digraph (directed) | edges have orientations |
| weighted | edges contain a certain weight to represent arbitrary value |
| tree | undirected graph with no cycles & a connected graph with n noded and n-1 edges |
| rooted tree | designated root, every node either points toward or away from the root |
| DAG (directed acyclic) | directed graphs with no cycles |
| bipartite | vertices can be split in two to separate groups, every edge connects between the separate groups |
| complete | unique edge between every pair of nodes |

# Representations
* adjacency matrix
```
_	A	B	C
A	0	4	1
B	3	0	6
C	4	1	0
```
* adjacency list: map to lists of node
```
{
	A: [B, C],
	B: [C],
	C: [A, B, D],
}
```
* edge list:
```
[
	[C, A, 1],
	[A, C, 4],
	[B, C, 2],
	[A, D, 3],
]
```

| representation | space efficient | edge weight lookup |
|---|---|---|
| adjacency matrix | O(V^2) | O(1) |
| adjacency list | space effieient for sparse graphs, not dense graphs | O(E) |
| edge list | space effieient for sparse graphs, not dense graphs | O(E) |

# Approach
* directed or undirected?
* edges weighted?
* likely to be sparse or dense with edges
* what representation should I use

# Common Problems

| problem | description | algorithms |
|---|---|---|
| shortest path | get from one point to another fastest | BFS, dijkstras, bellman-ford, floyd-warshall, A*, ... |
| path exists | can you get from one vertex to another | union find data structure or any search algo i.e. BFS, DFS |
| negative cycle | continue to increment/decrement as you cycle | bellman-ford & floyd-warshall |
| strongly connected components | self contained cycles | tarjan's and kosaraju's |
| traveling salesman | visit each city, get back to first, minimum cost | Held-Karp, branch and bound, many approximation algorithms (ant colony) |
| MST, minimum spanning tree | a subset of edges with no cycles & with minimum possible edge width | kruskal's, Prim's and Boruvka's algorithm |
| max network flow | with an infinite input source, how much flow can the network handle | ford-fulkerson, edmonds-karp, dinic's |

| feature | description |
|---|---|
| bridges | edge, when removed, increases # of connected components |
| articulation point | node, when removed, when removed, increases the number of connected components |

# Algorithms

| algorithm | time complexity | description | links |
|---|---|---|---|
| DFS | O(V+E) | usually augmented to count connected components, determine connectivity, find bridges/articulation | [dfs](./pseudocode/depth_first_search.md), [connected components](./pseudocode/dfs_connected_components.md) |
| BFS | O(V+E) | finds the shortest path on an unweighted path | [bfs](./pseudocode/breadth_first_search.py), [bfs with path](./pseudocode/bfs_get_path.py) |
| [topological sort](https://www.youtube.com/watch?v=09_LlHjoEiY&t=3383s) |  | prerequesites, should have a topological ordering or be a directed acyclic graph (DAG) |  |
|  |  |  |  |
|  |  |  |  |

