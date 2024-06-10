from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize the position for the next non-zero element
        next_non_zero_index = 0

        # Iterate through the list
        for i in range(len(nums)):
            if nums[i] != 0:
                
                # Swap the elements
                nums[next_non_zero_index], nums[i] = nums[i], nums[next_non_zero_index]
                
                # Move to the next position for non-zero element
                next_non_zero_index += 1

# Example usage
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print("Modified nums:", nums)
