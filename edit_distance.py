class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Create a 2D dp array with (m+1) rows and (n+1) columns
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1,    # Insert
                                   dp[i - 1][j] + 1,    # Delete
                                   dp[i - 1][j - 1] + 1) # Replace
        
        return dp[m][n]

# Example usage
solution = Solution()
print(solution.minDistance("horse", "ros"))       # Output: 3
print(solution.minDistance("intention", "execution"))  # Output: 5
