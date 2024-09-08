class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into words, automatically handles multiple spaces
        words = s.split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the words back into a string with a single space separating them
        return ' '.join(words)

# Example usage:
sol = Solution()

# Example 1:
s = "the sky is blue"
print(sol.reverseWords(s))  # Output: "blue is sky the"

# Example 2:
s = "  hello world  "
print(sol.reverseWords(s))  # Output: "world hello"

# Example 3:
s = "a good   example"
print(sol.reverseWords(s))  # Output: "example good a"

# Example 4:
s = "  a    b "
print(sol.reverseWords(s))  # Output: "b a"
