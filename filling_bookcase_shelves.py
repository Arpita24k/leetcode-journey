class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)  # dp[i] represents the minimum height for the first i books
        
        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float('inf')
            # Try to place books[j:i] on the same shelf
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
        
        return dp[n]

# Example usage:
sol = Solution()
print(sol.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))  # Output: 6
print(sol.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))  # Output: 4
