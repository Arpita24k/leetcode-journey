class Solution:
    def climbStairs(self, n: int) -> int:
        # Edge case for 0 or 1 steps
        if n <= 1:
            return 1

        # Initializing the base cases
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # Fill the dp array using the recurrence relation
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
