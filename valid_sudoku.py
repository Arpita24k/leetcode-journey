from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create data structures to keep track of seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    # Calculate the index for the sub-box
                    sub_box_index = (r // 3) * 3 + (c // 3)
                    
                    # Check if the number has already been seen in the row, column, or sub-box
                    if num in rows[r] or num in columns[c] or num in sub_boxes[sub_box_index]:
                        return False
                    
                    # Add the number to the sets for the row, column, and sub-box
                    rows[r].add(num)
                    columns[c].add(num)
                    sub_boxes[sub_box_index].add(num)
        
        # If all checks pass, the board is valid
        return True

# Example usage
solution = Solution()

board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(solution.isValidSudoku(board1))  # Output: True
print(solution.isValidSudoku(board2))  # Output: False
