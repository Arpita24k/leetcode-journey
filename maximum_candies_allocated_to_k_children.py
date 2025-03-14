class Solution:
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0  # Not enough candies for each child to get at least one

        # Binary Search for max candies per child
        left, right = 1, max(candies)
        result = 0

        def canAllocate(mid):
            """Check if we can allocate at least k piles of size 'mid'."""
            count = sum(candy // mid for candy in candies)  # Total children served
            return count >= k

        while left <= right:
            mid = (left + right) // 2
            if canAllocate(mid):
                result = mid  # Valid allocation, try for a larger `mid`
                left = mid + 1
            else:
                right = mid - 1  # Reduce `mid` to fit `k` children

        return result

# Example Test Cases
solution = Solution()
print(solution.maximumCandies([5, 8, 6], 3))  # Output: 5
print(solution.maximumCandies([2, 5], 11))    # Output: 0
