class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_linked_list(start, end):
            prev, curr = None, start
            while curr != end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth_node = group_prev
            # Find the k-th node
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            group_next = kth_node.next

            # Reverse the group
            prev, curr = kth_node.next, group_prev.next
            while curr != group_next:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp

            # Update the pointers
            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy.next

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
head = create_linked_list([1, 2, 3, 4, 5])
k = 2
new_head = Solution().reverseKGroup(head, k)
print(linked_list_to_list(new_head))  # Output: [2, 1, 4, 3, 5]

head = create_linked_list([1, 2, 3, 4, 5])
k = 3
new_head = Solution().reverseKGroup(head, k)
print(linked_list_to_list(new_head))  # Output: [3, 2, 1, 4, 5]
