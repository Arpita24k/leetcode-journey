class Solution:
    def countPalindromicSubsequence(self, s):
        """
        Count the number of unique palindromic subsequences of length 3.
        """
        unique_palindromes = set()
        
        # Iterate through each possible middle character
        for mid in range(1, len(s) - 1):  # Avoid the first and last index
            left_chars = set()
            right_chars = set(s[mid + 1:])  # Set of characters to the right of mid
            
            # Traverse from start to mid to get unique left characters
            for left in range(mid):
                left_chars.add(s[left])
            
            # Check for palindromes where left and right characters match
            for char in left_chars:
                if char in right_chars:
                    unique_palindromes.add(char + s[mid] + char)

        # Return the number of unique palindromic subsequences
        return len(unique_palindromes)


# Example usage:
solution = Solution()

# Test Case 1
s1 = "aabca"
print(solution.countPalindromicSubsequence(s1))  # Output: 3

# Test Case 2
s2 = "adc"
print(solution.countPalindromicSubsequence(s2))  # Output: 0

# Test Case 3
s3 = "bbcbaba"
print(solution.countPalindromicSubsequence(s3))  # Output: 4
