class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Constructs the lexicographically smallest number following the given 'I' and 'D' pattern.

        Args:
        pattern (str): A string consisting of 'I' and 'D'.

        Returns:
        str: The lexicographically smallest possible number.
        """
        result = []
        stack = []
        num = 1  # Start filling from 1 to 9

        for i, ch in enumerate(pattern):
            stack.append(str(num))  # Push the current number onto the stack
            num += 1  # Move to the next available digit

            if ch == 'I':  # On encountering 'I', pop the stack into result
                while stack:
                    result.append(stack.pop())

        stack.append(str(num))  # Add the last number
        while stack:
            result.append(stack.pop())  # Empty stack into result

        return "".join(result)
