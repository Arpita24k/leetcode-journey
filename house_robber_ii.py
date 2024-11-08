class Solution:
    def rob(self, nums):
        # Handle the edge case with only one house
        if len(nums) == 1:
            return nums[0]

        # Helper function to calculate max rob amount in a linear array (not circular)
        def rob_linear(houses):
            prev, curr = 0, 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr

        # Case 1: Rob houses from the first to the second-last
        max1 = rob_linear(nums[:-1])
        
        # Case 2: Rob houses from the second to the last
        max2 = rob_linear(nums[1:])

        # The result is the maximum of the two cases
        return max(max1, max2)

# Example usage
solution = Solution()

# Test case 1
nums1 = [2, 3, 2]
print("Output for nums1:", solution.rob(nums1))  # Expected: 3

# Test case 2
nums2 = [1, 2, 3, 1]
print("Output for nums2:", solution.rob(nums2))  # Expected: 4

# Test case 3
nums3 = [1, 2, 3]
print("Output for nums3:", solution.rob(nums3))  # Expected: 3
