# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Recursively calculate the maximum contribution from left and right children
            left_gain = max(max_gain(node.left), 0)  # Only take positive gains
            right_gain = max(max_gain(node.right), 0)  # Only take positive gains
            
            # The maximum path sum with the current node as the root of the path
            price_newpath = node.val + left_gain + right_gain
            
            # Update the global maximum sum if this path is better
            self.max_sum = max(self.max_sum, price_newpath)
            
            # Return the maximum gain if the current node is to be included in the upward path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(solution.maxPathSum(root1))  # Output: 6
    
    # Test Case 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(solution.maxPathSum(root2))  # Output: 42
