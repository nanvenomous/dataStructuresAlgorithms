# https://leetcode.com/problems/clone-graph/
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    # def __eq__(self, other):
    #     if isinstance(self, other.__class__):
    #         return self.val == other.val and self.neighbors == other.neighbors
    #     return False

class CloneGraph:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = []
        self.extra_edges = []
        self.val_map = {}
        if not node: return None
        self.clone = self.make_clone(node)
        self.complete_extra_edges()
        return self.clone

    def get_neighbors(self, node):
        new_neighbors = []
        for neighbor in node.neighbors:
            if neighbor.val not in self.visited:
                new_neighbors.append(self.make_clone(neighbor))
            else: self.extra_edges.append([node.val, neighbor.val]) 
        return new_neighbors

    def make_clone(self, node):
        self.visited.append(node.val)
        new_node = Node(node.val, self.get_neighbors(node))
        self.val_map[new_node.val] = new_node
        return new_node

    def complete_extra_edges(self):
        for nd, ne in self.extra_edges:
            self.val_map[nd].neighbors.append(self.val_map[ne])
