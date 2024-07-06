import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Initialize the heap with the head nodes of all lists
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        # Dummy node to start the result list
        dummy = ListNode()
        current = dummy
        
        # Process the heap and build the result list
        while min_heap:
            value, index, node = heapq.heappop(min_heap)
            current.next = ListNode(value)
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next

# Helper functions to create and print linked lists for testing
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    
    merged_list = solution.mergeKLists(lists)
    print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
