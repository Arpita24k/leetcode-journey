from collections import Counter

class Solution:
    def canBeEqual(self, target, arr):
        # Count the frequencies of each element in both arrays
        target_count = Counter(target)
        arr_count = Counter(arr)
        
        # Compare the counts
        return target_count == arr_count

# Example usage
solution = Solution()
target1 = [1, 2, 3, 4]
arr1 = [2, 4, 1, 3]
target2 = [7]
arr2 = [7]
target3 = [3, 7, 9]
arr3 = [3, 7, 11]

print(solution.canBeEqual(target1, arr1))  # Output: true
print(solution.canBeEqual(target2, arr2))  # Output: true
print(solution.canBeEqual(target3, arr3))  # Output: false
