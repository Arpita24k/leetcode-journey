class Solution:
    def minOperations(self, grid, x):
        # Flatten the grid
        flat = [cell for row in grid for cell in row]
        base = flat[0]

        # Check modulo condition
        for val in flat:
            if (val - base) % x != 0:
                return -1

        # Convert all values to number of steps from base
        steps = [(val - base) // x for val in flat]

        # Find the median step value
        steps.sort()
        median = steps[len(steps) // 2]

        # Compute total operations
        return sum(abs(s - median) for s in steps)
