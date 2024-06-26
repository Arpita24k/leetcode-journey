class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Inorder traversal to get sorted node values
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_vals = inorder_traversal(root)
        
        # Step 2: Build balanced BST from sorted node values
        def build_balanced_bst(vals):
            if not vals:
                return None
            mid = len(vals) // 2
            root = TreeNode(vals[mid])
            root.left = build_balanced_bst(vals[:mid])
            root.right = build_balanced_bst(vals[mid+1:])
            return root
        
        return build_balanced_bst(sorted_vals)

# Helper function to print the tree (for testing purposes)
def print_tree(node, level=0, label="."):
    indent = " " * (4 * level) + label + ": "
    print(indent + str(node.val) if node else indent + "None")
    if node:
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

# Example usage
# Building the input tree: [1,null,2,null,3,null,4,null,null]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
balanced_root = solution.balanceBST(root)

# Print the balanced tree
print_tree(balanced_root)
