class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Function to implement wildcard pattern matching with support for '?' and '*'.
        
        Args:
        s: Input string.
        p: Pattern string containing wildcards '?' and '*'.
        
        Returns:
        Boolean value indicating whether the pattern matches the entire input string.
        """
        # Lengths of the input string and pattern
        s_len, p_len = len(s), len(p)
        
        # Table to store results of subproblems
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns with '*' at the beginning
        for j in range(1, p_len + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the table
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] == '*':
                    # '*' can match zero or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Match single character or exact character
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[s_len][p_len]

# Example usage
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: False
print(solution.isMatch("aa", "*"))  # Output: True
print(solution.isMatch("cb", "?a")) # Output: False
