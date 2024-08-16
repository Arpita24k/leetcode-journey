class Solution:
    def reversePairs(self, nums):
        if not nums:
            return 0
        
        def merge_sort_and_count(nums, start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort_and_count(nums, start, mid) + merge_sort_and_count(nums, mid + 1, end)
            
            # Count the reverse pairs
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Merge the two halves
            left_half = nums[start:mid + 1]
            right_half = nums[mid + 1:end + 1]
            
            l = r = 0
            for k in range(start, end + 1):
                if l < len(left_half) and (r >= len(right_half) or left_half[l] <= right_half[r]):
                    nums[k] = left_half[l]
                    l += 1
                else:
                    nums[k] = right_half[r]
                    r += 1
            
            return count
        
        return merge_sort_and_count(nums, 0, len(nums) - 1)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1,3,2,3,1]
    print(solution.reversePairs(nums1))  # Output: 2
    
    # Test Case 2
    nums2 = [2,4,3,5,1]
    print(solution.reversePairs(nums2))  # Output: 3
