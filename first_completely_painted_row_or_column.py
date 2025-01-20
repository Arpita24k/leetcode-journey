class Solution:
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        
        # Map each value in mat to its coordinates (row, col)
        value_to_position = {}
        for r in range(m):
            for c in range(n):
                value_to_position[mat[r][c]] = (r, c)
        
        # Initialize row and column counters
        row_count = [0] * m
        col_count = [0] * n
        
        # Process each value in arr
        for i, value in enumerate(arr):
            r, c = value_to_position[value]  # Get the coordinates
            row_count[r] += 1
            col_count[c] += 1
            
            # Check if the row or column is fully painted
            if row_count[r] == n or col_count[c] == m:
                return i
        
        return -1  # Should not reach here if constraints are satisfied
