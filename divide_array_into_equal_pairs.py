from collections import Counter

class Solution:
    def divideArray(self, nums):
        freq = Counter(nums)  # Count occurrences of each number
        return all(count % 2 == 0 for count in freq.values())  # Check if all counts are even

# Example Test Cases
solution = Solution()
print(solution.divideArray([3,2,3,2,2,2]))  # Output: True
print(solution.divideArray([1,2,3,4]))      # Output: False
