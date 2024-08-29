class Solution:
    def removeStones(self, stones):
        def dfs(x):
            visited.add(x)
            for y in row_map[stones[x][0]] + col_map[stones[x][1]]:
                if y not in visited:
                    dfs(y)

        n = len(stones)
        row_map = {}
        col_map = {}
        
        # Build the graph
        for i, (r, c) in enumerate(stones):
            if r not in row_map:
                row_map[r] = []
            if c not in col_map:
                col_map[c] = []
            row_map[r].append(i)
            col_map[c].append(i)
        
        visited = set()
        num_components = 0
        
        # Find all connected components using DFS
        for i in range(n):
            if i not in visited:
                dfs(i)
                num_components += 1
        
        # Number of stones that can be removed is total stones - number of components
        return n - num_components

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    stones1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(solution.removeStones(stones1))  # Output: 5
    
    # Test Case 2
    stones2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    print(solution.removeStones(stones2))  # Output: 3
    
    # Test Case 3
    stones3 = [[0,0]]
    print(solution.removeStones(stones3))  # Output: 0
