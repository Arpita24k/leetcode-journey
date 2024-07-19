class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one element
        if not head or not head.next:
            return head

        # Helper function to find the middle of the list
        def get_middle(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Helper function to merge two sorted lists
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next, l1 = l1, l1.next
                else:
                    tail.next, l2 = l2, l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        
        # Split the list into two halves
        mid = get_middle(head)
        right_head = mid.next
        mid.next = None
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        # Merge the sorted halves
        return merge(left, right)

# Helper function to convert a list to a linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

# Example usage:
solution = Solution()

# Convert list to linked list
input_list = list_to_linkedlist([4,2,1,3])
# Sort the linked list
sorted_list_head = solution.sortList(input_list)
# Convert linked list back to list
print(linkedlist_to_list(sorted_list_head))  # Output: [1, 2, 3, 4]

input_list = list_to_linkedlist([-1,5,3,4,0])
sorted_list_head = solution.sortList(input_list)
print(linkedlist_to_list(sorted_list_head))  # Output: [-1, 0, 3, 4, 5]

input_list = list_to_linkedlist([])
sorted_list_head = solution.sortList(input_list)
print(linkedlist_to_list(sorted_list_head))  # Output: []
