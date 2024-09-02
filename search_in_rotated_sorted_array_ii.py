class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the mid element is the target
            if nums[mid] == target:
                return True
            
            # The tricky part is handling duplicates
            # If we have duplicates, we can just skip the duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # If left to mid is sorted
            elif nums[left] <= nums[mid]:
                # Check if target is in the left part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If mid to right is sorted
            else:
                # Check if target is in the right part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

# Example usage:
nums = [2,5,6,0,0,1,2]
target = 0
solution = Solution()
print(solution.search(nums, target))  # Output: True

nums = [2,5,6,0,0,1,2]
target = 3
print(solution.search(nums, target))  # Output: False
