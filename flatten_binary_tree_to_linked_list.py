#Flatten Binary Tree to Linked List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        # Flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Save the right subtree
        right_subtree = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        root.left = None  # Set left to None as per the linked list requirement
        
        # Move to the end of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Attach the previously saved right subtree
        current.right = right_subtree

# Example usage:
if __name__ == "__main__":
    # Example 1: Input: [1,2,5,3,4,null,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    solution = Solution()
    solution.flatten(root)

    # Print the flattened tree
    current = root
    while current:
        print(current.val, end=" ")
        current = current.right
    # Output: 1 2 3 4 5 6
