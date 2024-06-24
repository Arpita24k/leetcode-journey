# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both trees are empty
        if not p and not q:
            return True
        
        # One tree is empty and the other is not
        if not p or not q:
            return False
        
        # Both trees are non-empty, compare their values and their subtrees
        if p.val != q.val:
            return False
        
        # Recursively compare the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Helper function to create a binary tree from a list
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while i < len(nodes):
        node = queue.popleft()
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# Example usage
from collections import deque

p = create_tree([1, 2, 3])
q = create_tree([1, 2, 3])

solution = Solution()
print(solution.isSameTree(p, q))  # Output: True

p = create_tree([1, 2])
q = create_tree([1, None, 2])
print(solution.isSameTree(p, q))  # Output: False

p = create_tree([1, 2, 1])
q = create_tree([1, 1, 2])
print(solution.isSameTree(p, q))  # Output: False
