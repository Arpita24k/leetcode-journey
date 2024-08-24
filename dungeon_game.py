class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Start with the princess's cell, which is at bottom-right
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    dungeon1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(solution.calculateMinimumHP(dungeon1))  # Output: 7
    
    # Test Case 2
    dungeon2 = [[0]]
    print(solution.calculateMinimumHP(dungeon2))  # Output: 1
