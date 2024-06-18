class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths of s and t are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Dictionary to count occurrences of each character in s
        char_count_s = {}
        # Dictionary to count occurrences of each character in t
        char_count_t = {}
        
        # Count occurrences of each character in s
        for char in s:
            if char in char_count_s:
                char_count_s[char] += 1
            else:
                char_count_s[char] = 1
        
        # Count occurrences of each character in t
        for char in t:
            if char in char_count_t:
                char_count_t[char] += 1
            else:
                char_count_t[char] = 1
        
        # Compare the two dictionaries
        return char_count_s == char_count_t

# Example usage
solution = Solution()

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print(solution.isAnagram(s1, t1))  # Output: true
print(solution.isAnagram(s2, t2))  # Output: false
