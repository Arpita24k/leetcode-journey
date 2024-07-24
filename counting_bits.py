class Solution:
    def countBits(self, n: int) -> [int]:
        # Initialize the result array with zeros
        ans = [0] * (n + 1)
        
        # Fill the DP table
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans

# Examples
solution = Solution()
print(solution.countBits(2))  # Output: [0, 1, 1]
print(solution.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
