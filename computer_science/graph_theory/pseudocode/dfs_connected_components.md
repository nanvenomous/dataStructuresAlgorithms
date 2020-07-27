```
n = number of nodes in the graph
g = adjacency list representing the graph
count = 0
components = empty interger array # size n
visited = [False, ..., False] # size n

def findComponents():
	for i in range(n):
	if not visited[i]:
		count += 1
		dfs(i)
	return (count, components)


def dfs(at):
	visited[at] = True
	components[at] = count

	for next in g[at]:
		if not visited[next]:
			dfs(next)
```