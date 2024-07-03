from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, word_index):
            # Base case: if we've matched the entire word
            if word_index == len(word):
                return True
            
            # Boundary checks and character match check
            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0])
                    or board[x][y] != word[word_index]):
                return False
            
            # Mark the cell as visited
            temp = board[x][y]
            board[x][y] = '#'
            
            # Explore all four directions
            found = (dfs(x + 1, y, word_index + 1) or
                     dfs(x - 1, y, word_index + 1) or
                     dfs(x, y + 1, word_index + 1) or
                     dfs(x, y - 1, word_index + 1))
            
            # Restore the cell's original value
            board[x][y] = temp
            
            return found
        
        # Iterate over each cell in the grid to start the DFS
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):  # Start the search for the word from cell (i, j)
                    return True
        
        return False

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
    
    print(solution.exist(board1, word1))  # Output: True
    print(solution.exist(board1, word2))  # Output: True
    print(solution.exist(board1, word3))  # Output: False
