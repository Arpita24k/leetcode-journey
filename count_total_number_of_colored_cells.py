class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * n - 2 * n + 1

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.coloredCells(1))  # Output: 1
    print(solution.coloredCells(2))  # Output: 5
    print(solution.coloredCells(3))  # Output: 13
    print(solution.coloredCells(4))  # Output: 25
