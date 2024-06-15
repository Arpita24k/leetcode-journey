class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # If the tree is empty, return depth as 0
        if not root:
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the tree is the maximum of the left and right depths plus 1 for the root
        return max(left_depth, right_depth) + 1

# Helper function to create a binary tree from a list
def createBinaryTree(arr, index=0):
    if index < len(arr):
        if arr[index] is None:
            return None
        node = TreeNode(arr[index])
        node.left = createBinaryTree(arr, 2 * index + 1)
        node.right = createBinaryTree(arr, 2 * index + 2)
        return node
    return None

# Example usage
solution = Solution()

root1 = createBinaryTree([3, 9, 20, None, None, 15, 7])
root2 = createBinaryTree([1, None, 2])

print("Maximum depth of tree 1:", solution.maxDepth(root1))  # Output: 3
print("Maximum depth of tree 2:", solution.maxDepth(root2))  # Output: 2
