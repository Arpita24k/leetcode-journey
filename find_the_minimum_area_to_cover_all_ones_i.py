class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        # Initialize boundaries for the rectangle
        top, bottom = float('inf'), float('-inf')
        left, right = float('inf'), float('-inf')
        
        # Traverse the grid to find the extreme boundaries
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
        
        # Calculate the area
        height = bottom - top + 1
        width = right - left + 1
        return height * width

# Example usage:
solution = Solution()

# Example 1:
grid = [[0,1,0],[1,0,1]]
print(solution.minimumArea(grid))  # Output: 6

# Example 2:
grid = [[1,0],[0,0]]
print(solution.minimumArea(grid))  # Output: 1
