class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, path + [nums[i]])

        nums.sort()
        res = []
        backtrack(0, [])
        return res

# Test cases
solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))  # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(solution.subsetsWithDup([0]))         # Output: [[],[0]]
