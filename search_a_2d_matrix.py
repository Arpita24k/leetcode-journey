# Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Example usage
solution = Solution()
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13

print(solution.searchMatrix(matrix1, target1))  # Output: true
print(solution.searchMatrix(matrix2, target2))  # Output: false
