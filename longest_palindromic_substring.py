class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindromes
            l1, r1 = expand_around_center(i, i)
            # Even length palindromes
            l2, r2 = expand_around_center(i, i + 1)

            # Update the start and end indices if a longer palindrome is found
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

# Example usage:
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # Output: "bb"
