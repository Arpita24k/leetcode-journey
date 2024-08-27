import heapq
from collections import defaultdict
import math

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Build the graph using an adjacency list
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Max-heap priority queue
        max_heap = [(-1.0, start)]  # Use negative probabilities to simulate max-heap
        probabilities = [0.0] * n  # Track the best probability to each node
        probabilities[start] = 1.0
        
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob
            
            # If we reached the end, return the probability
            if node == end:
                return curr_prob
            
            # Visit all neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                # If a higher probability path to `neighbor` is found, update and push to heap
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we exhaust the search and never reach `end`
        return 0.0

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n1 = 3
    edges1 = [[0, 1], [1, 2], [0, 2]]
    succProb1 = [0.5, 0.5, 0.2]
    start1 = 0
    end1 = 2
    print(solution.maxProbability(n1, edges1, succProb1, start1, end1))  # Output: 0.25
    
    # Test Case 2
    n2 = 3
    edges2 = [[0, 1], [1, 2], [0, 2]]
    succProb2 = [0.5, 0.5, 0.3]
    start2 = 0
    end2 = 2
    print(solution.maxProbability(n2, edges2, succProb2, start2, end2))  # Output: 0.3
    
    # Test Case 3
    n3 = 3
    edges3 = [[0, 1]]
    succProb3 = [0.5]
    start3 = 0
    end3 = 2
    print(solution.maxProbability(n3, edges3, succProb3, start3, end3))  # Output: 0.0
