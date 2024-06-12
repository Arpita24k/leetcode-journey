from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        
        for num in count1:
            if num in count2:
                min_count = min(count1[num], count2[num])
                result.extend([num] * min_count)
                
        return result

# Example usage:
solution = Solution()

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersect(nums1, nums2))  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersect(nums1, nums2))  # Output: [4, 9]
