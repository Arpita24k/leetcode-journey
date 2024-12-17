class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            # Find the minimum value and its first occurrence index
            min_index = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i
            
            # Update the minimum value with the multiplied value
            nums[min_index] *= multiplier
        
        return nums

# Example usage:
solution = Solution()

# Example 1
nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
print(solution.getFinalState(nums, k, multiplier))  # Output: [8, 4, 6, 5, 6]

# Example 2
nums = [1, 2]
k = 3
multiplier = 4
print(solution.getFinalState(nums, k, multiplier))  # Output: [16, 8]
