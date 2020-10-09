```
from collections import deque
n = number of nodes in the graph
g = adjacency list representing unweighted graph

def solve(s):
	q = deque()
	q.append(s)
	visited = [False, ..., False] # size n
	visited[s] = True

	prev = [null, ..., null] # size n
	while q:
		node = q.popleft()
		neighbors = g.get(node)

		for(next in neighbors):
			if not visited[next]:
				q.append(next)
				visited[next] = True
				prev[next] = node
	return prev

def reconstructPath(s, e, prev):
	# reconstruct path going backwards from e
	path = []
	for at=e; at != null; at = prev[at]):
		path.add(at)
	path.reverse()
	# if s and e are connected return the path
	if path[0] == s:
		return path
	return []

# s: start node, e: end node, 0 <= e, s < n
def bfs(s, e):
	prev = solve(s)
	return reconstructPath(s, e, prev)
```