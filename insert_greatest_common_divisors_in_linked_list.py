import math

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert GCD between adjacent nodes
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            # Get the GCD of current node value and next node value
            gcd_value = math.gcd(current.val, current.next.val)

            # Create a new node with the GCD value
            gcd_node = ListNode(gcd_value)

            # Insert this new GCD node between current and next node
            gcd_node.next = current.next
            current.next = gcd_node

            # Move to the next original node (after the inserted GCD node)
            current = gcd_node.next

        return head

    # Utility function to print the linked list
    def printLinkedList(self, head: ListNode):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

    # Helper function to create a linked list from a list of values
    def createLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

# Example usage:
solution = Solution()

# Input: [18, 6, 10, 3]
values = [18, 6, 10, 3]
head = solution.createLinkedList(values)

print("Original List:")
solution.printLinkedList(head)

# Inserting GCD nodes
head = solution.insertGreatestCommonDivisors(head)

print("Modified List after inserting GCDs:")
solution.printLinkedList(head)
