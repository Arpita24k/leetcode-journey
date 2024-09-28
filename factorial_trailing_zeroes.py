class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # Keep dividing n by 5, 25, 125, etc., and add the quotients
        while n > 0:
            n //= 5
            count += n
        return count
