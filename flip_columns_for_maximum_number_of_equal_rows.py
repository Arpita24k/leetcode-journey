class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        """
        Given a binary matrix, returns the maximum number of rows
        that can be made identical by flipping columns.
        """
        from collections import defaultdict  # Use defaultdict for efficient counting

        pattern_count = defaultdict(int)  # Dictionary to count normalized patterns
        for row in matrix:
            # Normalize the row: if first element is 0, keep as is; otherwise, flip
            pattern = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            pattern_count[pattern] += 1  # Increment count of the pattern

        # Return the maximum frequency of any normalized pattern
        return max(pattern_count.values())


# Example Usage
if __name__ == "__main__":
    solution = Solution()  # Instantiate the Solution class

    # Test cases
    matrix1 = [[0, 1], [1, 1]]
    matrix2 = [[0, 1], [1, 0]]
    matrix3 = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]

    # Output results
    print(solution.maxEqualRowsAfterFlips(matrix1))  # Output: 1
    print(solution.maxEqualRowsAfterFlips(matrix2))  # Output: 2
    print(solution.maxEqualRowsAfterFlips(matrix3))  # Output: 2
