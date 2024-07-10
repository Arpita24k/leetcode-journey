class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge case
        max_length = 0  # Variable to keep track of the maximum length of valid parentheses
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the top of the stack for ')'
                if not stack:
                    stack.append(i)  # Push the current index if stack is empty
                else:
                    max_length = max(max_length, i - stack[-1])  # Update the maximum length
        
        return max_length

# Example usage:
solution = Solution()

# Test cases
print(solution.longestValidParentheses("(()"))      # Output: 2
print(solution.longestValidParentheses(")()())"))   # Output: 4
print(solution.longestValidParentheses(""))         # Output: 0
