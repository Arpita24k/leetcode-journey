class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Keep track of the largest square side length
                    max_side = max(max_side, dp[i][j])
        
        # The area of the largest square is max_side^2
        return max_side * max_side

# Example usage:
solution = Solution()

# Example 1:
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(solution.maximalSquare(matrix))  # Output: 4

# Example 2:
matrix = [["0","1"],["1","0"]]
print(solution.maximalSquare(matrix))  # Output: 1

# Example 3:
matrix = [["0"]]
print(solution.maximalSquare(matrix))  # Output: 0
