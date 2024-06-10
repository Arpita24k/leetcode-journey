class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0
        
        # Get the lengths of haystack and needle
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        # Loop through the haystack
        for i in range(len_haystack - len_needle + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i+len_needle] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1

# Example usage
solution = Solution()

haystack1 = "sadbutsad"
needle1 = "sad"

haystack2 = "leetcode"
needle2 = "leeto"

print(solution.strStr(haystack1, needle1))  # Output: 0
print(solution.strStr(haystack2, needle2))  # Output: -1
