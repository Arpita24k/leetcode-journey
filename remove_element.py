class Solution:
    def removeElement(self, nums, val):
        # Pointer for the place to insert the next value that is not equal to val
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val, place it at the k-th position
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

# Example usage
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = Solution().removeElement(nums1, val1)
print(k1, nums1[:k1])  # Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = Solution().removeElement(nums2, val2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 3, 0, 4]
