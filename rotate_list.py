

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head  # If the list is empty, has one node, or no rotation needed, return as is
        
        # Step 1: Find the length of the list and connect the tail to the head
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        old_tail.next = head  # Make it circular
        
        # Step 2: Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        if k == 0:
            old_tail.next = None  # Break the circular link if no rotation needed
            return head
        
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Step 3: Break the circular link
        new_tail.next = None
        
        return new_head

# Helper functions to create and display the linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
sol = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
rotated_head = sol.rotateRight(head, 2)
print(print_linked_list(rotated_head))  # Output: [4, 5, 1, 2, 3]

head = create_linked_list([0, 1, 2])
rotated_head = sol.rotateRight(head, 4)
print(print_linked_list(rotated_head))  # Output: [2, 0, 1]
