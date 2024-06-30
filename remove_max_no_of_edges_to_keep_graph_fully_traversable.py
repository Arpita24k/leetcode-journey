class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
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
            return True
        return False
    
    def connected(self):
        return self.count == 1

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        # Initialize Union-Find for Alice and Bob
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        uf_both = UnionFind(n)
        
        total_edges_used = 0
        
        # Process type 3 edges first (usable by both Alice and Bob)
        for edge_type, u, v in edges:
            if edge_type == 3:
                if uf_both.union(u - 1, v - 1):
                    uf_alice.union(u - 1, v - 1)
                    uf_bob.union(u - 1, v - 1)
                    total_edges_used += 1
        
        # Process type 1 edges (usable by Alice only)
        for edge_type, u, v in edges:
            if edge_type == 1:
                if uf_alice.union(u - 1, v - 1):
                    total_edges_used += 1
        
        # Process type 2 edges (usable by Bob only)
        for edge_type, u, v in edges:
            if edge_type == 2:
                if uf_bob.union(u - 1, v - 1):
                    total_edges_used += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if uf_alice.connected() and uf_bob.connected():
            return len(edges) - total_edges_used
        else:
            return -1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n1 = 4
    edges1 = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    n2 = 4
    edges2 = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    n3 = 4
    edges3 = [[3,2,3],[1,1,2],[2,3,4]]

    print(solution.maxNumEdgesToRemove(n1, edges1))  # Output: 2
    print(solution.maxNumEdgesToRemove(n2, edges2))  # Output: 0
    print(solution.maxNumEdgesToRemove(n3, edges3))  # Output: -1
