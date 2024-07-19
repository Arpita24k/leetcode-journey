class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        # Find the minimum element in each row
        row_mins = {min(row) for row in matrix}
        
        # Find the maximum element in each column
        col_maxs = {max(col) for col in zip(*matrix)}
        
        # The lucky numbers are the intersection of row minimums and column maximums
        lucky_numbers = row_mins & col_maxs
        
        return list(lucky_numbers)

# Example usage:
solution = Solution()
print(solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))  # Output: [15]
print(solution.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))  # Output: [12]
print(solution.luckyNumbers([[7,8],[1,2]]))  # Output: [7]
