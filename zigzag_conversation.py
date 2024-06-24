class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            # Change direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down in rows
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)

# Example usage
s1 = "PAYPALISHIRING"
numRows1 = 3
print(Solution().convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(Solution().convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

s3 = "A"
numRows3 = 1
print(Solution().convert(s3, numRows3))  # Output: "A"
