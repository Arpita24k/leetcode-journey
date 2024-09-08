class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        # Step 1: Count the number of nodes in the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = length // k  # Minimum size of each part
        extra_nodes = length % k  # Extra nodes to distribute among the first 'extra_nodes' parts
        
        # Step 3: Create the parts
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            # Determine the size of the current part
            current_part_size = part_size + (1 if i < extra_nodes else 0)
            
            # Traverse the current part (move current pointer)
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Disconnect the current part from the rest of the list
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list back to list (for easy output visualization)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
sol = Solution()

# Example 1:
head = list_to_linked_list([1, 2, 3])
k = 5
result = sol.splitListToParts(head, k)
output = [linked_list_to_list(part) for part in result]
print(output)  # Output: [[1], [2], [3], [], []]

# Example 2:
head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
k = 3
result = sol.splitListToParts(head, k)
output = [linked_list_to_list(part) for part in result]
print(output)  # Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
