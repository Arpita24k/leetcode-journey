# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.stack = []
        # Initialize by pushing all the left children of the root
        self._push_left(root)

    def _push_left(self, node: TreeNode):
        # Helper function to push all left children of the given node onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Next smallest element is the top of the stack
        node = self.stack.pop()
        # If the popped node has a right child, push all its left children
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        # Return True if there are more nodes to visit (stack is non-empty)
        return len(self.stack) > 0
# Construct the binary search tree from the example: [7, 3, 15, None, None, 9, 20]
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Create the BSTIterator object
bst_iterator = BSTIterator(root)

# Example of usage
print(bst_iterator.next())    # Output: 3
print(bst_iterator.next())    # Output: 7
print(bst_iterator.hasNext()) # Output: True
print(bst_iterator.next())    # Output: 9
print(bst_iterator.hasNext()) # Output: True
print(bst_iterator.next())    # Output: 15
print(bst_iterator.hasNext()) # Output: True
print(bst_iterator.next())    # Output: 20
print(bst_iterator.has Next()) # Output: False
