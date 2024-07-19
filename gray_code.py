class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = []
        for i in range(2 ** n):
            result.append(i ^ (i >> 1))
        return result

# Example usage:
solution = Solution()
print(solution.grayCode(2))  # Output: [0, 1, 3, 2]
print(solution.grayCode(1))  # Output: [0, 1]
