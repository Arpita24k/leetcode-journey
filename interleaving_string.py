class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        # Early return if lengths don't add up
        if m + n != len(s3):
            return False
        
        # Create a DP table with (n+1) elements
        dp = [False] * (n + 1)
        
        # Initialize the DP table
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[n]

# Example usage
solution = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(solution.isInterleave(s1, s2, s3))  # Output: true

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(solution.isInterleave(s1, s2, s3))  # Output: false

s1 = ""
s2 = ""
s3 = ""
print(solution.isInterleave(s1, s2, s3))  # Output: true
