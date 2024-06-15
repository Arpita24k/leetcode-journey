class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Iterate through the list
        while fast and fast.next:
            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next
            
            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True
        
        # If we reach here, there is no cycle
        return False

# Helper functions to create and print linked list
def createLinkedList(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    
    if pos == 0:
        cycle_node = head
    
    for index, value in enumerate(arr[1:], 1):
        current.next = ListNode(value)
        current = current.next
        if index == pos:
            cycle_node = current
    
    # Create cycle if pos is valid
    if cycle_node:
        current.next = cycle_node
    
    return head

def printList(head: ListNode, limit=10) -> None:
    current = head
    count = 0
    while current and count < limit:
        print(current.val, end=" -> ")
        current = current.next
        count += 1
    if current:
        print("...")
    else:
        print("None")

# Example usage
head1 = createLinkedList([3, 2, 0, -4], 1)
head2 = createLinkedList([1, 2], 0)
head3 = createLinkedList([1], -1)

solution = Solution()

print("List 1 (expected cycle):")
printList(head1)
print("Has cycle:", solution.hasCycle(head1))  # Output: True

print("\nList 2 (expected cycle):")
printList(head2)
print("Has cycle:", solution.hasCycle(head2))  # Output: True

print("\nList 3 (expected no cycle):")
printList(head3)
print("Has cycle:", solution.hasCycle(head3))  # Output: False
