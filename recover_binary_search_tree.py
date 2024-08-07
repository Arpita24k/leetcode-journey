# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = y = pred = predecessor = None

        while root:
            if root.left:
                # Find the rightmost node in the left subtree or the predecessor
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # Make a link to the root and move to the left subtree
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    # If there is a link, it means we have finished the left subtree
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root

                    # Remove the link and move to the right subtree
                    predecessor.right = None
                    root = root.right
            else:
                # If there is no left subtree, visit this node and move to the right subtree
                if pred and root.val < pred.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right

        # Swap the values of the two nodes
        x.val, y.val = y.val, x.val

# Example usage
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# Create a test case
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)

solution = Solution()
print("Before recovery:", inorder_traversal(root1))  # Output: [3, 1, 2]
solution.recoverTree(root1)
print("After recovery:", inorder_traversal(root1))   # Output: [1, 3, 2]

root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)

print("Before recovery:", inorder_traversal(root2))  # Output: [1, 3, 2, 4]
solution.recoverTree(root2)
print("After recovery:", inorder_traversal(root2))   # Output: [1, 2, 3, 4]
