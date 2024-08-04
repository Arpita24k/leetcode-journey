class Solution:
    def minimumTotal(self, triangle):
        # Initialize the dp array with the last row of the triangle
        dp = triangle[-1][:]
        
        # Iterate from the second last row to the top row
        for r in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[r])):
                # Update dp[i] with the minimum path sum for the current element
                dp[i] = triangle[r][i] + min(dp[i], dp[i + 1])
        
        # The minimum path sum from top to bottom will be the first element of dp
        return dp[0]

# Example usage
solution = Solution()
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle2 = [[-10]]

print(solution.minimumTotal(triangle1))  # Output: 11
print(solution.minimumTotal(triangle2))  # Output: -10
