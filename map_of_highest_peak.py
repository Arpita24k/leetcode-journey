from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        
        # Initialize height matrix
        height = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Initialize BFS queue with all water cells
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        # Directions for north, south, east, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS to assign heights
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and unvisited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height

# ✅ Example Usage:
solution = Solution()

# Test Case 1
isWater1 = [[0, 1], [0, 0]]
print(solution.highestPeak(isWater1))  # Output: [[1, 0], [2, 1]]

# Test Case 2
isWater2 = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(solution.highestPeak(isWater2))  # Output: [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
