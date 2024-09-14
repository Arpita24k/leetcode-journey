class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Step 1: Find the maximum element in the array
        max_and = max(nums)
        
        # Step 2: Find the longest subarray where all elements are equal to max_and
        max_len = 0
        current_len = 0
        
        for num in nums:
            if num == max_and:
                # If the current number is equal to max_and, increase the current subarray length
                current_len += 1
                # Update max_len if the current length is longer
                max_len = max(max_len, current_len)
            else:
                # Reset current_len if the current number is not equal to max_and
                current_len = 0
        
        return max_len

# Example usage:
solution = Solution()

# Example 1:
nums = [1, 2, 3, 3, 2, 2]
print(solution.longestSubarray(nums))  # Output: 2

# Example 2:
nums = [1, 2, 3, 4]
print(solution.longestSubarray(nums))  # Output: 1
