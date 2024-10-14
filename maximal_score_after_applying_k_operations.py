import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        # Use a max-heap to store negative values because Python's heapq is a min-heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Pop the largest element (remember it's negative in the heap)
            largest = -heapq.heappop(max_heap)
            score += largest
            
            # Compute the new value after dividing by 3 and taking the ceiling
            new_value = (largest + 2) // 3
            
            # Push the updated value back into the heap
            heapq.heappush(max_heap, -new_value)
        
        return score

# Example usage:
# solution = Solution()
# print(solution.maxKelements([10,10,10,10,10], 5))  # Output: 50
# print(solution.maxKelements([1,10,3,3,3], 3))  # Output: 17
