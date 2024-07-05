class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string and empty pattern are a match
        dp[0][0] = True
        
        # Base case: patterns with '*' can match an empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can either match zero previous elements or one/more previous elements
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # Current characters match or pattern has a '.'
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        
        return dp[m][n]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa", "a"))       # Output: False
    print(solution.isMatch("aa", "a*"))      # Output: True
    print(solution.isMatch("ab", ".*"))      # Output: True
    print(solution.isMatch("aab", "c*a*b"))  # Output: True
    print(solution.isMatch("mississippi", "mis*is*p*."))  # Output: False
