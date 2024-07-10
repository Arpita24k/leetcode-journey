class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(0)  # Dummy node for the list of nodes < x
        before = before_head  # Pointer to build the before list
        after_head = ListNode(0)  # Dummy node for the list of nodes >= x
        after = after_head  # Pointer to build the after list
        
        current = head  # Pointer to traverse the original list
        
        while current:
            if current.val < x:
                before.next = current  # Append to before list
                before = before.next  # Move the before pointer
            else:
                after.next = current  # Append to after list
                after = after.next  # Move the after pointer
            current = current.next  # Move to the next node
        
        after.next = None  # Terminate the after list
        before.next = after_head.next  # Connect the before list to the after list
        
        return before_head.next  # The head of the new list is the node following before_head

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Example usage:
solution = Solution()

# Test cases
head1 = create_linked_list([1, 4, 3, 2, 5, 2])
x1 = 3
new_head1 = solution.partition(head1, x1)
print(linked_list_to_list(new_head1))  # Output: [1, 2, 2, 4, 3, 5]

head2 = create_linked_list([2, 1])
x2 = 2
new_head2 = solution.partition(head2, x2)
print(linked_list_to_list(new_head2))  # Output: [1, 2]
