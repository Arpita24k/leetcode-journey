class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D dp array with m rows and n columns
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths to reach the bottom-right corner
        return dp[m-1][n-1]

# Example usage
solution = Solution()
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3
