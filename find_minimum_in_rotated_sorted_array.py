class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # If the middle element is greater than the rightmost element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half including mid
                right = mid
        
        # After the loop, left points to the minimum element
        return nums[left]

# Example usage:
sol = Solution()

# Example 1:
nums1 = [3, 4, 5, 1, 2]
print(sol.findMin(nums1))  # Output: 1

# Example 2:
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(sol.findMin(nums2))  # Output: 0

# Example 3:
nums3 = [11, 13, 15, 17]
print(sol.findMin(nums3))  # Output: 11
