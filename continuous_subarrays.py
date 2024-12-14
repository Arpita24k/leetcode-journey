from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        max_deque = deque()  # Decreasing deque for maximum
        min_deque = deque()  # Increasing deque for minimum
        l = 0
        result = 0
        
        for r in range(n):
            # Update max_deque
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            max_deque.append(r)
            
            # Update min_deque
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            min_deque.append(r)
            
            # Shrink the window if condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                l += 1
                # Remove indices out of the current window
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()
            
            # Count subarrays ending at r
            result += (r - l + 1)
        
        return result

# Example usage:
solution = Solution()

# Example 1
nums = [5, 4, 2, 4]
print(solution.continuousSubarrays(nums))  # Output: 8

# Example 2
nums = [1, 2, 3]
print(solution.continuousSubarrays(nums))  # Output: 6
