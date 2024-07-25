class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting point is an obstacle, return 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize a 1D DP array with size n
        dp = [0] * n
        dp[0] = 1  # Starting point

        # Fill the DP array
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # If there's an obstacle, set paths to 0
                elif j > 0:
                    dp[j] += dp[j - 1]  # Update the paths from the left and above

        return dp[-1]

# Examples
solution = Solution()
print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # Output: 2
print(solution.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # Output: 1
