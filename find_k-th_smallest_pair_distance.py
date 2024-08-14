#Find K-th Smallest Pair Distance
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()  # Step 1: Sort the array

        def countPairs(mid):
            count = 0
            left = 0
            # Two-pointer approach to count pairs with distance <= mid
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        # Binary search over the possible distances
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1,3,1]
    k1 = 1
    print(solution.smallestDistancePair(nums1, k1))  # Output: 0
    
    # Test Case 2
    nums2 = [1,1,1]
    k2 = 2
    print(solution.smallestDistancePair(nums2, k2))  # Output: 0
    
    # Test Case 3
    nums3 = [1,6,1]
    k3 = 3
    print(solution.smallestDistancePair(nums3, k3))  # Output: 5
