class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # Initialize the stack to keep track of characters and substrings
        
        for char in s:
            if char == ')':  # When we encounter a closing parenthesis
                substring = []
                while stack and stack[-1] != '(':  # Pop characters until we find an opening parenthesis
                    substring.append(stack.pop())
                stack.pop()  # Pop the opening parenthesis '('
                stack.extend(substring)  # Push the reversed substring back onto the stack
            else:
                stack.append(char)  # Push other characters onto the stack
        
        return ''.join(stack)  # Join the characters in the stack to form the final result

# Example usage:
solution = Solution()

# Test cases
print(solution.reverseParentheses("(abcd)"))       # Output: "dcba"
print(solution.reverseParentheses("(u(love)i)"))   # Output: "iloveu"
print(solution.reverseParentheses("(ed(et(oc))el)")) # Output: "leetcode"
