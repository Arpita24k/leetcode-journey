class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update 'ones' to track bits that have appeared once, ignoring bits that appeared twice
            ones = (ones ^ num) & ~twos
            
            # Update 'twos' to track bits that have appeared twice, ignoring bits that appeared once
            twos = (twos ^ num) & ~ones
            
        return ones

# Example usage:
solution = Solution()

# Test case 1:
nums = [2, 2, 3, 2]
print(solution.singleNumber(nums))  # Output: 3

# Test case 2:
nums = [0, 1, 0, 1, 0, 1, 99]
print(solution.singleNumber(nums))  # Output: 99
