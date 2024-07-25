class Solution:
    def jump(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # We do not need to consider the last element
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        
        return jumps

# Examples
solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))  # Output: 2
print(solution.jump([2, 3, 0, 1, 4]))  # Output: 2
