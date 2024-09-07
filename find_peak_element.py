class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is smaller than the next element, search in the right half
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # If the middle element is greater than or equal to the next element, search in the left half
                right = mid
        
        # At the end, left and right will converge at the peak element
        return left

# Example usage:
sol = Solution()
print(sol.findPeakElement([1, 2, 3, 1]))  # Output: 2
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5
