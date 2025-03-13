class Solution:
    def minZeroArray(self, nums, queries):
        n = len(nums)
        
        # Function to check if we can zero the array using the first 'k' queries
        def canZeroArray(k):
            diff = [0] * (n + 1)  # Difference array for efficient range updates
            
            # Apply the first 'k' queries using the difference array
            for i in range(k):
                li, ri, vali = queries[i]
                diff[li] -= vali  # Start decrementing at li
                diff[ri + 1] += vali  # Stop decrementing after ri
            
            # Apply the difference array using prefix sum
            curr_decrement = 0
            for i in range(n):
                curr_decrement += diff[i]
                if nums[i] + curr_decrement > 0:  # If any value remains > 0, return False
                    return False
            return True

        # Binary Search for the minimum 'k'
        left, right, result = 0, len(queries), -1
        while left <= right:
            mid = (left + right) // 2
            if canZeroArray(mid):
                result = mid
                right = mid - 1  # Try for smaller 'k'
            else:
                left = mid + 1  # Increase 'k'

        return result

# Example Test Cases
solution = Solution()
print(solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))  # Output: 2
print(solution.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))  # Output: -1
