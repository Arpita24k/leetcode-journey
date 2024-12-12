import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Create a max-heap using negative values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        # Simulate for k seconds
        for _ in range(k):
            # Extract the largest pile (convert back to positive)
            largest = -heapq.heappop(max_heap)
            # Calculate the gifts left behind (floor of square root)
            remaining = math.floor(math.sqrt(largest))
            # Push the remaining gifts back into the heap
            heapq.heappush(max_heap, -remaining)
        
        # Calculate the total remaining gifts
        return -sum(max_heap)

# Example usage:
solution = Solution()

# Example 1
gifts = [25, 64, 9, 4, 100]
k = 4
print(solution.pickGifts(gifts, k))  # Output: 29

# Example 2
gifts = [1, 1, 1, 1]
k = 4
print(solution.pickGifts(gifts, k))  # Output: 4
