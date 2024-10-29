class Solution:
    def maxMoves(self, grid):
        m, n = len(grid), len(grid[0])  # Get dimensions of the grid
        memo = [[-1] * n for _ in range(m)]  # Initialize memoization table with -1

        def dfs(row, col):
            # Return the precomputed result if already visited
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_moves = 0  # Initialize the maximum moves possible from this cell

            # Explore all possible moves (top-right, right, bottom-right)
            for dr in [-1, 0, 1]:
                new_row, new_col = row + dr, col + 1
                # Check boundaries and if the next cell value is greater
                if 0 <= new_row < m and new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))  # Recursive DFS
            
            memo[row][col] = max_moves  # Store result in memo table
            return max_moves

        max_total_moves = 0  # Track the maximum moves over all starting points
        for row in range(m):
            max_total_moves = max(max_total_moves, dfs(row, 0))  # Start DFS from each cell in the first column
        
        return max_total_moves  # Return the maximum moves found

# Example usage:
solution = Solution()

# Example 1 from the prompt
grid1 = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print("Example 1 Output:", solution.maxMoves(grid1))  # Expected Output: 3

# Example 2 from the prompt
grid2 = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
print("Example 2 Output:", solution.maxMoves(grid2))  # Expected Output: 0
