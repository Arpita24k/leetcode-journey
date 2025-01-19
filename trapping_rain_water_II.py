import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Directions for moving in 4 possible ways
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_water = 0
        
        # Process the cells in the heap
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate trapped water
                    total_water += max(0, height - heightMap[nx][ny])
                    # Update height to ensure the boundary height is maintained
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return total_water

# ✅ Example Usage
solution = Solution()

# Test Case 1
heightMap1 = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
print(solution.trapRainWater(heightMap1))  # Output: 4

# Test Case 2
heightMap2 = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
print(solution.trapRainWater(heightMap2))  # Output: 10
