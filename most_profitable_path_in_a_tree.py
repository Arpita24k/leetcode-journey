from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        graph = defaultdict(list)
        
        # Step 1: Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Compute Bob's path and visit times
        bob_time = {i: float('inf') for i in range(n)}
        def dfs_bob(node, parent, depth):
            if node == 0:
                bob_time[node] = depth  # Bob reaches node 0 at depth
                return True
            for neighbor in graph[node]:
                if neighbor != parent and dfs_bob(neighbor, node, depth + 1):
                    bob_time[node] = depth
                    return True
            return False
        
        dfs_bob(bob, -1, 0)  # Compute Bob's visiting times

        # Step 3: DFS for Alice to find max income
        def dfs_alice(node, parent, depth, income):
            # Alice is at `node`, depth tracks the current depth
            if depth < bob_time[node]:  # Alice reaches first
                income += amount[node]
            elif depth == bob_time[node]:  # Both arrive together
                income += amount[node] // 2
            
            # Base case: Leaf node
            if len(graph[node]) == 1 and node != 0:
                return income

            max_profit = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_profit = max(max_profit, dfs_alice(neighbor, node, depth + 1, income))
            
            return max_profit

        return dfs_alice(0, -1, 0, 0)
