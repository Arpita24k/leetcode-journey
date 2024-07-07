class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev node for next swap
            prev = first_node
            head = first_node.next

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Usage:
solution = Solution()

head = create_linked_list([1, 2, 3, 4])
swapped_head = solution.swapPairs(head)
print(linked_list_to_list(swapped_head))  # Output: [2, 1, 4, 3]

head = create_linked_list([])
swapped_head = solution.swapPairs(head)
print(linked_list_to_list(swapped_head))  # Output: []

head = create_linked_list([1])
swapped_head = solution.swapPairs(head)
print(linked_list_to_list(swapped_head))  # Output: [1]
