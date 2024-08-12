class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        
        # Initialize the result list with the first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            # Start each row with a 1
            row = [1]
            # Compute the inner elements of the row
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # End each row with a 1
            row.append(1)
            # Add the row to the triangle
            triangle.append(row)
        
        return triangle

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    numRows = 5
    print(solution.generate(numRows))  # Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
    
    # Test Case 2
    numRows = 1
    print(solution.generate(numRows))  # Output: [[1]]
