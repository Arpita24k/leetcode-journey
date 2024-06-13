
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given n x n 2D matrix by 90 degrees clockwise in place.
        """
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage
solution = Solution()

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution.rotate(matrix1)
print("Rotated matrix1:", matrix1)
