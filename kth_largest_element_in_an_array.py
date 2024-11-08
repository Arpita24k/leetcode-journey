import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Step 1: Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Transform list into a heap
        
        # Step 2: Process the remaining elements in nums
        for num in nums[k:]:
            if num > min_heap[0]:  # Only push if num is larger than the smallest in heap
                heapq.heappushpop(min_heap, num)  # Push num and pop the smallest element
        
        # The root of the heap is now the k-th largest element
        return min_heap[0]

# Example usage
solution = Solution()

# Test case 1
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print("Output for nums1:", solution.findKthLargest(nums1, k1))  # Expected: 5

# Test case 2
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print("Output for nums2:", solution.findKthLargest(nums2, k2))  # Expected: 4
