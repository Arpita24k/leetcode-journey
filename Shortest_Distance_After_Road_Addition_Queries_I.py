from collections import deque, defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        """
        Find the shortest path from city 0 to city n-1 after each query.

        Args:
        n (int): Number of cities.
        queries (List[List[int]]): New roads to add as queries.

        Returns:
        List[int]: Length of the shortest path after each query.
        """
        # Initialize the graph as an adjacency list
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)  # Add the default unidirectional edges
        
        def bfs_shortest_path():
            """Perform BFS to find the shortest path from city 0 to city n-1."""
            queue = deque([(0, 0)])  # (current city, distance)
            visited = set()
            
            while queue:
                current, distance = queue.popleft()
                if current in visited:
                    continue
                visited.add(current)
                
                if current == n - 1:  # Reached the target city
                    return distance
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
            
            return -1  # Return -1 if there's no path

        result = []
        for u, v in queries:
            graph[u].append(v)  # Add the new road
            result.append(bfs_shortest_path())  # Compute the shortest path

        return result
