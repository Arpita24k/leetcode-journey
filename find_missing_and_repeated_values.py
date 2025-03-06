class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        N = n * n
        
        # Compute expected sum and sum of squares
        S_expected = (N * (N + 1)) // 2
        S2_expected = (N * (N + 1) * (2 * N + 1)) // 6
        
        # Compute actual sum and sum of squares
        num_count = {}
        S_actual = 0
        S2_actual = 0
        repeated = -1
        
        for row in grid:
            for num in row:
                S_actual += num
                S2_actual += num * num
                if num in num_count:
                    repeated = num
                num_count[num] = num_count.get(num, 0) + 1
        
        # Missing number calculation
        ΔS = S_expected - S_actual  # b - a
        ΔS2 = S2_expected - S2_actual  # b^2 - a^2
        
        missing = (ΔS2 // ΔS + ΔS) // 2
        return [repeated, missing]

# Example Test Cases
solution = Solution()
print(solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]))  # Output: [2, 4]
print(solution.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))  # Output: [9, 5]
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        N = n * n
        
        # Compute expected sum and sum of squares
        S_expected = (N * (N + 1)) // 2
        S2_expected = (N * (N + 1) * (2 * N + 1)) // 6
        
        # Compute actual sum and sum of squares
        num_count = {}
        S_actual = 0
        S2_actual = 0
        repeated = -1
        
        for row in grid:
            for num in row:
                S_actual += num
                S2_actual += num * num
                if num in num_count:
                    repeated = num
                num_count[num] = num_count.get(num, 0) + 1
        
        # Missing number calculation
        ΔS = S_expected - S_actual  # b - a
        ΔS2 = S2_expected - S2_actual  # b^2 - a^2
        
        missing = (ΔS2 // ΔS + ΔS) // 2
        return [repeated, missing]

# Example Test Cases
solution = Solution()
print(solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]))  # Output: [2, 4]
print(solution.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))  # Output: [9, 5]
