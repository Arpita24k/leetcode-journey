class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Ensure the node to be deleted is not the last node
        if node is None or node.next is None:
            return
        
        # Copy the value from the next node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next

def printList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a list from a Python list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
# Create a linked list [4 -> 5 -> 1 -> 9]
head = createLinkedList([4, 5, 1, 9])

# Print the original list
print("Original list:")
printList(head)

# Let's say we want to delete the node with value 5 (second node)
node_to_delete = head.next  # This is the node with value 5

# Create a Solution object and delete the node
solution = Solution()
solution.deleteNode(node_to_delete)

# Print the modified list
print("List after deleting the node with value 5:")
printList(head)
