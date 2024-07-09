class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] in the suffix
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap the found element with nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting right after the position i
        nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
solution = Solution()

# Test cases
nums1 = [1, 2, 3]
solution.nextPermutation(nums1)
print(nums1)  # Output: [1, 3, 2]

nums2 = [3, 2, 1]
solution.nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

nums3 = [1, 1, 5]
solution.nextPermutation(nums3)
print(nums3)  # Output: [1, 5, 1]
