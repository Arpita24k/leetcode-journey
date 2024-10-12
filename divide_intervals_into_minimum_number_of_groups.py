import heapq

class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        
        # Add start and end events for each interval
        for start, end in intervals:
            events.append((start, 1))  # 1 indicates the start of an interval
            events.append((end + 1, -1))  # -1 indicates the end of an interval (end + 1 to handle inclusive intervals)
        
        # Sort events by time. If two events have the same time, end event (-1) should come before start event (1)
        events.sort()

        max_groups = 0
        active_intervals = 0

        # Sweep through events
        for time, event in events:
            active_intervals += event
            max_groups = max(max_groups, active_intervals)
        
        return max_groups

# Example usage:
# solution = Solution()
# print(solution.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))  # Output: 3
# print(solution.minGroups([[1,3],[5,6],[8,10],[11,13]]))  # Output: 1
