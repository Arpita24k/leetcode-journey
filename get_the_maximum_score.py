class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 10**9 + 7  # To return the result modulo 10^9 + 7
        
        i, j = 0, 0  # Pointers for nums1 and nums2
        sum1, sum2 = 0, 0  # Accumulated sums for both arrays
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]  # Add nums1's element to sum1
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]  # Add nums2's element to sum2
                j += 1
            else:
                # When both elements are equal, switch paths
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        
        # Add remaining elements from nums1 (if any)
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        
        # Add remaining elements from nums2 (if any)
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1
        
        # Return the maximum of the two paths, modulo 10^9 + 7
        return max(sum1, sum2) % MOD

# Usage example:
solution = Solution()
print(solution.maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]))  # Output: 30
print(solution.maxSum([1, 3, 5, 7, 9], [3, 5, 100]))    # Output: 109
print(solution.maxSum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))  # Output: 40
