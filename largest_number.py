from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
        
        # Convert integers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Sort based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers to form the largest number
        largest_num = ''.join(nums_str)
        
        # Edge case: if the result is a bunch of zeros, return "0"
        if largest_num[0] == '0':
            return '0'
        
        return largest_num

# Example usage:
sol = Solution()
print(sol.largestNumber([10, 2]))  # Output: "210"
print(sol.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"
