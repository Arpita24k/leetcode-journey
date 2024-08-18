class Solution:
    def removeDuplicates(self, nums):
        # Edge case: if the length is less than or equal to 2, we don't need to do anything
        if len(nums) <= 2:
            return len(nums)
        
        # Initialize the write pointer j
        j = 1
        count = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            # If count is less than or equal to 2, write the element to the position j
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1,1,1,2,2,3]
    k1 = solution.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 5, nums1 = [1, 1, 2, 2, 3]
    
    # Test Case 2
    nums2 = [0,0,1,1,1,1,2,3,3]
    k2 = solution.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 7, nums2 = [0, 0, 1, 1, 2, 3, 3]
