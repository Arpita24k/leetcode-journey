import heapq
import math
from typing import List, Tuple

class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        INF = int(2e9)
        graph = [[] for _ in range(n)]

        # Build the graph with known weights
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        # Compute the initial shortest distance
        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            return []

        if current_shortest_distance == target:
            # Update edges with -1 weight to a high value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        # Binary search to find the minimum possible weight for the -1 edges
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                # Binary search for the minimal valid weight
                low, high = 1, target

                while low < high:
                    mid = (low + high) // 2
                    graph[u].append((v, mid))
                    graph[v].append((u, mid))
                    new_distance = self._dijkstra(graph, source, destination)
                    
                    if new_distance >= target:
                        high = mid
                    else:
                        low = mid + 1
                    
                    # Remove the edge after checking
                    graph[u].pop()
                    graph[v].pop()

                # Set the correct weight
                edges[i][2] = low
                graph[u].append((v, low))
                graph[v].append((u, low))

        # Final check if the target is achievable
        if self._dijkstra(graph, source, destination) == target:
            # Update remaining edges with -1 weight to an impossible value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges
        else:
            return []

    def _dijkstra(
        self, graph: List[List[Tuple[int, int]]], src: int, destination: int
    ) -> int:
        min_distance = [math.inf] * len(graph)
        min_distance[src] = 0
        min_heap = [(0, src)]  # (distance, node)

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]

# Example Usage:
solution = Solution()

n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 5
print(solution.modifiedGraphEdges(n, edges, source, destination, target))  # Expected: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]

n = 3
edges = [[0,1,-1],[0,2,5]]
source = 0
destination = 2
target = 6
print(solution.modifiedGraphEdges(n, edges, source, destination, target))  # Expected: []

n = 4
edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
source = 0
destination = 2
target = 6
print(solution.modifiedGraphEdges(n, edges, source, destination, target))  # Expected: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
