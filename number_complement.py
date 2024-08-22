class Solution:
    def findComplement(self, num: int) -> int:
        # Find the bit length of num
        bit_length = num.bit_length()
        
        # Create a bitmask with all bits set to 1 of the same length as num
        bitmask = (1 << bit_length) - 1
        
        # XOR num with the bitmask to get the complement
        return num ^ bitmask

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    num1 = 5
    print(solution.findComplement(num1))  # Output: 2
    
    # Test Case 2
    num2 = 1
    print(solution.findComplement(num2))  # Output: 0
