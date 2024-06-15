class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left, right = head, prev
        while right:  # Only need to compare until the end of the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
head1 = createLinkedList([1, 2, 2, 1])
head2 = createLinkedList([1, 2])

solution = Solution()

print("List 1:")
printList(head1)
print("Is Palindrome:", solution.isPalindrome(head1))  # Output: True

print("List 2:")
printList(head2)
print("Is Palindrome:", solution.isPalindrome(head2))  # Output: False
