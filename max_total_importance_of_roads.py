from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Count connections for each city
        connection_counts = defaultdict(int)
        for a, b in roads:
            connection_counts[a] += 1
            connection_counts[b] += 1
        
        # Sort cities by the number of connections in descending order
        sorted_cities = sorted(range(n), key=lambda x: connection_counts[x], reverse=True)
        
        # Assign highest values to the most connected cities
        city_values = {}
        value = n
        for city in sorted_cities:
            city_values[city] = value
            value -= 1
        
        # Calculate total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += city_values[a] + city_values[b]
        
        return total_importance

# Example usage
solution = Solution()

# Test case 1
n1 = 5
roads1 = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(solution.maximumImportance(n1, roads1))  # Output: 43

# Test case 2
n2 = 5
roads2 = [[0,3],[2,4],[1,3]]
print(solution.maximumImportance(n2, roads2))  # Output: 20
