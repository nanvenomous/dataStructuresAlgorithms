from collections import deque

def bfs(graph, vertex):
    queue = deque([vertex])
    visited = {vertex: True}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in visited:            
                queue.append(n)
                visited[n] = True