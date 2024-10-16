class Solution:
    def calculate(self, s: str) -> int:
        # Initialize stack, current number, and operation
        stack = []
        current_num = 0
        operation = '+'  # Start with '+' as the default operation

        # Iterate over the string, adding a dummy '+' at the end to handle the last number
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Build the number

            # If the character is an operator or we reach the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)  # Add number to stack
                elif operation == '-':
                    stack.append(-current_num)  # Add negative number to stack
                elif operation == '*':
                    stack[-1] = stack[-1] * current_num  # Multiply and replace top of stack
                elif operation == '/':
                    # Integer division should truncate towards zero
                    stack[-1] = int(stack[-1] / current_num)

                # Update operation and reset current_num for the next number
                operation = char
                current_num = 0

        # Return the sum of the stack
        return sum(stack)

# Usage example:
solution = Solution()
print(solution.calculate("3+2*2"))  # Output: 7
print(solution.calculate(" 3/2 "))  # Output: 1
print(solution.calculate(" 3+5 / 2 "))  # Output: 5
