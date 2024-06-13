from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the input list of characters in place with O(1) extra memory.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the characters at left and right indices
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1

# Example usage
solution = Solution()

s1 = ["h", "e", "l", "l", "o"]
solution.reverseString(s1)
print("Reversed s1:", s1)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s2)
print("Reversed s2:", s2)  # Output: ["h", "a", "n", "n", "a", "H"]
