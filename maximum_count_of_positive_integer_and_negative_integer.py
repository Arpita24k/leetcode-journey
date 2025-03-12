from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums):
        # Find first non-negative index (count of negatives)
        neg_count = bisect_left(nums, 0)
        
        # Find first positive index (count of positives)
        pos_count = len(nums) - bisect_right(nums, 0)
        
        return max(neg_count, pos_count)

# Example Test Cases
solution = Solution()
print(solution.maximumCount([-2,-1,-1,1,2,3]))  # Output: 3
print(solution.maximumCount([-3,-2,-1,0,0,1,2]))  # Output: 3
print(solution.maximumCount([5,20,66,1314]))  # Output: 4
