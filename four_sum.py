from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    
    print(solution.fourSum(nums1, target1))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(solution.fourSum(nums2, target2))  # Output: [[2, 2, 2, 2]]
