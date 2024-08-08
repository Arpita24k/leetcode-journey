#Reorder List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            # Save next pointers
            tmp1 = first.next
            tmp2 = second.next

            # Reorder pointers
            first.next = second
            second.next = tmp1

            # Move to the next nodes
            first = tmp1
            second = tmp2

# Helper function to print the list (for testing)
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Creating the linked list for example 1: [1,2,3,4]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
solution.reorderList(head)
printList(head)  # Output: 1 -> 4 -> 2 -> 3 -> None

# Creating the linked list for example 2: [1,2,3,4,5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution.reorderList(head)
printList(head)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None
