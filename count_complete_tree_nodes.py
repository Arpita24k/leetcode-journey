# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Function to compute the tree height by going all the way to the left
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_height = compute_height(root.left)
        right_height = compute_height(root.right)
        
        if left_height == right_height:
            # Left subtree is a perfect binary tree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree of one level less
            return (1 << right_height) + self.countNodes(root.left)

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# solution = Solution()
# print(solution.countNodes(root))  # Output: 6
