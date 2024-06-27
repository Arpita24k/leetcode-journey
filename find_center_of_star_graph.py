class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # The center node must be one of the nodes in the first edge
        # It must appear in the second edge too if it is the center
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]

# Example usage
solution = Solution()

# Test case 1
edges1 = [[1, 2], [2, 3], [4, 2]]
print(solution.findCenter(edges1))  # Output: 2

# Test case 2
edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
print(solution.findCenter(edges2))  # Output: 1
