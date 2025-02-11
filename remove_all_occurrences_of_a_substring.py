class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Removes all occurrences of substring part from s using stack.

        Args:
        s (str): Input string.
        part (str): Substring to remove.

        Returns:
        str: Final string after all removals.
        """
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)  # Add character to stack

            # Check if the last `len(part)` characters form `part`
            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                del stack[-part_len:]  # Remove last `part_len` characters

        return "".join(stack)
