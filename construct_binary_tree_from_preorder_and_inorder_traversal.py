# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        # The first element in preorder list is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder list
        mid = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

# Example usage
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
root = solution.buildTree(preorder, inorder)

# This function can be used to print the tree in a human-readable format, 
# or you can use any tree visualization tools to verify the structure.
def print_tree(node):
    """Preorder traversal to print the tree."""
    if not node:
        return None
    return [node.val, print_tree(node.left), print_tree(node.right)]

print(print_tree(root))
