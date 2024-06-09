class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Dictionary to store the count of each character
        char_count = {}
        
        # First pass: Count the occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Second pass: Find the first character with a count of 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character found, return -1
        return -1

# Example usage
solution = Solution()

s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

print(solution.firstUniqChar(s1))  # Output: 0
print(solution.firstUniqChar(s2))  # Output: 2
print(solution.firstUniqChar(s3))  # Output: -1
