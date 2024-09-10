class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Start at the top-right corner
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        
        # Traverse the matrix
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down
        
        return False

# Example usage:
solution = Solution()

# Example 1
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
print(solution.searchMatrix(matrix, target))  # Output: True

# Example 2
target = 20
print(solution.searchMatrix(matrix, target))  # Output: False
