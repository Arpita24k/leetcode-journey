from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the next part of the list
                backtrack(start + 1)
                # Backtrack (swap the elements back)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack()
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [0, 1]
    nums3 = [1]
    
    print(solution.permute(nums1))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(solution.permute(nums2))  # Output: [[0, 1], [1, 0]]
    print(solution.permute(nums3))  # Output: [[1]]
