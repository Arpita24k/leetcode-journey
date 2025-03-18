class Solution:
    def longestNiceSubarray(self, nums):
        left = 0  # Left pointer of sliding window
        curr_bits = 0  # Store OR of elements in the window
        max_len = 0
        
        for right in range(len(nums)):
            # If nums[right] has common bits with the window, shrink from left
            while (curr_bits & nums[right]) != 0:
                curr_bits ^= nums[left]  # Remove nums[left] from the OR set
                left += 1  # Move left pointer forward
            
            # Include nums[right] in the OR window
            curr_bits |= nums[right]
            
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
