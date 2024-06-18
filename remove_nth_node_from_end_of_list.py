class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0, head)
        
        # Initialize two pointers, both starting from the dummy node
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        # This ensures the gap between first and second is n nodes apart
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end of the list
        # At this point, the second pointer will be just before the node to be removed
        while first:
            first = first.next
            second = second.next
        
        # Skip the nth node from the end by adjusting the next pointer of the second node
        second.next = second.next.next
        
        # Return the head of the modified list, which is the next node of dummy
        return dummy.next

def printList(head: ListNode) -> None:
    # Helper function to print the linked list in a readable format
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def createLinkedList(arr):
    # Helper function to create a linked list from a list of values
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
# Create a linked list [1, 2, 3, 4, 5]
head = createLinkedList([1, 2, 3, 4, 5])
n = 2

# Print the original list
print("Original list:")
printList(head)

# Create a Solution object and remove the nth node from the end
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)

# Print the modified list after removing the nth node from the end
print(f"List after removing {n}th node from the end:")
printList(new_head)
