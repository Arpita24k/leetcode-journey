class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create the augmented string: s + "#" + reverse(s)
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        
        # Compute the KMP table (prefix function)
        n = len(new_s)
        lps = [0] * n  # LPS (Longest Prefix Suffix) array
        
        # Fill the LPS array
        for i in range(1, n):
            j = lps[i - 1]  # Length of the previous longest prefix suffix
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # The length of the longest palindromic prefix is stored in lps[-1]
        longest_palindrome_prefix_len = lps[-1]
        
        # Add the remaining suffix (the part of s that isn't part of the palindrome) reversed at the front
        suffix_to_add = rev_s[:len(s) - longest_palindrome_prefix_len]
        return suffix_to_add + s

# Example usage:
solution = Solution()

# Testcase 1
s1 = "aacecaaa"
print(f"Output for s = '{s1}': {solution.shortestPalindrome(s1)}")  # Expected Output: "aaacecaaa"

# Testcase 2
s2 = "abcd"
print(f"Output for s = '{s2}': {solution.shortestPalindrome(s2)}")  # Expected Output: "dcbabcd"
