from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # Add the current node to the path
            path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and if the path sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))  # Append a copy of the current path
            
            # Continue the search on the left and right subtrees
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            
            # Backtrack
            path.pop()
        
        result = []
        dfs(root, 0, [])
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)
    targetSum1 = 22
    print(solution.pathSum(root1, targetSum1))  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
    
    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    targetSum2 = 5
    print(solution.pathSum(root2, targetSum2))  # Output: []
    
    # Example 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    targetSum3 = 0
    print(solution.pathSum(root3, targetSum3))  # Output: []
