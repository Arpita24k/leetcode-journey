# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result, stack = [], []
        current = root
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)
            
            # We have visited the node and its left subtree.
            # Now, it's the right subtree's turn.
            current = current.right
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(solution.inorderTraversal(root1))  # Output: [1, 3, 2]
    
    # Test Case 2
    root2 = None
    print(solution.inorderTraversal(root2))  # Output: []
    
    # Test Case 3
    root3 = TreeNode(1)
    print(solution.inorderTraversal(root3))  # Output: [1]
