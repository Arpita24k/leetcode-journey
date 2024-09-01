class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for i in range(1, nums.length):
            current = nums[i]

            if current < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)

            result = max(result, max_product)

        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 3, -2, 4]
    print(solution.maxProduct(nums1))  # Output: 6
    
    # Test Case 2
    nums2 = [-2, 0, -1]
    print(solution.maxProduct(nums2))  # Output: 0
