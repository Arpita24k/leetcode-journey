#Spiral Matrix III

class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        # Define the directions for movement in the order: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize the list to keep track of visited positions
        visited = []
        # Calculate the total number of cells in the grid
        total_cells = rows * cols
        # Initial steps to move in the current direction
        steps = 1
        # Used to determine when to increment the steps
        step_increment = 0
        # Starting position
        x, y = rStart, cStart
        # Start by moving right
        direction_idx = 0

        # Continue moving until all cells are visited
        while len(visited) < total_cells:
            # Move in the current direction for the current number of steps
            for _ in range(steps):
                # If within grid bounds, add the position to the visited list
                if 0 <= x < rows and 0 <= y < cols:
                    visited.append([x, y])
                # Move to the next cell in the current direction
                x += directions[direction_idx][0]
                y += directions[direction_idx][1]
            # Change direction after completing the current steps
            direction_idx = (direction_idx + 1) % 4
            
            # Increment step count after every two turns
            step_increment += 1
            if step_increment % 2 == 0:
                steps += 1

        return visited

# Example usage:
rows = 5
cols = 6
rStart = 1
cStart = 4
solution = Solution()
print(solution.spiralMatrixIII(rows, cols, rStart, cStart))
