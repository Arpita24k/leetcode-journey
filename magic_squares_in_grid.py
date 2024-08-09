# Magic Squares In Grid

class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagic(grid, r, c):
            # Check if the subgrid contains all distinct numbers from 1 to 9
            s = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or num in s:
                        return False
                    s.add(num)
            
            # Check row sums, column sums, and diagonal sums
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and  # row 1
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and  # row 2
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and  # row 3
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and  # column 1
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and  # column 2
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and  # column 3
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and  # diagonal 1
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):  # diagonal 2
                return True
            return False
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # Iterate through each possible 3x3 subgrid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] == 5 and isMagic(grid, r, c):  # Center must be 5 in a magic square
                    count += 1
        
        return count

# Example usage:
grid1 = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
solution = Solution()
print(solution.numMagicSquaresInside(grid1))  # Output: 1

grid2 = [[8]]
print(solution.numMagicSquaresInside(grid2))  # Output: 0
