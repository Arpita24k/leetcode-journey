class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        uf = UnionFind(n)

        # Group indices that satisfy the condition
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    uf.union(i, j)

        # Group values based on the roots
        groups = {}
        for i in range(n):
            root = uf.find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        # Sort values within each group
        result = nums[:]
        for indices in groups.values():
            # Extract and sort the values in this group
            sorted_values = sorted(result[idx] for idx in indices)
            # Replace the original values with the sorted ones
            for idx, val in zip(sorted(indices), sorted_values):
                result[idx] = val

        return result


# ✅ Example Usage:
solution = Solution()

# Test Case 1
nums1 = [1, 5, 3, 9, 8]
limit1 = 2
print(solution.lexicographicallySmallestArray(nums1, limit1))  # Output: [1, 3, 5, 8, 9]

# Test Case 2
nums2 = [1, 7, 6, 18, 2, 1]
limit2 = 3
print(solution.lexicographicallySmallestArray(nums2, limit2))  # Output: [1, 6, 7, 18, 1, 2]

# Test Case 3
nums3 = [1, 7, 28, 19, 10]
limit3 = 3
print(solution.lexicographicallySmallestArray(nums3, limit3))  # Output: [1, 7, 28, 19, 10]
