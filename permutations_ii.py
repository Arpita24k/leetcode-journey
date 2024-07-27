class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
                return
            
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        nums.sort()
        result = []
        backtrack()
        return result

# Examples
solution = Solution()
print(solution.permuteUnique([1, 1, 2]))  # Output: [[1,1,2], [1,2,1], [2,1,1]]
print(solution.permuteUnique([1, 2, 3]))  # Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
