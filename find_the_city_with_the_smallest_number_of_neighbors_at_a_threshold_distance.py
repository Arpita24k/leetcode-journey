class Solution:
    def findTheCity(self, n: int, edges: [[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with inf
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall Algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Count the number of reachable cities within the distance threshold for each city
        min_count = float('inf')
        result_city = -1
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            # Choose the city with the smallest number of reachable cities,
            # In case of tie, choose the city with the greatest number
            if count < min_count or (count == min_count and i > result_city):
                min_count = count
                result_city = i
        
        return result_city

# Examples
solution = Solution()
print(solution.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))  # Output: 3
print(solution.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))  # Output: 0
