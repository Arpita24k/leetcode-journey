class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0 and if n & (n - 1) is zero
        return n > 0 and (n & (n - 1)) == 0

# Example usage:
solution = Solution()

# Example 1:
n = 1
print(solution.isPowerOfTwo(n))  # Output: True

# Example 2:
n = 16
print(solution.isPowerOfTwo(n))  # Output: True

# Example 3:
n = 3
print(solution.isPowerOfTwo(n))  # Output: False
