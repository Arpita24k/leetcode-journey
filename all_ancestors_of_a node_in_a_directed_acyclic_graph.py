from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edgeList: List[List[int]]) -> List[List[int]]:
        # Create graph adjacency list
        graph = defaultdict(list)
        for src, dst in edgeList:
            graph[dst].append(src)
        
        # Prepare to store ancestors for each node
        ancestors = [set() for _ in range(n)]
        
        # Helper function for DFS to find ancestors
        def dfs(node, visited, start):
            for ancestor in graph[node]:
                if ancestor not in visited:
                    visited.add(ancestor)
                    ancestors[start].add(ancestor)
                    dfs(ancestor, visited, start)
        
        # Start DFS from each node to collect its ancestors
        for node in range(n):
            visited = set()
            dfs(node, visited, node)
        
        # Convert sets to sorted lists
        return [sorted(ancestors[node]) for node in range(n)]

# Example usage
sol = Solution()
n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(sol.getAncestors(n, edges))  # Output: [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

n = 5
edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.getAncestors(n, edges))  # Output: [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
