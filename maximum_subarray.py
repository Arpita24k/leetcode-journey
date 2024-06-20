class Solution:
    def maxSubArray(self, nums):
        # Initialize the variables to store the maximum sum and current sum
        max_sum = float('-inf')
        current_sum = 0
        
        # Iterate through the array
        for num in nums:
            # Add the current number to the current sum
            current_sum += num
            
            # Update the max_sum if the current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
            
            # If current_sum becomes negative, reset it to zero
            if current_sum < 0:
                current_sum = 0
        
        return max_sum

# Example usage
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums1))  # Output: 6

nums2 = [1]
print(Solution().maxSubArray(nums2))  # Output: 1

nums3 = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums3))  # Output: 23
