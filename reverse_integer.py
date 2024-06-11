class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return 0
            
            result = result * 10 + digit
        
        return sign * result

# Example usage
solution = Solution()

x1 = 123
x2 = -123
x3 = 120
x4 = 0
x5 = 1534236469  # This should cause overflow and return 0

print(solution.reverse(x1))  # Output: 321
print(solution.reverse(x2))  # Output: -321
print(solution.reverse(x3))  # Output: 21
print(solution.reverse(x4))  # Output: 0
print(solution.reverse(x5))  # Output: 0
