# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        # Helper function for recursive traversal
        def traverse(node):
            if not node:
                return
            # Visit the node (add its value to the result)
            result.append(node.val)
            # Traverse the left subtree
            traverse(node.left)
            # Traverse the right subtree
            traverse(node.right)
        
        # Start traversal from the root
        traverse(root)
        return result

# Example usage:
solution = Solution()

# Example 1:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(solution.preorderTraversal(root))  # Output: [1, 2, 3]

# Example 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.left.left = TreeNode(9)
print(solution.preorderTraversal(root))  # Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]

# Example 3:
root = None
print(solution.preorderTraversal(root))  # Output: []

# Example 4:
root = TreeNode(1)
print(solution.preorderTraversal(root))  # Output: [1]
