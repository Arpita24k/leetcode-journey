from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        # Initialize the left pointer at 1 (second position)
        l = 1
        
        # Iterate through the list starting from the second element
        for r in range(1, len(nums)):
            # If the current element is not the same as the previous one
            if nums[r] != nums[r - 1]:
                # Assign the current element to the left pointer position
                nums[l] = nums[r]
                # Move the left pointer to the next position
                l += 1
        
        # Return the count of unique elements
        return l, nums[:l]

# Example usage
solution = Solution()
nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
count, unique_nums = solution.removeDuplicates(nums)
print("Count of unique elements:", count)
print("Unique elements:", unique_nums)
