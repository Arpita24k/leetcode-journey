from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in the magazine
        magazine_count = Counter(magazine)
        
        # Iterate through each character in the ransomNote
        for char in ransomNote:
            # If the character is not in magazine or is used up, return False
            if magazine_count[char] <= 0:
                return False
            # Otherwise, decrement the count of the character
            magazine_count[char] -= 1
            
        # If we can construct the ransomNote, return True
        return True

# Example usage:
solution = Solution()
print(solution.canConstruct("a", "b"))         # Output: False
print(solution.canConstruct("aa", "ab"))       # Output: False
print(solution.canConstruct("aa", "aab"))      # Output: True
