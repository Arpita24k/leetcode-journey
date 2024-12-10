class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        # Step 2: Backtracking on the board
        def backtrack(node, row, col, path):
            char = board[row][col]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            path += char
            
            # Check if we found a word
            if next_node.is_end_of_word:
                result.add(path)
                next_node.is_end_of_word = False  # Avoid duplicate matches
            
            # Mark the cell as visited
            board[row][col] = "#"
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    backtrack(next_node, nr, nc, path)
            
            # Restore the cell
            board[row][col] = char
        
        # Dimensions of the board
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        result = set()
        
        # Start backtracking from each cell
        for i in range(m):
            for j in range(n):
                backtrack(root, i, j, "")
        
        return list(result)

# Example usage:
solution = Solution()

# Example 1
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(solution.findWords(board, words))  # Output: ["eat","oath"]

# Example 2
board = [["a","b"],["c","d"]]
words = ["abcb"]
print(solution.findWords(board, words))  # Output: []
