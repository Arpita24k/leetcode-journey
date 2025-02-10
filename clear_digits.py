class Solution:
    def clearDigits(self, s):
        stack = []

        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove the closest non-digit to the left
            else:
                stack.append(char)  # Keep adding letters to the stack

        return "".join(stack)
