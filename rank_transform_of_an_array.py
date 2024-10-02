class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Create a sorted list of the unique elements in arr
        sorted_unique = sorted(set(arr))
        
        # Create a dictionary to map each element to its rank
        rank_map = {val: rank + 1 for rank, val in enumerate(sorted_unique)}
        
        # Replace each element in arr with its rank
        return [rank_map[num] for num in arr]

# Example usage:
solution = Solution()

# Example 1
arr1 = [40, 10, 20, 30]
result1 = solution.arrayRankTransform(arr1)
print(f"Input: {arr1}, Output: {result1}")

# Example 2
arr2 = [100, 100, 100]
result2 = solution.arrayRankTransform(arr2)
print(f"Input: {arr2}, Output: {result2}")

# Example 3
arr3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
result3 = solution.arrayRankTransform(arr3)
print(f"Input: {arr3}, Output: {result3}")
