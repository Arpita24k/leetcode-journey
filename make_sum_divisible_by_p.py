class Solution:
    def minSubarray(self, nums, p):
        n = len(nums)
        total_sum = sum(nums) % p  # Calculate total sum modulo p
        if total_sum == 0:
            return 0  # Already divisible by p, no need to remove subarray
        
        mod_map = {0: -1}  # Track prefix sum modulo p
        current_sum = 0
        min_len = n
        target = total_sum

        for i in range(n):
            current_sum = (current_sum + nums[i]) % p  # Update prefix sum mod p
            needed = (current_sum - target + p) % p  # Find the remainder to match
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])  # Check subarray length
            mod_map[current_sum] = i  # Store current prefix sum mod p

        return -1 if min_len == n else min_len  # Return result

# Example usage:
solution = Solution()
nums = [3, 1, 4, 2]
p = 6
print(solution.minSubarray(nums, p))  # Output: 1

nums = [6, 3, 5, 2]
p = 9
print(solution.minSubarray(nums, p))  # Output: 2

nums = [1, 2, 3]
p = 3
print(solution.minSubarray(nums, p))  # Output: 0
