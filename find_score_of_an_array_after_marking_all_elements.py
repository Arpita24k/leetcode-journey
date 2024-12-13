

import heapq

class Solution:
    def findScore(self, nums: list[int]) -> int:
        n = len(nums)
        # Min-heap with (value, index)
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        
        # Array to track marked elements
        marked = [False] * n
        score = 0
        
        while heap:
            value, index = heapq.heappop(heap)
            # If already marked, skip
            if marked[index]:
                continue
            
            # Add the value to the score
            score += value
            
            # Mark the current element and its two adjacent ones
            marked[index] = True
            if index > 0:  # Left neighbor
                marked[index - 1] = True
            if index < n - 1:  # Right neighbor
                marked[index + 1] = True
        
        return score

# Example usage:
solution = Solution()

# Example 1
nums = [2, 1, 3, 4, 5, 2]
print(solution.findScore(nums))  # Output: 7

# Example 2
nums = [2, 3, 5, 1, 3, 2]
print(solution.findScore(nums))  # Output: 5
