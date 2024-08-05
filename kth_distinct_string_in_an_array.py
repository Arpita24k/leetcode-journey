# Kth Distinct String in an Array
from collections import Counter  # Import Counter from collections to count occurrences of each string

class Solution:
    def kthDistinct(self, arr, k):
        count = Counter(arr)  # Count occurrences of each string in the array
        distinct_strings = [string for string in arr if count[string] == 1]  # Filter out distinct strings
        
        if len(distinct_strings) >= k:  # Check if there are at least k distinct strings
            return distinct_strings[k - 1]  # Return the k-th distinct string (1-indexed)
        else:
            return ""  # Return an empty string if fewer than k distinct strings

# Example usage:
solution = Solution()

arr1 = ["d", "b", "c", "b", "c", "a"]
k1 = 2
print(solution.kthDistinct(arr1, k1))  # Output: "a"

arr2 = ["aaa", "aa", "a"]
k2 = 1
print(solution.kthDistinct(arr2, k2))  # Output: "aaa"

arr3 = ["a", "b", "a"]
k3 = 3
print(solution.kthDistinct(arr3, k3))  # Output: ""
