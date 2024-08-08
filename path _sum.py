#Path Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # If the tree is empty, return False
        if not root:
            return False
        
        # If we reached a leaf node, check if the current sum equals targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Otherwise, continue the search in the left and right subtrees
        # Subtract the current node's value from targetSum
        targetSum -= root.val
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Example usage:
# Creating the tree for example 1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

solution = Solution()
print(solution.hasPathSum(root, 22))  # Output: true

# Creating the tree for example 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(solution.hasPathSum(root, 5))  # Output: false

# Creating the tree for example 3 (empty tree)
root = None

print(solution.hasPathSum(root, 0))  # Output: false
