import heapq

class Solution:
    def getSkyline(self, buildings):
        # Create events for the start and end of each building
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        
        # Sort events by x-coordinate, and by height for start events before end events
        events.sort()
        
        # Max-heap to keep track of the current heights of buildings
        result = []
        max_heap = [(0, float('inf'))]  # (height, end)
        
        for x, neg_height, end in events:
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, end))
            
            current_height = -max_heap[0][0]
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])
        
        return result

# Test the function with the provided examples
sol = Solution()
print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10],
