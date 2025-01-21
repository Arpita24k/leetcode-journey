class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        
        # Precompute prefix sums for the bottom row
        prefix_bottom = [0] * n
        prefix_bottom[0] = grid[1][0]
        for i in range(1, n):
            prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i]
        
        # Precompute suffix sums for the top row
        suffix_top = [0] * n
        suffix_top[-1] = grid[0][-1]
        for i in range(n - 2, -1, -1):
            suffix_top[i] = suffix_top[i + 1] + grid[0][i]
        
        # Minimize the maximum points collected by the second robot
        result = float('inf')
        for i in range(n):
            # Points remaining in the top row to the right of the split
            points_top = suffix_top[i + 1] if i + 1 < n else 0
            # Points remaining in the bottom row to the left of the split
            points_bottom = prefix_bottom[i - 1] if i - 1 >= 0 else 0
            
            # The second robot collects the max of the two
            second_robot_points = max(points_top, points_bottom)
            result = min(result, second_robot_points)
        
        return result

# ✅ Example Usage:
solution = Solution()

# Test Case 1
grid1 = [[2, 5, 4], [1, 5, 1]]
print(solution.gridGame(grid1))  # Output: 4

# Test Case 2
grid2 = [[3, 3, 1], [8, 5, 2]]
print(solution.gridGame(grid2))  # Output: 4

# Test Case 3
grid3 = [[1, 3, 1, 15], [1, 3, 3, 1]]
print(solution.gridGame(grid3))  # Output: 7
