```
n = number of nodes in the graph
g = adjacency list representing the graph
visited = [False, ..., False] # size n

def dfs(at):
	if visited[at]: return
	visited[at] = True

	neighbors = graph[at]
	for next in neighbors:
		dfs(next)
dfs(0)
```