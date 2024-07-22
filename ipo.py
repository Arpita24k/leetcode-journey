import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: [int], capital: [int]) -> int:
        # Create a list of projects with (capital, profit)
        projects = list(zip(capital, profits))
        
        # Sort projects based on capital requirements
        projects.sort(key=lambda x: x[0])
        
        # Min-heap for capital requirements and max-heap for profits
        min_heap = []
        max_heap = []
        
        # Initialize index for iterating over projects
        i = 0
        
        for _ in range(k):
            # Push all projects that can be started with the current capital to the max-heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Use negative to simulate max-heap
                i += 1
            
            # If max-heap is empty, no more projects can be started
            if not max_heap:
                break
            
            # Pop the most profitable project and add its profit to current capital
            w += -heapq.heappop(max_heap)
        
        return w

# Examples
solution = Solution()
print(solution.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))  # Output: 4
print(solution.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))  # Output: 6
