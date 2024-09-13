class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # Step 1: Compute prefix XOR array
        n = len(arr)
        prefix = [0] * (n + 1)  # prefix[i] will store XOR of arr[0] to arr[i-1]
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        
        # Step 2: Process each query
        result = []
        for left, right in queries:
            # XOR from arr[left] to arr[right] is prefix[right + 1] ^ prefix[left]
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result

# Example usage:
solution = Solution()

# Example 1:
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(solution.xorQueries(arr, queries))  # Output: [2, 7, 14, 8]

# Example 2:
arr = [4, 8, 2, 10]
queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
print(solution.xorQueries(arr, queries))  # Output: [8, 0, 4, 4]
