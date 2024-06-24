# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # If the tree is empty, return None
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left subtree
        self.invertTree(root.left)
        # Recursively invert the right subtree
        self.invertTree(root.right)
        
        return root

# Helper function to print the tree (level order traversal)
from collections import deque
def print_tree(root):
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    # Remove trailing "null" values
    while result and result[-1] == "null":
        result.pop()
    
    return result

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
inverted_root = solution.invertTree(root)
print(print_tree(inverted_root))  # Output: [4, 7, 2, 9, 6, 3, 1]
