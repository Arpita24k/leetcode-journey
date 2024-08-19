from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the deque that are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current element at the back of the deque
            dq.append(i)
            
            # The front of the deque contains the index of the maximum element for the current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    print(solution.maxSlidingWindow(nums1, k1))  # Output: [3, 3, 5, 5, 6, 7]
    
    # Test Case 2
    nums2 = [1]
    k2 = 1
    print(solution.maxSlidingWindow(nums2, k2))  # Output: [1]
