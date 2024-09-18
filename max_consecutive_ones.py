class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count

# Example usage:
solution = Solution()

# Example 1:
nums = [1,1,0,1,1,1]
print(solution.findMaxConsecutiveOnes(nums))  # Output: 3

# Example 2:
nums = [1,0,1,1,0,1]
print(solution.findMaxConsecutiveOnes(nums))  # Output: 2
