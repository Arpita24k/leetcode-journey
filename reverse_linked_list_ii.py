class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Edge case: when the list is empty or there's no need to reverse
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases like reversing from the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the `left` position
        for _ in range(left - 1):
            prev = prev.next
        
        # `start` will point to the first node in the sublist to be reversed
        start = prev.next
        # `then` will point to the node that will be reversed
        then = start.next
        
        # Reverse the sublist from left to right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next

# Example usage:
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left1, right1 = 2, 4
    new_head1 = solution.reverseBetween(head1, left1, right1)
    print_list(new_head1)  # Output: [1, 4, 3, 2, 5]
    
    # Test Case 2
    head2 = ListNode(5)
    left2, right2 = 1, 1
    new_head2 = solution.reverseBetween(head2, left2, right2)
    print_list(new_head2)  # Output: [5]
