class Solution:
    def findTargetSumWays(self, nums, target):
        """
        Calculate the number of ways to assign '+' or '-' to nums to achieve the target.

        Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

        Returns:
        int: Number of ways to achieve the target.
        """
        # Initialize a hashmap to store the number of ways to reach each sum
        dp = {0: 1}  # Base case: one way to achieve sum = 0 (do nothing)

        # Process each number in nums
        for num in nums:
            next_dp = {}  # New hashmap for the current number
            for summ, count in dp.items():
                # Add the current number
                next_dp[summ + num] = next_dp.get(summ + num, 0) + count
                # Subtract the current number
                next_dp[summ - num] = next_dp.get(summ - num, 0) + count
            dp = next_dp  # Move to the next state

        # Return the number of ways to achieve the target
        return dp.get(target, 0)
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(solution.findTargetSumWays(nums1, target1))  # Output: 5

    # Example 2
    nums2 = [1]
    target2 = 1
    print(solution.findTargetSumWays(nums2, target2))  # Output: 1
