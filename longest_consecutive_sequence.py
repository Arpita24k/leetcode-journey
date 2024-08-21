class Solution:
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        max_length = 0
        
        for num in nums:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums1))  # Output: 4
    
    # Test Case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(solution.longestConsecutive(nums2))  # Output: 9
