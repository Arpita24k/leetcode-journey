class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Example usage
solution = Solution()

# Test case 1
nums1 = [1, 3, 5, 6]
target1 = 5
print(solution.searchInsert(nums1, target1))  # Output: 2

# Test case 2
nums2 = [1, 3, 5, 6]
target2 = 2
print(solution.searchInsert(nums2, target2))  # Output: 1

# Test case 3
nums3 = [1, 3, 5, 6]
target3 = 7
print(solution.searchInsert(nums3, target3))  # Output: 4
