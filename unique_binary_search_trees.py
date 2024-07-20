class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize the array to store the number of unique BSTs for each number of nodes
        G = [0] * (n + 1)
        # Base cases
        G[0] = 1
        G[1] = 1

        # Fill the DP table
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]

# Example Usage:
solution = Solution()
print(solution.numTrees(3))  # Output: 5
print(solution.numTrees(1))  # Output: 1
