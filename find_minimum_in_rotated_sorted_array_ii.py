#Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element, the minimum must be to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than the rightmost, the minimum is in the left half or at mid
            elif nums[mid] < nums[right]:
                right = mid
            # If nums[mid] == nums[right], we can't be sure, so reduce the right bound by 1
            else:
                right -= 1
        
        # The loop ends when left == right, which is the index of the minimum element
        return nums[left]

# Example usage:
# solution = Solution()
# print(solution.findMin([1, 3, 5]))  # Output: 1
# print(solution.findMin([2, 2, 2, 0, 1]))  # Output: 0
