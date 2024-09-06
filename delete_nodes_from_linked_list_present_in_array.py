class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        # Convert nums to a set for O(1) lookup
        nums_set = set(nums)

        # Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the list
        while current and current.next:
            if current.next.val in nums_set:
                # Remove the node by skipping it
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        # Return the modified list, which starts at dummy.next
        return dummy.next

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

# Helper function to convert a linked list back to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
nums = [1, 2, 3]
head_list = [1, 2, 3, 4, 5]
head = list_to_linked_list(head_list)

# Use the Solution class
sol = Solution()
modified_head = sol.modifiedList(nums, head)

# Convert the resulting linked list back to a list for easy viewing
print(linked_list_to_list(modified_head))  # Output: [4, 5]
