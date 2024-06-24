class Solution:
    def isValid(self, s: str) -> bool:
        # A dictionary to hold matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it is not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly closed; otherwise, return False
        return not stack

# Example usage
s1 = "()"
print(Solution().isValid(s1))  # Output: True

s2 = "()[]{}"
print(Solution().isValid(s2))  # Output: True

s3 = "(]"
print(Solution().isValid(s3))  # Output: False

s4 = "([)]"
print(Solution().isValid(s4))  # Output: False

s5 = "{[]}"
print(Solution().isValid(s5))  # Output: True
