class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j - 1] + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0))
        
        return dp[0][n - 1]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "aaabbb"
    print(solution.strangePrinter(s1))  # Output: 2
    
    # Test Case 2
    s2 = "aba"
    print(solution.strangePrinter(s2))  # Output: 2
