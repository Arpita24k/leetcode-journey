class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Count the number of servers in each row and column
        row_count = [0] * m
        col_count = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count the servers that can communicate
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        
        return count

# ✅ Example Usage:
solution = Solution()

# Test Case 1
grid1 = [[1, 0], [0, 1]]
print(solution.countServers(grid1))  # Output: 0

# Test Case 2
grid2 = [[1, 0], [1, 1]]
print(solution.countServers(grid2))  # Output: 3

# Test Case 3
grid3 = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(solution.countServers(grid3))  # Output: 4
