from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_list = SortedList()
        
        for i, num in enumerate(nums):
            # Remove the element that's out of the indexDiff range
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            
            # Check if there is an element within the valueDiff range
            # Find the smallest number >= nums[i] - valueDiff
            pos1 = sorted_list.bisect_left(num - valueDiff)
            if pos1 < len(sorted_list) and abs(sorted_list[pos1] - num) <= valueDiff:
                return True
            
            # Add the current number to the sorted list
            sorted_list.add(num)
        
        return False

# Example usage:
solution = Solution()

# Example 1
nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0
print(solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))  # Output: True

# Example 2
nums = [1, 5, 9, 1, 5, 9]
indexDiff = 2
valueDiff = 3
print(solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))  # Output: False
