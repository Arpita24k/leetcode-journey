class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # Initialize an empty matrix
        matrix = [[0] * n for _ in range(n)]
        # Initial boundaries
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        
        # Continue filling the matrix in spiral order
        while top <= bottom and left <= right:
            # Fill the top row from left to right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            if top <= bottom:
                # Fill the bottom row from right to left
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                # Fill the left column from bottom to top
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix

# Examples
solution = Solution()
print(solution.generateMatrix(3))  # Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(solution.generateMatrix(1))  # Output: [[1]]
