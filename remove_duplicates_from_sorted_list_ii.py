class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize prev as dummy and current as head
        prev = dummy
        current = head
        
        while current:
            # Check if current node is a duplicate
            if current.next and current.val == current.next.val:
                # Skip all nodes that have the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Connect prev's next to the node after all duplicates
                prev.next = current.next
            else:
                # Move prev to the current node if it's not a duplicate
                prev = prev.next
            
            # Move current to the next node
            current = current.next
        
        # Return the modified list starting from dummy's next
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
head = create_linked_list([1,2,3,3,4,4,5])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print(linked_list_to_list(new_head))  # Output: [1, 2, 5]

head = create_linked_list([1,1,1,2,3])
new_head = solution.deleteDuplicates(head)
print(linked_list_to_list(new_head))  # Output: [2, 3]
