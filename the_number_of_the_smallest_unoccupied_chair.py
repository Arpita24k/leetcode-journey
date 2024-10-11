import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        # Create a list of events: (time, type, friend_index)
        events = []
        
        for i, (arrival, leaving) in enumerate(times):
            events.append((arrival, 'arrive', i))
            events.append((leaving, 'leave', i))
        
        # Sort events based on time. If two events have the same time, 'leave' goes before 'arrive'.
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))

        # Min-heap to keep track of the smallest available chairs.
        available_chairs = []
        heapq.heapify(available_chairs)
        
        # Dictionary to store which chair each friend is sitting on
        friend_to_chair = {}

        # Initialize all chairs from 0 to n - 1 in the heap (since n friends, at most n chairs will be used)
        for i in range(len(times)):
            heapq.heappush(available_chairs, i)
        
        for time, event_type, friend in events:
            if event_type == 'arrive':
                # Assign the smallest available chair
                chair = heapq.heappop(available_chairs)
                friend_to_chair[friend] = chair
                # If the arriving friend is the targetFriend, return the chair
                if friend == targetFriend:
                    return chair
            else:  # event_type == 'leave'
                # Free the chair when a friend leaves
                heapq.heappush(available_chairs, friend_to_chair[friend])

# Example usage:
# solution = Solution()
# print(solution.smallestChair([[1,4],[2,3],[4,6]], 1))  # Output: 1
# print(solution.smallestChair([[3,10],[1,5],[2,6]], 0))  # Output: 2
