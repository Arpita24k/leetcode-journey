from collections import deque

class Solution:
    def minCost(self, grid):
        # Grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Direction mappings: (dx, dy) for directions 1, 2, 3, 4
        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }
        
        # BFS setup
        queue = deque([(0, 0, 0)])  # (x, y, cost)
        visited = set()
        
        # BFS
        while queue:
            x, y, cost = queue.popleft()
            
            # If reached the bottom-right corner
            if (x, y) == (m - 1, n - 1):
                return cost
            
            # Mark the cell as visited
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            # Explore neighbors
            for d, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                
                # Check bounds
                if 0 <= nx < m and 0 <= ny < n:
                    # Correct direction: Add to the front (cost = 0)
                    if d == grid[x][y]:
                        queue.appendleft((nx, ny, cost))
                    # Incorrect direction: Add to the back (cost = 1)
                    else:
                        queue.append((nx, ny, cost + 1))
        
        return -1  # Should never reach here if the input is valid

# Example Usage:
solution = Solution()

# Test Case 1
grid1 = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
print(solution.minCost(grid1))  # Output: 3

# Test Case 2
grid2 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
print(solution.minCost(grid2))  # Output: 0

# Test Case 3
grid3 = [[1, 2], [4, 3]]
print(solution.minCost(grid3))  # Output: 1
