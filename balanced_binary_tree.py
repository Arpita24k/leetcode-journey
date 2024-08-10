# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_balance(node: TreeNode) -> (bool, int):
            if not node:  # If the node is None, it's balanced with height -1
                return True, -1
            
            left_balanced, left_height = check_balance(node.left)  # Check left subtree
            right_balanced, right_height = check_balance(node.right)  # Check right subtree
            
            # Current node is balanced if both subtrees are balanced and the height difference is <= 1
            current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            # Current height is 1 more than the maximum height of the two subtrees
            current_height = 1 + max(left_height, right_height)
            
            return current_balanced, current_height
        
        balanced, _ = check_balance(root)  # We only care about the balanced status
        return balanced

# Example usage:
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    solution = Solution()
    print(solution.isBalanced(root1))  # Output: True
    
    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(solution.isBalanced(root2))  # Output: False
    
    # Example 3
    root3 = None  # Empty tree
    print(solution.isBalanced(root3))  # Output: True
