class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            return not (cols[col] or hills[row - col] or dales[row + col])  # Check if the position (row, col) is safe
        
        def place_queen(row, col):
            cols[col] = 1  # Mark the column as under attack
            hills[row - col] = 1  # Mark the "hill" diagonal as under attack
            dales[row + col] = 1  # Mark the "dale" diagonal as under attack
        
        def remove_queen(row, col):
            cols[col] = 0  # Unmark the column
            hills[row - col] = 0  # Unmark the "hill" diagonal
            dales[row + col] = 0  # Unmark the "dale" diagonal
        
        def backtrack(row = 0, count = 0):
            for col in range(n):  # Try to place a queen in each column of the current row
                if is_not_under_attack(row, col):  # If the position is safe
                    place_queen(row, col)  # Place the queen
                    if row + 1 == n:
                        count += 1  # Found a valid solution
                    else:
                        count = backtrack(row + 1, count)  # Recurse to the next row
                    remove_queen(row, col)  # Backtrack
            return count  # Return the count of solutions
        
        cols = [0] * n  # Initialize column attack tracker
        hills = [0] * (2 * n - 1)  # Initialize "hill" diagonal attack tracker
        dales = [0] * (2 * n - 1)  # Initialize "dale" diagonal attack tracker
        
        return backtrack()  # Start backtracking from the first row

# Example usage:
sol = Solution()
print(sol.totalNQueens(4))  # Output: 2
print(sol.totalNQueens(1))  # Output: 1
