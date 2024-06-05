class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

# Example usage:
solution = Solution()

nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
