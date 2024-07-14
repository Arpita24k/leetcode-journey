class Solution:
    def solveNQueens(self, n: int):
        """
        Function to solve the N-Queens puzzle and return all distinct solutions.
        
        Args:
        n: Integer, the size of the chessboard (n x n).
        
        Returns:
        List of lists containing distinct board configurations.
        """
        def is_safe(board, row, col):
            # Check this column on upper side
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check upper diagonal on left side
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check upper diagonal on right side
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solve(board, row):
            # If all queens are placed
            if row == n:
                # Convert the board to the required format and add to solutions
                solutions.append(["".join(row) for row in board])
                return
            
            # Consider this row and try placing this queen in all columns one by one
            for col in range(n):
                if is_safe(board, row, col):
                    # Place this queen in board[row][col]
                    board[row][col] = 'Q'
                    # Recur to place rest of the queens
                    solve(board, row + 1)
                    # If placing queen in board[row][col] doesn't lead to a solution
                    # then remove queen from board[row][col]
                    board[row][col] = '.'
        
        # Initialize the board
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        # Start the solving process from the first row
        solve(board, 0)
        return solutions

# Example usage
solution = Solution()
print(solution.solveNQueens(4))  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(1))  # Output: [["Q"]]
