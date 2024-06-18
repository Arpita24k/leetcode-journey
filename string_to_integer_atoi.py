class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the boundaries for 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Initialize variables
        i = 0
        n = len(s)
        result = 0
        sign = 1
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Read digits and form the number
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Check for overflow and clamp the result if necessary
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        # Apply the sign and return the result
        return sign * result

# Example usage
solution = Solution()

s1 = "42"
s2 = "   -42"
s3 = "4193 with words"
s4 = "words and 987"
s5 = "-91283472332"

print(solution.myAtoi(s1))  # Output: 42
print(solution.myAtoi(s2))  # Output: -42
print(solution.myAtoi(s3))  # Output: 4193
print(solution.myAtoi(s4))  # Output: 0
print(solution.myAtoi(s5))  # Output: -2147483648 (clamped)
