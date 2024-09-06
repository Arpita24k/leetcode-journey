class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Helper function to find the middle element of the linked list
        def find_middle(start, end):
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Main function to convert list to BST
        def convert_list_to_bst(start, end):
            if start == end:
                return None

            # Find the middle element, which becomes the root
            mid = find_middle(start, end)
            node = TreeNode(mid.val)

            # Recursively form the left and right subtrees
            node.left = convert_list_to_bst(start, mid)
            node.right = convert_list_to_bst(mid.next, end)

            return node

        return convert_list_to_bst(head, None)

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage:
head_list = [-10, -3, 0, 5, 9]
head = create_linked_list(head_list)

sol = Solution()
tree_root = sol.sortedListToBST(head)

# Helper function to perform a level-order traversal and return the tree as a list
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Print the tree in level-order format
print(level_order_traversal(tree_root))  # Example output: [0, -3, 9, -10, None, 5]
