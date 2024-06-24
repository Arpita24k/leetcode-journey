class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any trailing spaces
        s = s.rstrip()
        
        # Split the string into words by spaces
        words = s.split(' ')
        
        # Return the length of the last word
        return len(words[-1])

# Example usage
s1 = "Hello World"
print(Solution().lengthOfLastWord(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s3))  # Output: 6
