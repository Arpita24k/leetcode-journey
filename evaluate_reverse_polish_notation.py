class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Apply the operation based on the operator
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Division should truncate towards zero
                    stack.append(int(a / b))  # Using int() for truncation towards zero
            else:
                # It's a number, push it to the stack
                stack.append(int(token))
        
        # The final result should be the only element in the stack
        return stack[0]

# Example usage:
solution = Solution()

# Test case 1
tokens = ["2", "1", "+", "3", "*"]
print(solution.evalRPN(tokens))  # Output: 9

# Test case 2
tokens = ["4", "13", "5", "/", "+"]
print(solution.evalRPN(tokens))  # Output: 6

# Test case 3
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.evalRPN(tokens))  # Output: 22
