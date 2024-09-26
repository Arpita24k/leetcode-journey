class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # If the tree is empty, return None
        if not root:
            return None

        # Start with the leftmost node of the current level (beginning with root)
        leftmost = root

        # Traverse the levels as long as there are left children (since it's a perfect binary tree)
        while leftmost.left:
            # Traverse nodes at the current level
            head = leftmost
            while head:
                # Connect the left child to the right child of the same node
                head.left.next = head.right

                # If there's a next node, connect the right child to the left child of the next node
                if head.next:
                    head.right.next = head.next.left

                # Move to the next node at the same level
                head = head.next

            # Move down to the next level (leftmost node's left child)
            leftmost = leftmost.left

        # Return the root after all connections are made
        return root
