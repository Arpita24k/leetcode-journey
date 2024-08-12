class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'E'  # Mark 'O' as 'E' to indicate it's connected to the boundary
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Explore in all 4 directions
                dfs(i + x, j + y)
        
        # Step 1: Mark the non-surrounded 'O's by starting from the boundary
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m-1][j] == 'O': dfs(m-1, j)
        
        # Step 2: Flip all remaining 'O's to 'X' (these are surrounded)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Step 3: Restore the marked 'O's (those not surrounded)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
        
        return board  # Return is optional, as the board is modified in place

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    
    solution.solve(board)
    print(board)  # Output should match the expected result
