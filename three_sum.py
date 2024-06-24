from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use the two-pointer technique effectively
        nums.sort()
        result = []

        # Iterate through the array, considering each element as the first element of the triplet
        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            left, right = i + 1, len(nums) - 1

            # Use the two-pointer technique to find pairs that sum up to the negative of nums[i]
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # If the sum is zero, add the triplet to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    # If the sum is less than zero, move the left pointer to the right to increase the sum
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left to decrease the sum
                    right -= 1

        return result

# Example usage:
solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0, 1, 1]))             # Output: []
print(solution.threeSum([0, 0, 0]))             # Output: [[0, 0, 0]]
