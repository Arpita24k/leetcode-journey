class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Compare the filtered list with its reverse
        return filtered_chars == filtered_chars[::-1]

# Example usage
solution = Solution()

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(solution.isPalindrome(s1))  # Output: true
print(solution.isPalindrome(s2))  # Output: false
print(solution.isPalindrome(s3))  # Output: true
