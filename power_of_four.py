class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive, a power of two, and that the '1' bit is in the correct position
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    print(solution.isPowerOfFour(16))  # Output: True
    
    # Test Case 2
    print(solution.isPowerOfFour(5))   # Output: False
    
    # Test Case 3
    print(solution.isPowerOfFour(1))   # Output: True
