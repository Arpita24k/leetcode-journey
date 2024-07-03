class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string has one way to be decoded
        
        for i in range(1, n + 1):
            # Single character decoding
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Two character decoding
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        
        return dp[n]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("12"))  # Output: 2
    print(solution.numDecodings("226"))  # Output: 3
    print(solution.numDecodings("06"))  # Output: 0
