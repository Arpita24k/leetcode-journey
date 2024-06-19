# Assuming isBadVersion API is defined
def isBadVersion(version: int) -> bool:
    # This is a mock implementation for testing purposes
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # Move the right pointer to mid
            else:
                left = mid + 1  # Move the left pointer to mid + 1
        
        return left

# Example usage:
solution = Solution()

# Example 1
n = 5
bad = 4
print(solution.firstBadVersion(n))  # Output: 4

# Example 2
n = 1
bad = 1
print(solution.firstBadVersion(n))  # Output: 1
