class Solution:
    def minimumCost(self, source: str, target: str, original: [str], changed: [str], cost: [int]) -> int:
        import sys
        INF = sys.maxsize
        
        # Initialize the cost matrix with infinity
        dist = [[INF] * 26 for _ in range(26)]
        
        # Set the distance from a character to itself as 0
        for i in range(26):
            dist[i][i] = 0
        
        # Populate the cost matrix with given transformations
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        
        # Apply Floyd-Warshall algorithm to find shortest paths between all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total_cost = 0
        
        # Calculate the minimum cost to transform source to target
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            
            if dist[u][v] == INF:
                return -1  # Transformation is impossible
            
            total_cost += dist[u][v]
        
        return total_cost

# Examples
solution = Solution()
print(solution.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]))  # Output: 28
print(solution.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]))  # Output: 12
print(solution.minimumCost("abcd", "abce", ["a"], ["e"], [10000]))  # Output: -1
