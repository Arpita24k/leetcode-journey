class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            if stack:
                # If top of the stack + current char forms "AB" or "CD"
                if (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D'):
                    stack.pop()  # Remove the last character since "AB" or "CD" is found
                else:
                    stack.append(char)  # Otherwise, push the current character
            else:
                stack.append(char)  # If stack is empty, just push the character
        
        return len(stack)

# Example usage:
solution = Solution()

# Testcase 1
s1 = "ABFCACDB"
print(f"Output for s = '{s1}': {solution.minLength(s1)}")  # Expected Output: 2

# Testcase 2
s2 = "ACBBD"
print(f"Output for s = '{s2}': {solution.minLength(s2)}")  # Expected Output: 5
