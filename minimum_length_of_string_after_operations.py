class Solution:
    def minimumLength(self, s):
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        # Process the string from both ends
        while left < right and s[left] == s[right]:
            # Store the current character to be removed
            current_char = s[left]
            
            # Move left pointer inward while characters match
            while left <= right and s[left] == current_char:
                left += 1
            
            # Move right pointer inward while characters match
            while left <= right and s[right] == current_char:
                right -= 1
        
        # Length of the remaining string
        return right - left + 1

# ✅ Example Usage
solution = Solution()

# Test Case 1
s1 = "abaacbcbb"
print(solution.minimumLength(s1))  # Output: 5

# Test Case 2
s2 = "aa"
print(solution.minimumLength(s2))  # Output: 2

# Test Case 3
s3 = "abc"
print(solution.minimumLength(s3))  # Output: 3

# Test Case 4
s4 = "aabccbaa"
print(solution.minimumLength(s4))  # Output: 0
