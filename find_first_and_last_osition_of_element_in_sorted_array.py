#Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1  # Move left to find the first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1  # Move right to find the last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos
        
        first = findFirst(nums, target)
        if first == -1:  # If the target is not found, no need to search for the last
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    print(solution.searchRange(nums1, target1))  # Output: [3, 4]
    
    # Test Case 2
    nums2 = [5,7,7,8,8,10]
    target2 = 6
    print(solution.searchRange(nums2, target2))  # Output: [-1, -1]
    
    # Test Case 3
    nums3 = []
    target3 = 0
    print(solution.searchRange(nums3, target3))  # Output: [-1, -1]
