from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        # We consider four possible scenarios to find the minimum difference
        option1 = nums[-1] - nums[3]      # Remove the three smallest
        option2 = nums[-2] - nums[2]      # Remove the two smallest and the largest
        option3 = nums[-3] - nums[1]      # Remove the smallest and the two largest
        option4 = nums[-4] - nums[0]      # Remove the three largest
        
        return min(option1, option2, option3, option4)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDifference([5, 3, 2, 4]))           # Output: 0
    print(solution.minDifference([1, 5, 0, 10, 14]))      # Output: 1
    print(solution.minDifference([3, 100, 20]))           # Output: 0
    print(solution.minDifference([6, 6, 0, 1, 1, 4, 6])) 
