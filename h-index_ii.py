class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Check if citations at mid is greater than or equal to number of papers remaining
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return n - left

# Example usage:
solution = Solution()

# Example 1:
citations = [0, 1, 3, 5, 6]
print("H-index:", solution.hIndex(citations))  # Output: 3

# Example 2:
citations = [1, 2, 100]
print("H-index:", solution.hIndex(citations))  # Output: 2
