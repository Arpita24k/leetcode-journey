class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize previous node to None and current node to head
        prev = None
        curr = head
        
        # Iterate through the list
        while curr:
            # Store the next node
            next_temp = curr.next
            # Reverse the current node's next pointer
            curr.next = prev
            # Move previous and current nodes one step forward
            prev = curr
            curr = next_temp
        
        # At the end, prev will be the new head of the reversed list
        return prev

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
# Create linked lists
head1 = createLinkedList([1, 2, 3, 4, 5])
head2 = createLinkedList([1, 2])

# Print the original lists
print("Original list 1:")
printList(head1)
print("Original list 2:")
printList(head2)

# Create a Solution object and reverse the lists
solution = Solution()
reversed_head1 = solution.reverseList(head1)
reversed_head2 = solution.reverseList(head2)

# Print the reversed lists
print("Reversed list 1:")
printList(reversed_head1)
print("Reversed list 2:")
printList(reversed_head2)
