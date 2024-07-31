class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start, path):
            # If the combination is of length k, add it to the result
            if len(path) == k:
                result.append(path[:])
                return
            
            # Iterate over the range, starting from the current number
            for i in range(start, n + 1):
                path.append(i)  # Include the current number
                backtrack(i + 1, path)  # Move to the next number
                path.pop()  # Backtrack to try the next number
        
        result = []  # This will store all the valid combinations
        backtrack(1, [])  # Initialize backtracking with the first number and an empty path
        return result

# Example usage:
sol = Solution()
print(sol.combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(sol.combine(1, 1))  # Output: [[1]]
