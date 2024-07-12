class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(remaining, comb, start):
            if remaining == 0:
                result.append(list(comb))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remaining - candidates[i], comb, i)
                comb.pop()
        
        result = []
        backtrack(target, [], 0)
        return result

    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

# Example usage for combinationSum:
solution = Solution()
candidates1 = [2, 3, 6, 7]
target1 = 7
print(solution.combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

# Example usage for firstMissingPositive:
nums = [3, 4, -1, 1]
print(solution.firstMissingPositive(nums))  # Output: 2
