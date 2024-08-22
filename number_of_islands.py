class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(i, j):
            # If we're out of bounds or on water ('0'), return immediately
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            # Mark the land as visited by setting it to '0'
            grid[i][j] = '0'
            
            # Explore all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Start a DFS to mark the entire island
                    dfs(i, j)
                    island_count += 1
        
        return island_count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(solution.numIslands(grid1))  # Output: 1
    
    # Test Case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(solution.numIslands(grid2))  # Output: 3
