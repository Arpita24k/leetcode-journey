class Solution:
    def canWinNim(self, n: int) -> bool:
        # You can win if n is not divisible by 4
        return n % 4 != 0

# Example usage:
solution = Solution()

# Example 1:
n = 4
print(solution.canWinNim(n))  # Output: False

# Example 2:
n = 1
print(solution.canWinNim(n))  # Output: True

# Example 3:
n = 2
print(solution.canWinNim(n))  # Output: True
