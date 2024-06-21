class Solution:
    def majorityElement(self, nums):
        # Initialize the candidate for majority element and the count
        candidate = None
        count = 0
        
        # First pass: Find the candidate for the majority element
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # The candidate is the majority element
        return candidate

# Example usage
nums1 = [3, 2, 3]
print(Solution().majorityElement(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums2))  # Output: 2
