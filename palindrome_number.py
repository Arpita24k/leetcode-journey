class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Reverse the integer and compare with the original integer
        original = x
        reversed_num = 0
        
        while x != 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x //= 10
        
        return original == reversed_num

# Example usage
solution = Solution()

# Test case 1
x1 = 121
print(solution.isPalindrome(x1))  # Output: True

# Test case 2
x2 = -121
print(solution.isPalindrome(x2))  # Output: False

# Test case 3
x3 = 10
print(solution.isPalindrome(x3))  # Output: False
