class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants to handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for easier bit manipulation
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Left shift divisor until it is larger than dividend
        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts <<= 1
            dividend -= temp_divisor
            quotient += num_shifts
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))

# Example usage:
solution = Solution()

# Test cases
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
