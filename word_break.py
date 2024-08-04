class Solution:
    def wordBreak(self, s, wordDict):
        # Create a set for quick look-up of words
        word_set = set(wordDict)
        
        # Initialize the DP array
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        # Fill the DP array
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[:j] can be segmented and s[j:i] is a word, then s[:i] can be segmented
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Example usage
solution = Solution()

s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(solution.wordBreak(s1, wordDict1))  # Output: True

s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print(solution.wordBreak(s2, wordDict2))  # Output: True

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s3, wordDict3))  # Output: False
