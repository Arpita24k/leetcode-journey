class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ',':
                continue  # Ignore commas, they are just separators
            elif ch == ')':
                # When we hit a closing parenthesis, we need to evaluate the sub-expression
                sub_expr = []
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove the opening parenthesis '('

                # Get the operator before the parentheses
                operator = stack.pop()

                if operator == '!':
                    # For '!', there is exactly one sub-expression
                    stack.append('t' if sub_expr[0] == 'f' else 'f')
                elif operator == '&':
                    # For '&', if all are 't', result is 't', otherwise 'f'
                    stack.append('t' if all(x == 't' for x in sub_expr) else 'f')
                elif operator == '|':
                    # For '|', if any is 't', result is 't', otherwise 'f'
                    stack.append('t' if any(x == 't' for x in sub_expr) else 'f')
            else:
                # Push all other characters to the stack (operators, 't', 'f', '(')
                stack.append(ch)

        # At the end, the stack will contain a single element, which is the result
        return stack[0] == 't'

# Usage examples:
solution = Solution()
print(solution.parseBoolExpr("&(|(f))"))  # Output: False
print(solution.parseBoolExpr("|(f,f,f,t)"))  # Output: True
print(solution.parseBoolExpr("!(&(f,t))"))  # Output: True
