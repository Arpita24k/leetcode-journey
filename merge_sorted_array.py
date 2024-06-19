from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array.

        Args:
        nums1 (List[int]): First sorted array with m elements followed by n zeroes to accommodate nums2.
        m (int): Number of actual elements in nums1.
        nums2 (List[int]): Second sorted array.
        n (int): Number of actual elements in nums2.
        """
        # Start from the end of both arrays
        i, j, k = m - 1, n - 1, m + n - 1

        # Iterate while there are elements to compare in nums1 and nums2
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Example usage:
solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
