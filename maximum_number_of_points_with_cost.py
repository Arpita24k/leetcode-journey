class Solution:
    def maxPoints(self, points):
        m, n = len(points), len(points[0])

        # Initialize dp to the first row
        dp = points[0]

        for r in range(1, m):
            # Left pass to calculate left_dp
            left_dp = [0] * n
            left_dp[0] = dp[0]
            for c in range(1, n):
                left_dp[c] = max(left_dp[c - 1] - 1, dp[c])

            # Right pass to calculate right_dp
            right_dp = [0] * n
            right_dp[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right_dp[c] = max(right_dp[c + 1] - 1, dp[c])

            # Calculate the dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left_dp[c], right_dp[c])

        # The answer is the max value in the last row's dp array
        return max(dp)

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    points1 = [[1,2,3],[1,5,1],[3,1,1]]
    print(solution.maxPoints(points1))  # Output: 9

    # Test Case 2
    points2 = [[1,5],[2,3],[4,2]]
    print(solution.maxPoints(points2))  # Output: 11
