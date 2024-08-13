# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        # Traverse the list
        while current and current.next:
            if current.val == current.next.val:
                # Skip the next node since it's a duplicate
                current.next = current.next.next
            else:
                # Move to the next distinct element
                current = current.next
        
        return head

# Example usage:
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

if __name__ == "__main__":
    # Example 1: Input: head = [1,1,2]
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    solution = Solution()
    new_head1 = solution.deleteDuplicates(head1)
    print_list(new_head1)  # Output: [1, 2]
    
    # Example 2: Input: head = [1,1,2,3,3]
    head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    new_head2 = solution.deleteDuplicates(head2)
    print_list(new_head2)  # Output: [1, 2, 3]
