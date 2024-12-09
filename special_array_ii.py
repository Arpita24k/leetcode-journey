class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        same_parity = [0] * (n - 1)
        
        # Preprocess same_parity array
        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                same_parity[i] = 1
        
        # Build prefix sum array
        prefix = [0] * n
        for i in range(n - 1):
            prefix[i + 1] = prefix[i] + same_parity[i]
        
        # Answer queries
        result = []
        for fromi, toi in queries:
            if prefix[toi] - prefix[fromi] > 0:
                result.append(False)  # Subarray is not special
            else:
                result.append(True)   # Subarray is special
        
        return result

# Example usage
solution = Solution()

nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]
print(solution.isArraySpecial(nums, queries))  # Output: [False, True]
