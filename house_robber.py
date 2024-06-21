class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize an array to store the maximum amount of money that can be robbed up to each house
        dp = [0] * len(nums)
        
        # The maximum money that can be robbed from the first house is the value of the first house itself
        dp[0] = nums[0]
        # The maximum money that can be robbed from the first two houses is the maximum of the first two houses' values
        dp[1] = max(nums[0], nums[1])
        
        # Iterate over the houses starting from the third house
        for i in range(2, len(nums)):
            # For each house, decide whether to rob it or not
            # If we rob the current house, we add its value to the maximum money that can be robbed from two houses back
            # If we don't rob the current house, the maximum money is the same as the previous house
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        # The answer is the maximum money that can be robbed from all the houses
        return dp[-1]

# Example usage
nums1 = [1, 2, 3, 1]
print(Solution().rob(nums1))  # Output: 4

nums2 = [2, 7, 9, 3, 1]
print(Solution().rob(nums2))  # Output: 12
