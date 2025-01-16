class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        set_bits = bin(num2).count('1')
        
        # Count the number of set bits in num1
        num1_bits = bin(num1).count('1')
        
        # Convert num1 to a list of bits
        result = 0
        
        # If num1 already has enough set bits, keep the highest ones
        if num1_bits >= set_bits:
            # Place `set_bits` number of highest set bits from num1
            for i in range(31, -1, -1):  # Checking bits from most significant to least
                if num1 & (1 << i):
                    result |= (1 << i)
                    set_bits -= 1
                if set_bits == 0:
                    break
        else:
            # Otherwise, place all set bits from num1 and add more from the right
            result = num1
            set_bits -= num1_bits
            for i in range(32):
                if not (num1 & (1 << i)):  # Add extra bits where num1 has 0
                    result |= (1 << i)
                    set_bits -= 1
                if set_bits == 0:
                    break
                    
        return result

# ✅ Example Usage:
solution = Solution()

# Test Case 1
num1 = 3
num2 = 5
print(solution.minimizeXor(num1, num2))  # Output: 3

# Test Case 2
num1 = 1
num2 = 12
print(solution.minimizeXor(num1, num2))  # Output: 3

# Test Case 3
num1 = 8
num2 = 7
print(solution.minimizeXor(num1, num2))  # Output: 7
