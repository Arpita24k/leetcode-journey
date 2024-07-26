class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create a dp array of the same size as grid
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the starting point
        dp[0][0] = grid[0][0]
        
        # Initialize the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Initialize the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]

# Examples
solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(solution.minPathSum([[1,2,3],[4,5,6]]))  # Output: 12
