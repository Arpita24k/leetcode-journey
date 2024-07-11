class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True  # Puzzle solved
        
        row, col = empty
        
        for num in '123456789':
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = '.'  # Backtrack
        
        return False

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def is_valid(self, board, row, col, num):
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 sub-box
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == num:
                    return False
        
        return True

# Example usage:
solution = Solution()

board = [
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

solution.solveSudoku(board)

for row in board:
    print(row)
