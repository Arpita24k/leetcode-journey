# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Create a dummy node which will be the new head of the sorted list
        dummy = ListNode(0)
        
        # Iterate over the original list
        current = head
        while current:
            # At each iteration, we insert current into the sorted list
            prev = dummy
            # Find the right place to insert current node in the sorted list
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Store the next node to be processed in the original list
            next_temp = current.next
            
            # Insert the current node into the sorted list
            current.next = prev.next
            prev.next = current
            
            # Move to the next node in the original list
            current = next_temp
        
        # Return the head of the sorted list, which is after the dummy node
        return dummy.next

# Example usage:
if __name__ == "__main__":
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    
    # Helper function to print a linked list
    def print_linked_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        print(result)
    
    solution = Solution()
    
    # Test Case 1
    head1 = create_linked_list([4, 2, 1, 3])
    sorted_head1 = solution.insertionSortList(head1)
    print_linked_list(sorted_head1)  # Output: [1, 2, 3, 4]
    
    # Test Case 2
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    sorted_head2 = solution.insertionSortList(head2)
    print_linked_list(sorted_head2)  # Output: [-1, 0, 3, 4, 5]
