class Solution:
    def minDays(self, grid):
        def count_islands():
            """Count the number of islands in the grid using DFS."""
            visited = [[False] * n for _ in range(m)]  # Track visited cells
            island_count = 0  # Initialize island count

            def dfs(x, y):
                """Perform DFS to mark all cells in the current island."""
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return  # Skip invalid or already visited cells
                visited[x][y] = True  # Mark cell as visited
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Explore all 4 directions
                    dfs(x + dx, y + dy)  # DFS in each direction

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        island_count += 1  # Found a new island
                        dfs(i, j)  # Mark all cells in this island
            return island_count  # Return total number of islands

        def is_disconnected():
            """Check if the grid is disconnected (i.e., has more than one island)."""
            return count_islands() != 1  # If islands count isn't 1, it's disconnected

        m, n = len(grid), len(grid[0])  # Get dimensions of the grid

        if is_disconnected():
            return 0  # If already disconnected, return 0 days

        # Try removing one cell to disconnect the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Only consider land cells
                    grid[i][j] = 0  # Temporarily remove this cell
                    if is_disconnected():
                        return 1  # If grid becomes disconnected, return 1 day
                    grid[i][j] = 1  # Revert the cell back to land

        # Try removing two cells to disconnect the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Only consider land cells
                    grid[i][j] = 0  # Temporarily remove this cell
                    for x, y in [(i + dx, j + dy) for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]]:  # Check neighboring cells
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:  # If valid and is a land cell
                            grid[x][y] = 0  # Temporarily remove the neighboring cell
                            if is_disconnected():
                                return 2  # If grid becomes disconnected, return 2 days
                            grid[x][y] = 1  # Revert the neighboring cell back to land
                    grid[i][j] = 1  # Revert the first cell back to land

        return 2  # If no disconnection after 2 removals, return 2 days

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    print(solution.minDays(grid1))  # Output: 2
    
    # Test Case 2
    grid2 = [[1,1]]
    print(solution.minDays(grid2))  # Output: 2
