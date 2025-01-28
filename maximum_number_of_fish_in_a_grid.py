from collections import deque

class Solution:
    def findMaxFish(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited[r][c] = True
            total_fish = 0

            while queue:
                x, y = queue.popleft()
                total_fish += grid[x][y]
                
                # Explore neighbors
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            
            return total_fish

        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    max_fish = max(max_fish, bfs(r, c))

        return max_fish


# ✅ Example Usage:
solution = Solution()

# Test Case 1
grid1 = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
print(solution.findMaxFish(grid1))  # Output: 7

# Test Case 2
grid2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
print(solution.findMaxFish(grid2))  # Output: 1
