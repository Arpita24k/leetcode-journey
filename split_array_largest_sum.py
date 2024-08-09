class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(mid):
            current_sum = 0
            required_splits = 1
            for num in nums:
                if current_sum + num > mid:
                    required_splits += 1
                    current_sum = num
                    if required_splits > k:
                        return False
                else:
                    current_sum += num
            return True
        
        low, high = max(nums), sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        
        return low

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums = [7, 2, 5, 10, 8]
    k = 2
    print("Input:", nums, "k =", k)
    result = solution.splitArray(nums, k)
    print("Output:", result)  # Output should be 18
    
    # Test Case 2
    nums = [1, 2, 3, 4, 5]
    k = 2
    print("\nInput:", nums, "k =", k)
    result = solution.splitArray(nums, k)
    print("Output:", result)  # Output should be 9
