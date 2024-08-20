class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = i  # Maximum is i operations (just Paste 1 at a time)
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
        
        return dp[n]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n1 = 3
    print(solution.minSteps(n1))  # Output: 3
    
    # Test Case 2
    n2 = 1
    print(solution.minSteps(n2))  # Output: 0
