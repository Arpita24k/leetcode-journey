class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        # Convert dictionary into a set for faster lookups
        word_set = set(dictionary)
        
        # Initialize the DP array with large values
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: No characters mean 0 extra characters
        
        # Iterate over the string
        for i in range(1, n + 1):
            # Check every possible word ending at index i-1
            for j in range(i):
                substring = s[j:i]
                # If substring is in the dictionary, update dp[i]
                if substring in word_set:
                    dp[i] = min(dp[i], dp[j])
                else:
                    # If not, count this as extra characters
                    dp[i] = min(dp[i], dp[j] + i - j)
        
        # Return the answer for the full string
        return dp[n]

# Example usage:
solution = Solution()

# Example 1:
s = "leetscode"
dictionary = ["leet","code","leetcode"]
print(solution.minExtraChar(s, dictionary))  # Output: 1

# Example 2:
s = "sayhelloworld"
dictionary = ["hello", "world"]
print(solution.minExtraChar(s, dictionary))  # Output: 3
