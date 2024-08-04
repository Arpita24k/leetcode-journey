class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # If the node is already visited, return the cloned node from the visited dictionary
        if node in self.visited:
            return self.visited[node]
        
        # Clone the node (without neighbors initially)
        clone = Node(node.val)
        self.visited[node] = clone
        
        # Clone all the neighbors recursively
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone

# Helper function to build the graph from adjacency list
def buildGraph(adjList):
    if not adjList:
        return None
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]

# Helper function to print the graph as adjacency list
def printGraph(node):
    if not node:
        return []
    
    visited = set()
    result = []
    
    def dfs(n):
        if n.val in visited:
            return
        visited.add(n.val)
        result.append([neigh.val for neigh in n.neighbors])
        for neigh in n.neighbors:
            dfs(neigh)
    
    dfs(node)
    return result

# Example usage
solution = Solution()

adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
adjList2 = [[]]
adjList3 = []

graph1 = buildGraph(adjList1)
cloned_graph1 = solution.cloneGraph(graph1)
print(printGraph(cloned_graph1))  # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

graph2 = buildGraph(adjList2)
cloned_graph2 = solution.cloneGraph(graph2)
print(printGraph(cloned_graph2))  # Output: [[]]

graph3 = buildGraph(adjList3)
cloned_graph3 = solution.cloneGraph(graph3)
print(printGraph(cloned_graph3))  # Output: []
