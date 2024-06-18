class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)

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

root1 = createBinaryTree([2, 1, 3])
root2 = createBinaryTree([5, 1, 4, None, None, 3, 6])

print("Tree 1 is a valid BST:", solution.isValidBST(root1))  # Output: True
print("Tree 2 is a valid BST:", solution.isValidBST(root2))  # Output: False
