class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Create a 2D prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        # Step 2: Create the result matrix
        result = [[0] * n for _ in range(m)]
        
        # Step 3: Compute the block sum for each element in the matrix
        for i in range(m):
            for j in range(n):
                # Define the boundaries of the block
                r1 = max(0, i - k)
                r2 = min(m - 1, i + k)
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)
                
                # Convert to 1-based indexing for the prefix sum matrix
                r1 += 1
                r2 += 1
                c1 += 1
                c2 += 1
                
                # Calculate the block sum using the prefix sum matrix
                result[i][j] = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]
        
        return result

# Example usage:
solution = Solution()

# Example 1:
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
k1 = 1
result1 = solution.matrixBlockSum(mat1, k1)
print("Example 1 Output:", result1)

# Example 2:
mat2 = [[1,2,3],[4,5,6],[7,8,9]]
k2 = 2
result2 = solution.matrixBlockSum(mat2, k2)
print("Example 2 Output:", result2)
