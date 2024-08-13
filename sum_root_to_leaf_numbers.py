#Sum Root to Leaf Numbers
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val  # Form the current number
            
            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum
            
            # Recursively sum the numbers from both subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)

# Example usage:
if __name__ == "__main__":
    # Example 1: Input: [1,2,3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    solution = Solution()
    print(solution.sumNumbers(root1))  # Output: 25
    
    # Example 2: Input: [4,9,0,5,1]
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    print(solution.sumNumbers(root2))  # Output: 1026
