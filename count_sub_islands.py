class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(r, c):
            # Base case: If the cell is out of bounds or water, return True.
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            # Mark this cell as visited in grid2
            grid2[r][c] = 0
            
            # Check if this cell is water in grid1. If so, it's not a sub-island
            is_sub_island = grid1[r][c] == 1
            
            # Visit all four directions
            is_sub_island &= dfs(r + 1, c)
            is_sub_island &= dfs(r - 1, c)
            is_sub_island &= dfs(r, c + 1)
            is_sub_island &= dfs(r, c - 1)
            
            return is_sub_island
        
        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:  # Found an unvisited island part in grid2
                    if dfs(r, c):
                        count += 1
                        
        return count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    grid1 = [
        [1,1,1,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,1,1]
    ]
    grid2 = [
        [1,1,1,0,0],
        [0,0,1,1,1],
        [0,1,0,0,0],
        [1,0,1,1,0],
        [0,1,0,1,0]
    ]
    print(solution.countSubIslands(grid1, grid2))  # Output: 3

    grid1 = [
        [1,0,1,0,1],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [1,0,1,0,1]
    ]
    grid2 = [
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [1,0,0,0,1]
    ]
    print(solution.countSubIslands(grid1, grid2))  # Output: 2
