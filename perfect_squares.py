import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize dp array where dp[i] is the minimum number of squares needed for i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 requires 0 squares
        
        # Build up dp array from 1 to n
        for i in range(1, n + 1):
            # Check each perfect square j*j that is <= i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)  # Choose the minimum count
                j += 1
        
        return dp[n]  # Result is stored in dp[n]

# Example usage:
solution = Solution()

# Example 1
n1 = 12
print("Example 1 Output:", solution.numSquares(n1))  # Expected Output: 3

# Example 2
n2 = 13
print("Example 2 Output:", solution.numSquares(n2))  # Expected Output: 2
