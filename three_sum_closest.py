from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Found the exact target sum
        
        return closest_sum

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
    print(solution.threeSumClosest([0, 0, 0], 1))      # Output: 0
