class Solution:
    def getRow(self, rowIndex: int):
        # Initialize the first element of the row, which is always 1
        row = [1]
        
        # Compute each subsequent element of the row
        for i in range(1, rowIndex + 1):
            # The next element is derived from the previous one using the formula
            next_value = row[-1] * (rowIndex - i + 1) // i
            row.append(next_value)
        
        return row

# Example usage:
sol = Solution()

# Example 1:
rowIndex1 = 3
print(sol.getRow(rowIndex1))  # Output: [1, 3, 3, 1]

# Example 2:
rowIndex2 = 0
print(sol.getRow(rowIndex2))  # Output: [1]

# Example 3:
rowIndex3 = 1
print(sol.getRow(rowIndex3))  # Output: [1, 1]
