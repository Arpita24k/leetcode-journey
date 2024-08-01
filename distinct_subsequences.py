class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # Initialize the DP table with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: An empty t can be formed from any prefix of s
        for i in range(m + 1):
            dp[i][0] = 1  # Empty t is a subsequence of any s
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:  # If characters match
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:  # If characters do not match
                    dp[i][j] = dp[i-1][j]
        
        # The result is in dp[m][n]
        return dp[m][n]

# Example usage
solution = Solution()
s1, t1 = "rabbbit", "rabbit"
s2, t2 = "babgbag", "bag"

print(solution.numDistinct(s1, t1))  # Output: 3
print(solution.numDistinct(s2, t2))  # Output: 5
