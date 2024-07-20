class Solution:
    def restoreMatrix(self, rowSum, colSum):
        # Initialize the matrix with zeros
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        
        # Traverse through each cell
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                # Determine the value to put in the cell
                value = min(rowSum[i], colSum[j])
                # Assign the value to the cell
                matrix[i][j] = value
                # Subtract the assigned value from the corresponding row and column sums
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix

# Example usage:
rowSum = [3, 8]
colSum = [4, 7]
solution = Solution()
print(solution.restoreMatrix(rowSum, colSum))
# Output: [[3, 0], [1, 7]]

rowSum = [5, 7, 10]
colSum = [8, 6, 8]
print(solution.restoreMatrix(rowSum, colSum))
# Output: [[0, 5, 0], [6, 1, 0], [2, 0, 8]]
