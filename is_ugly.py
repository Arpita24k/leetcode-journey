class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False  # Ugly numbers are positive

        # Keep dividing n by 2, 3, and 5 while it's divisible
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime

        # If n is reduced to 1, it's an ugly number
        return n == 1

# Example usage:
solution = Solution()
print(solution.isUgly(6))  # Output: True
print(solution.isUgly(1))  # Output: True
print(solution.isUgly(14))  # Output: False
