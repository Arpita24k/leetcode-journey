class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Check the least significant bit
            n >>= 1         # Right shift the number
        return count
