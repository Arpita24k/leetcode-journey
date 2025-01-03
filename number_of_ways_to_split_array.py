class Solution:
    def waysToSplitArray(self, nums):
        """
        Returns the number of valid splits in the array.
        """
        # Step 1: Calculate total sum of the array
        total_sum = sum(nums)
        
        # Step 2: Initialize variables
        left_sum = 0
        count = 0
        
        # Step 3: Iterate and check valid splits
        for i in range(len(nums) - 1):  # Stop at n-1 since the right part must not be empty
            left_sum += nums[i]  # Update left sum
            right_sum = total_sum - left_sum  # Calculate right sum
            
            if left_sum >= right_sum:
                count += 1
        
        return count


# Example usage:
solution = Solution()

# Test Case 1
nums1 = [10, 4, -8, 7]
print(solution.waysToSplitArray(nums1))  # Output: 2

# Test Case 2
nums2 = [2, 3, 1, 0]
print(solution.waysToSplitArray(nums2))  # Output: 2
