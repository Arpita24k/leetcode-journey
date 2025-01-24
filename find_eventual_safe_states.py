from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n

        # Construct the reversed graph and compute in-degrees
        for src in range(n):
            for dest in graph[src]:
                reverse_graph[dest].append(src)
                in_degree[src] += 1
        
        # Start with all terminal nodes (in-degree = 0)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []

        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Return safe nodes sorted in ascending order
        return sorted(safe_nodes)

# ✅ Example Usage:
solution = Solution()

# Test Case 1
graph1 = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(solution.eventualSafeNodes(graph1))  # Output: [2, 4, 5, 6]

# Test Case 2
graph2 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
print(solution.eventualSafeNodes(graph2))  # Output: [4]
