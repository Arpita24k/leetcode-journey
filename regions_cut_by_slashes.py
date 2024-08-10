class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def get_count(self):
        return self.count

class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        uf = UnionFind(4 * n * n)  # 4 triangles per cell

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)  # root of the current cell

                # Connect triangles within a single cell
                if grid[i][j] == '/':
                    uf.union(root + 0, root + 3)  # Connect 0 to 3
                    uf.union(root + 1, root + 2)  # Connect 1 to 2
                elif grid[i][j] == '\\':
                    uf.union(root + 0, root + 1)  # Connect 0 to 1
                    uf.union(root + 2, root + 3)  # Connect 2 to 3
                else:  # ' '
                    uf.union(root + 0, root + 1)  # Connect all parts
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)

                # Connect triangles between adjacent cells
                # Right
                if j + 1 < n:
                    uf.union(root + 1, 4 * (i * n + (j + 1)) + 3)
                # Down
                if i + 1 < n:
                    uf.union(root + 2, 4 * ((i + 1) * n + j) + 0)

        # Count regions, which are the number of disjoint sets left
        return uf.get_count()

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    grid1 = [" /","/ "]
    print(solution.regionsBySlashes(grid1))  # Output: 2
    
    # Test Case 2
    grid2 = [" /","  "]
    print(solution.regionsBySlashes(grid2))  # Output: 1
    
    # Test Case 3
    grid3 = ["/\\","\\/"]
    print(solution.regionsBySlashes(grid3))  # Output: 5
