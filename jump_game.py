class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reachable = 0  # The farthest index we can reach

        for i, jump in enumerate(nums):
            if i > max_reachable:  # If the current index is beyond the farthest we can reach, return false
                return False
            max_reachable = max(max_reachable, i + jump)  # Update the farthest index we can reach
            if max_reachable >= len(nums) - 1:  # If we can reach or exceed the last index, return true
                return True

        return max_reachable >= len(nums) - 1  # In case the loop completes, check if we can reach the last index

# Example usage
solution = Solution()

# Test case 1
nums1 = [2, 3, 1, 1, 4]
print(solution.canJump(nums1))  # Output: True

# Test case 2
nums2 = [3, 2, 1, 0, 4]
print(solution.canJump(nums2))  # Output: False
