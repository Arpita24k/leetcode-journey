class Solution:
    def calculate(self, s: str) -> int:
        # Initialize stack, current number, result and sign
        stack = []
        current_number = 0
        current_result = 0
        sign = 1
        
        # Iterate over each character in the string
        for char in s:
            if char.isdigit():  # If the character is a digit
                current_number = current_number * 10 + int(char)  # Form the current number
            elif char in ['+', '-']:  # If the character is an operator
                current_result += sign * current_number  # Update result with the current number and sign
                current_number = 0  # Reset current number
                sign = 1 if char == '+' else -1  # Update sign based on the operator
            elif char == '(':  # If the character is an opening parenthesis
                # Push the current result and sign onto the stack
                stack.append(current_result)
                stack.append(sign)
                # Reset result and sign for new sub-expression
                current_result = 0
                sign = 1
            elif char == ')':  # If the character is a closing parenthesis
                current_result += sign * current_number  # Update result with the current number and sign
                current_number = 0  # Reset current number
                current_result *= stack.pop()  # Apply the sign before the parenthesis
                current_result += stack.pop()  # Add the result before the parenthesis
            # Ignore spaces
        current_result += sign * current_number  # Add any remaining number to the result
        
        return current_result  # Return the final result

# Example usage
solution = Solution()
s1 = "1 + 1"
s2 = " 2-1 + 2 "
s3 = "(1+(4+5+2)-3)+(6+8)"

print(solution.calculate(s1))  # Output: 2
print(solution.calculate(s2))  # Output: 3
print(solution.calculate(s3))  # Output: 23
