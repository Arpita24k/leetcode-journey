class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Initialize the isPalindrome table
        isPalindrome = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            isPalindrome[i][i] = True
        
        # Fill the isPalindrome table
        for length in range(2, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or isPalindrome[i + 1][j - 1]:
                        isPalindrome[i][j] = True
        
        # Initialize dp array
        dp = [float('inf')] * n
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if isPalindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "aab"
    print(solution.minCut(s1))  # Output: 1
    
    # Test Case 2
    s2 = "a"
    print(solution.minCut(s2))  # Output: 0
    
    # Test Case 3
    s3 = "ab"
    print(solution.minCut(s3))  # Output: 1
