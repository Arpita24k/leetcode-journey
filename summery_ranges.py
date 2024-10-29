class Solution:
    def summaryRanges(self, nums):
        # Result list to store the ranges
        result = []
        
        if not nums:
            return result  # Return empty if nums is empty
        
        start = nums[0]  # Initialize start of the first range
        
        for i in range(1, len(nums)):
            # If nums[i] is not consecutive, end the current range
            if nums[i] != nums[i - 1] + 1:
                # Append the current range to result
                if start == nums[i - 1]:
                    result.append(str(start))  # Single number range
                else:
                    result.append(f"{start}->{nums[i - 1]}")  # Range with start and end
                start = nums[i]  # Start a new range
        
        # Add the last range after the loop
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result

# Example usage:
solution = Solution()

# Example 1
nums1 = [0, 1, 2, 4, 5, 7]
print("Example 1 Output:", solution.summaryRanges(nums1))  # Expected Output: ["0->2", "4->5", "7"]

# Example 2
nums2 = [0, 2, 3, 4, 6, 8, 9]
print("Example 2 Output:", solution.summaryRanges(nums2))  # Expected Output: ["0", "2->4", "6", "8->9"]
