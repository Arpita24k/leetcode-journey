class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        
        # XOR all characters in s and t
        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)
        
        # The result is the ASCII value of the extra character
        return chr(result)

# Example usage:
solution = Solution()

# Example 1
s = "abcd"
t = "abcde"
print(solution.findTheDifference(s, t))  # Output: "e"

# Example 2
s = ""
t = "y"
print(solution.findTheDifference(s, t))  # Output: "y"
