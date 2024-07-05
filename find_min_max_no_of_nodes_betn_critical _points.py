 from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        critical_points = []
        prev = head
        curr = head.next
        index = 1  # Start with the second node
        
        while curr.next:
            next_node = curr.next
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                critical_points.append(index)
            prev = curr
            curr = next_node
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]

# Example usage:
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    # Example 1
    head1 = create_linked_list([3, 1])
    solution = Solution()
    print(solution.nodesBetweenCriticalPoints(head1))  # Output: [-1, -1]
    
    # Example 2
    head2 = create_linked_list([5, 3, 1, 2, 5, 1, 2])
    print(solution.nodesBetweenCriticalPoints(head2))  # Output: [1, 3]
    
    # Example 3
    head3 = create_linked_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
    print(solution.nodesBetweenCriticalPoints(head3))  # Output: [3, 3]
