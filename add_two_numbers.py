class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node and current pointer
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Sum the values of l1, l2 and carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            # Update carry and the new digit
            carry = total // 10
            new_digit = total % 10
            
            # Append the new digit to the result list
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move to the next nodes in l1 and l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [7, 0, 8]
    
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [0]
    
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
