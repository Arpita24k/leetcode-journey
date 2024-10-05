class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        # Create a 3D DP array initialized to 0
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        # Helper function with memoization
        def calculatePoints(l, r, k):
            # If the range is invalid, return 0 points
            if l > r:
                return 0
            # If we already computed the result, return the cached value
            if dp[l][r][k] != 0:
                return dp[l][r][k]
            
            # Merge boxes with the same color as boxes[r]
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            
            # Calculate the points for removing the group from l to r
            dp[l][r][k] = calculatePoints(l, r - 1, 0) + (k + 1) * (k + 1)
            
            # Try merging non-adjacent boxes with the same color
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], 
                                      calculatePoints(l, i, k + 1) + calculatePoints(i + 1, r - 1, 0))
            
            return dp[l][r][k]
        
        # Start solving the problem from the entire array (from index 0 to n-1)
        return calculatePoints(0, n - 1, 0)

# Example usage:
solution = Solution()

# Testcase 1
boxes1 = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print(f"Output for boxes = {boxes1}: {solution.removeBoxes(boxes1)}")  # Expected Output: 23

# Testcase 2
boxes2 = [1, 1, 1]
print(f"Output for boxes = {boxes2}: {solution.removeBoxes(boxes2)}")  # Expected Output: 9

# Testcase 3
boxes3 = [1]
print(f"Output for boxes = {boxes3}: {solution.removeBoxes(boxes3)}")  # Expected Output: 1
