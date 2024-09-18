class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the least significant bit of n
            bit = n & 1
            # Shift the bit to the correct position in the reversed number
            result = (result << 1) | bit
            # Shift n to the right to process the next bit
            n >>= 1
        return result

# Example usage:
solution = Solution()

# Example 1:
n = 0b00000010100101000001111010011100  # Input as binary
print(solution.reverseBits(n))  # Output: 964176192 (00111001011110000010100101000000)

# Example 2:
n = 0b11111111111111111111111111111101  # Input as binary
print(solution.reverseBits(n))  # Output: 3221225471 (10111111111111111111111111111111)
