from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: [[int]], colConditions: [[int]]) -> [[int]]:
        def topological_sort(conditions, k):
            # Create adjacency list and in-degree array
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            # Kahn's algorithm for topological sorting
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(order) == k:
                return order
            else:
                return []  # Not possible to sort topologically
            
        # Get the topological order for rows and columns
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        # Create a mapping from number to its position in the order
        row_position = {num: i for i, num in enumerate(row_order)}
        col_position = {num: i for i, num in enumerate(col_order)}
        
        # Construct the matrix
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_position[num]][col_position[num]] = num
        
        return matrix

# Examples
solution = Solution()
print(solution.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))  # Output: [[3,0,0],[0,0,1],[0,2,0]]
print(solution.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]))  # Output: []
