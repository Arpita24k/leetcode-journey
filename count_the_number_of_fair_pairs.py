Maximum XOR for Each Query   from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()  # Sort the array to use binary search effectively
        n = len(nums)
        count = 0

        for i in range(n):
            left_bound = lower - nums[i]
            right_bound = upper - nums[i]

            # Use binary search to find the range of valid pairs for nums[j]
            left_index = bisect_left(nums, left_bound, i + 1, n)  # nums[j] should be >= left_bound
            right_index = bisect_right(nums, right_bound, i + 1, n)  # nums[j] should be <= right_bound

            count += (right_index - left_index)

        return count

# Example usage:
solution = Solution()

# Example 1:
nums1 = [0, 1, 7, 4, 4, 5]
lower1 = 3
upper1 = 6
print("Output for Example 1:", solution.countFairPairs(nums1, lower1, upper1))  # Expected: 6

# Example 2:
nums2 = [1, 7, 9, 2, 5]
lower2 = 11
upper2 = 11
print("Output for Example 2:", solution.countFairPairs(nums2, lower2, upper2))  # Expected: 1
