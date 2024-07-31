class Solution:
    def subsets(self, nums: list) -> list:
        def backtrack(start, path):
            result.append(path[:])  # Append a copy of the current path to the result
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include the current element in the path
                backtrack(i + 1, path)  # Recurse with the next element
                path.pop()  # Backtrack and remove the last element

        result = []  # Initialize the result list
        backtrack(0, [])  # Start backtracking from index 0 with an empty path
        return result  # Return the final result list

# Example usage:
sol = Solution()
print(sol.subsets([1, 2, 3]))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(sol.subsets([0]))  # Output: [[], [0]]
